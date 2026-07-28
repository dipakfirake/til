# Spring Data JPA Specifications

> _2026-07-29_ | Category: **spring-boot**

Dynamic query building for complex filters.

```java
public class ProductSpec {
    public static Specification<Product> hasCategory(String cat) {
        return (root, query, cb) -> cat == null ? null : cb.equal(root.get("category"), cat);
    }
    
    public static Specification<Product> priceBetween(Double min, Double max) {
        return (root, query, cb) -> {
            if (min != null && max != null) return cb.between(root.get("price"), min, max);
            if (min != null) return cb.greaterThanOrEqualTo(root.get("price"), min);
            if (max != null) return cb.lessThanOrEqualTo(root.get("price"), max);
            return null;
        };
    }
    
    public static Specification<Product> nameContains(String keyword) {
        return (root, query, cb) -> keyword == null ? null :
            cb.like(cb.lower(root.get("name")), "%" + keyword.toLowerCase() + "%");
    }
}

// Usage: combine dynamically
@GetMapping("/search")
public Page<Product> search(String category, Double minPrice, Double maxPrice, String keyword, Pageable page) {
    Specification<Product> spec = Specification
        .where(ProductSpec.hasCategory(category))
        .and(ProductSpec.priceBetween(minPrice, maxPrice))
        .and(ProductSpec.nameContains(keyword));
    return productRepo.findAll(spec, page);
}
```

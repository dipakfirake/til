# Spring Data JPA - Repositories

> _2026-08-24_ | Category: **spring-boot**

CRUD without writing SQL.

```java
@Entity
@Table(name = "products")
public class Product {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private double price;
    private String category;
}

public interface ProductRepository extends JpaRepository<Product, Long> {
    // Spring generates SQL automatically from method name!
    List<Product> findByCategory(String category);
    List<Product> findByPriceBetween(double min, double max);
    List<Product> findByNameContainingIgnoreCase(String keyword);
    Optional<Product> findByNameAndCategory(String name, String cat);
    
    @Query("SELECT p FROM Product p WHERE p.price > :min ORDER BY p.price DESC")
    List<Product> findExpensive(@Param("min") double min);
    
    @Query(value = "SELECT * FROM products WHERE category = ?1", nativeQuery = true)
    List<Product> findByCategoryNative(String category);
}
```

**Key Takeaway**: Name methods following Spring's convention and it generates queries automatically. Use `@Query` for complex cases.

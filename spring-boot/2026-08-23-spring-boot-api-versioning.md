# Spring Boot API Versioning

> _2026-08-23_ | Category: **spring-boot**

Manage breaking changes in APIs.

```java
// 1. URL versioning (most common)
@RestController @RequestMapping("/api/v1/users")
public class UserControllerV1 {
    @GetMapping("/{id}") public UserV1Response get(@PathVariable Long id) { }
}

@RestController @RequestMapping("/api/v2/users")
public class UserControllerV2 {
    @GetMapping("/{id}") public UserV2Response get(@PathVariable Long id) { }
}

// 2. Header versioning
@GetMapping(value = "/{id}", headers = "X-API-Version=2")
public UserV2Response getV2(@PathVariable Long id) { }

// 3. Content negotiation
@GetMapping(value = "/{id}", produces = "application/vnd.myapp.v2+json")
public UserV2Response getV2(@PathVariable Long id) { }
```

| Strategy | Pros | Cons |
|:---|:---|:---|
| URL `/v1/` | Simple, clear | URL changes |
| Header | Clean URLs | Hidden |
| Content-Type | REST purist | Complex |

**Key Takeaway**: URL versioning is simplest and most common. Version your DTOs, not your entities.

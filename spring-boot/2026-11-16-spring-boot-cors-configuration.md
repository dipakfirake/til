# Spring Boot CORS Configuration

> _2026-11-16_ | Category: **spring-boot**

Enable cross-origin requests for frontend apps.

```java
@Configuration
public class CorsConfig implements WebMvcConfigurer {
    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/api/**")
            .allowedOrigins("http://localhost:3000", "https://myapp.com")
            .allowedMethods("GET","POST","PUT","DELETE","OPTIONS")
            .allowedHeaders("*")
            .allowCredentials(true)
            .maxAge(3600);
    }
}

// Or per-controller
@CrossOrigin(origins = "http://localhost:3000")
@RestController
public class UserController { }

// Or per-method
@CrossOrigin(origins = "*")
@GetMapping("/public/data")
public List<Data> publicData() { }
```

**Key Takeaway**: Configure CORS on the backend, not frontend. In production, specify exact origins — never use `*` with credentials.

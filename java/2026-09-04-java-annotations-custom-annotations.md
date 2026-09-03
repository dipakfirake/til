# Java Annotations - Custom Annotations

> _2026-09-04_ | Category: **java**

Create and process custom annotations.

```java
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface Cacheable {
    int ttlSeconds() default 300;
    String key() default "";
}

// Usage
public class UserService {
    @Cacheable(ttlSeconds = 600, key = "user")
    public User findById(Long id) { return repo.findById(id); }
}

// Process at runtime with reflection
for (Method m : UserService.class.getDeclaredMethods()) {
    if (m.isAnnotationPresent(Cacheable.class)) {
        Cacheable c = m.getAnnotation(Cacheable.class);
        System.out.println(m.getName() + " cached for " + c.ttlSeconds() + "s");
    }
}
```

**Key Takeaway**: Frameworks like Spring use annotations heavily. Understanding custom annotations helps debug and extend frameworks.

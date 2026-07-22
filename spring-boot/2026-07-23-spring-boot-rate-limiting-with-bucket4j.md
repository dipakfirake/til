# Spring Boot Rate Limiting with Bucket4j

> _2026-07-23_ | Category: **spring-boot**

Protect APIs from abuse.

```java
// pom.xml: bucket4j-core

@Component
public class RateLimitInterceptor implements HandlerInterceptor {
    private final Map<String, Bucket> cache = new ConcurrentHashMap<>();
    
    private Bucket createBucket() {
        return Bucket.builder()
            .addLimit(Bandwidth.classic(100, Refill.greedy(100, Duration.ofMinutes(1))))
            .build();
    }
    
    @Override
    public boolean preHandle(HttpServletRequest req, HttpServletResponse res, Object handler) {
        String ip = req.getRemoteAddr();
        Bucket bucket = cache.computeIfAbsent(ip, k -> createBucket());
        
        if (bucket.tryConsume(1)) {
            long remaining = bucket.getAvailableTokens();
            res.setHeader("X-Rate-Limit-Remaining", String.valueOf(remaining));
            return true;
        }
        
        res.setStatus(429);
        res.setHeader("Retry-After", "60");
        return false;
    }
}
```

**Key Takeaway**: Rate limit by IP for public APIs, by API key for authenticated users. Use Redis for distributed rate limiting across multiple instances.

# Spring Boot Logging Best Practices

> _2026-11-24_ | Category: **spring-boot**

Structured logging with SLF4J and Logback.

```java
@Service
@Slf4j // Lombok
public class OrderService {
    public Order createOrder(CreateOrderRequest req) {
        log.info("Creating order for user={} items={}", req.getUserId(), req.getItems().size());
        try {
            Order order = processOrder(req);
            log.info("Order created orderId={} total={}", order.getId(), order.getTotal());
            return order;
        } catch (Exception e) {
            log.error("Failed to create order userId={}", req.getUserId(), e);
            throw e;
        }
    }
}
```

```yaml
# application.yml
logging:
  level:
    root: INFO
    com.myapp: DEBUG
    org.hibernate.SQL: DEBUG
  pattern:
    console: "%d{HH:mm:ss} [%thread] %-5level %logger{36} - %msg%n"
  file:
    name: logs/app.log
```

**Key Takeaway**: Use `{}` placeholders, not string concatenation (avoids building string when log level is off). Include context (userId, orderId) in every log.

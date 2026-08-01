# Spring Boot Actuator

> _2026-08-02_ | Category: **spring-boot**

Production monitoring endpoints.

```yaml
# application.yml
management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics,env
  endpoint:
    health:
      show-details: always
```

| Endpoint | Purpose |
|:---|:---|
| `/actuator/health` | App health + DB + disk |
| `/actuator/metrics` | JVM, HTTP, custom metrics |
| `/actuator/info` | App version, build info |
| `/actuator/env` | All config properties |

```java
// Custom health check
@Component
public class PaymentGatewayHealth implements HealthIndicator {
    public Health health() {
        boolean up = paymentGateway.ping();
        return up ? Health.up().withDetail("gateway","reachable").build()
                  : Health.down().withDetail("error","timeout").build();
    }
}
```

**Key Takeaway**: Secure actuator endpoints in production. Only expose `/health` publicly.

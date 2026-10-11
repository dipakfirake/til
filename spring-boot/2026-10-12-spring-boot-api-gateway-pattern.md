# Spring Boot API Gateway Pattern

> _2026-10-12_ | Category: **spring-boot**

Single entry point for microservices.

```yaml
# Spring Cloud Gateway
spring:
  cloud:
    gateway:
      routes:
        - id: user-service
          uri: lb://user-service
          predicates:
            - Path=/api/users/**
          filters:
            - StripPrefix=1
            - name: CircuitBreaker
              args: { name: userCB, fallbackUri: forward:/fallback }
        
        - id: order-service
          uri: lb://order-service
          predicates:
            - Path=/api/orders/**
          filters:
            - StripPrefix=1
            - name: RequestRateLimiter
              args:
                redis-rate-limiter:
                  replenishRate: 10
                  burstCapacity: 20
```

### Gateway Responsibilities
- **Routing**: /users → user-service, /orders → order-service
- **Auth**: Validate JWT before forwarding
- **Rate Limiting**: Protect backend services
- **Load Balancing**: Distribute across instances
- **Circuit Breaking**: Fallback on failures

**Key Takeaway**: API Gateway is the single entry point. Clients talk to gateway only, not individual services.

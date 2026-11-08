# Spring Boot Profiles

> _2026-11-09_ | Category: **spring-boot**

Environment-specific configuration.

```yaml
# application-dev.yml
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/app_dev
    username: root
  jpa:
    show-sql: true
    hibernate.ddl-auto: update

# application-prod.yml
spring:
  datasource:
    url: jdbc:mysql://prod-db:3306/app
    username: ${DB_USER}
    password: ${DB_PASS}
  jpa:
    show-sql: false
    hibernate.ddl-auto: validate
```

```bash
# Activate profile
java -jar app.jar --spring.profiles.active=prod
# Or environment variable
SPRING_PROFILES_ACTIVE=prod java -jar app.jar
```

**Key Takeaway**: Never hardcode credentials. Use profiles + environment variables for different environments.

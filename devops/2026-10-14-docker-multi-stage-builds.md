# Docker Multi-Stage Builds

> _2026-10-14_ | Category: **devops**

Reduce image size by separating build and runtime.

```dockerfile
# Stage 1: Build (800MB+)
FROM maven:3.9-eclipse-temurin-17 AS builder
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:resolve    # cache dependencies
COPY src ./src
RUN mvn clean package -DskipTests

# Stage 2: Run (200MB)
FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
COPY --from=builder /app/target/*.jar app.jar
EXPOSE 8080
HEALTHCHECK CMD curl -f http://localhost:8080/actuator/health || exit 1
ENTRYPOINT ["java", "-jar", "app.jar"]
```

**Benefits**: 75% smaller image, no build tools in production, faster deployments, smaller attack surface.

**Key Takeaway**: Always use multi-stage builds. Layer dependencies before source code (Docker cache optimization).

# Spring Boot Async Processing

> _2026-09-06_ | Category: **spring-boot**

Run tasks in background threads.

```java
@EnableAsync
@SpringBootApplication
public class App {}

@Service
public class NotificationService {
    @Async("taskExecutor")
    public CompletableFuture<Boolean> sendEmail(String to, String subject, String body) {
        // Runs in background thread — caller doesn't wait
        emailClient.send(to, subject, body);
        return CompletableFuture.completedFuture(true);
    }
}

@Configuration
public class AsyncConfig {
    @Bean("taskExecutor")
    public Executor taskExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setCorePoolSize(5);
        executor.setMaxPoolSize(10);
        executor.setQueueCapacity(25);
        executor.setThreadNamePrefix("async-");
        executor.setRejectedExecutionHandler(new ThreadPoolExecutor.CallerRunsPolicy());
        executor.initialize();
        return executor;
    }
}
```

**Key Takeaway**: `@Async` methods MUST be called from outside the class (proxy limitation). Always configure a custom thread pool — don't use default.

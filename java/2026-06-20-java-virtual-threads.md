# Java Virtual Threads

> _2026-06-20_ | Category: **java**

Lightweight threads for high-concurrency I/O (Java 21).

```java
// Platform thread: heavy, OS-managed
Thread.ofPlatform().start(() -> handleRequest());

// Virtual thread: ultra-lightweight, JVM-managed
Thread.ofVirtual().start(() -> handleRequest());

// Handle 100K concurrent requests
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    for (int i = 0; i < 100_000; i++) {
        executor.submit(() -> {
            var data = callExternalAPI();  // blocking I/O is fine!
            saveToDatabase(data);
            return data;
        });
    }
}
```

**Key Takeaway**: Virtual threads make blocking I/O efficient. Use for HTTP calls, DB queries. NOT for CPU-bound work.

# Java Memory Model and volatile

> _2026-08-08_ | Category: **java**

How threads see shared memory.

```java
// Without volatile: thread may cache stale value
private volatile boolean running = true;

// Thread A
new Thread(() -> {
    while (running) { doWork(); } // reads latest value
}).start();

// Thread B
running = false; // visible to Thread A immediately

// Happens-Before Rules:
// 1. volatile write → subsequent volatile read
// 2. synchronized unlock → subsequent lock
// 3. Thread.start() → first action in started thread
// 4. Thread action → Thread.join() return
```

**Key Takeaway**: `volatile` guarantees visibility across threads but NOT atomicity. Use `AtomicInteger` for atomic read-modify-write.

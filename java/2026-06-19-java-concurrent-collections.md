# Java Concurrent Collections

> _2026-06-19_ | Category: **java**

Thread-safe collections beyond ConcurrentHashMap.

```java
// CopyOnWriteArrayList — reads never block
CopyOnWriteArrayList<String> list = new CopyOnWriteArrayList<>();
// Great for: many reads, rare writes (event listeners)

// BlockingQueue — producer-consumer
BlockingQueue<Task> queue = new LinkedBlockingQueue<>(100);
queue.put(task);    // blocks if full
Task t = queue.take(); // blocks if empty

// ConcurrentLinkedQueue — non-blocking FIFO
ConcurrentLinkedQueue<Event> events = new ConcurrentLinkedQueue<>();
events.offer(event); // never blocks

// CountDownLatch — wait for N tasks
CountDownLatch latch = new CountDownLatch(3);
// Each task calls: latch.countDown();
latch.await(); // waits for all 3

// CyclicBarrier — N threads wait for each other
CyclicBarrier barrier = new CyclicBarrier(3, () -> System.out.println("All arrived!"));
// Each thread calls: barrier.await();
```

| Collection | Use Case |
|:---|:---|
| ConcurrentHashMap | Thread-safe map |
| CopyOnWriteArrayList | Read-heavy lists |
| BlockingQueue | Producer-consumer |
| ConcurrentSkipListMap | Sorted concurrent map |

# Java ConcurrentHashMap

> _2026-07-06_ | Category: **java**

Thread-safe map without locking entire table.

```java
ConcurrentHashMap<String, Integer> map = new ConcurrentHashMap<>();

// Atomic operations
map.put("counter", 0);
map.compute("counter", (k, v) -> v + 1);       // atomic increment
map.merge("counter", 1, Integer::sum);           // atomic merge
map.computeIfAbsent("cache", k -> expensiveOp()); // lazy compute
map.putIfAbsent("key", value);                   // only if missing

// Parallel bulk operations (Java 8+)
map.forEach(2, (k, v) -> System.out.println(k + "=" + v)); // parallelism threshold=2
long count = map.reduceValues(2, v -> v > 10 ? 1L : 0L, Long::sum);
```

| Feature | HashMap | ConcurrentHashMap |
|:---|:---|:---|
| Thread-safe | No | Yes |
| Null key/value | Allowed | NOT allowed |
| Locking | None | Bucket-level CAS |

**Key Takeaway**: Use ConcurrentHashMap in multi-threaded code. Never use `Collections.synchronizedMap()` — it's slower.

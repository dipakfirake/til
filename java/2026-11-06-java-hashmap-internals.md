# Java HashMap Internals

> _2026-11-06_ | Category: **java**

How HashMap works under the hood.

```java
Map<String, Integer> map = new HashMap<>();
// Default: capacity=16, loadFactor=0.75
// Rehash when size > 16 * 0.75 = 12

map.put("key", 1);
// 1. hashCode("key") = 106079
// 2. index = hash & (capacity-1) = bucket position
// 3. Store Entry(key, value, hash, next) in bucket
```

### Collision Resolution
- Java 7: LinkedList (O(n) worst case)
- Java 8+: LinkedList → **Red-Black Tree** when bucket size ≥ 8 (O(log n))

### Custom key class must override:
```java
@Override public int hashCode() { return Objects.hash(field1, field2); }
@Override public boolean equals(Object o) { /* compare fields */ }
```

**Key Takeaway**: Always override both `hashCode()` and `equals()` together when using custom objects as Map keys.

# Java Records

> _2026-07-01_ | Category: **java**

Immutable data carriers with zero boilerplate (Java 14+).

```java
// Before: 50+ lines
public class Point { private final int x, y; /* constructor, getters, equals, hashCode, toString */ }

// After: 1 line
public record Point(int x, int y) {}

Point p = new Point(3, 4);
p.x();        // 3 (accessor, not getX)
p.toString();  // Point[x=3, y=4]

// Custom validation
public record Email(String value) {
    public Email {  // compact constructor
        if (!value.contains("@")) throw new IllegalArgumentException("Invalid email");
        value = value.toLowerCase(); // normalize
    }
}

// With methods
public record Range(int min, int max) {
    public boolean contains(int n) { return n >= min && n <= max; }
}
```

**Key Takeaway**: Use records for DTOs, value objects, and API responses. They auto-generate equals, hashCode, toString.

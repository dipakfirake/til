# Java Control Flow - if-else and switch

> _2026-07-16_ | Category: **java**

Decision making with if-else chains and modern switch expressions.

```java
// Enhanced switch (Java 14+)
String day = "MONDAY";
String type = switch (day) {
    case "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY" -> "Weekday";
    case "SATURDAY", "SUNDAY" -> "Weekend";
    default -> "Unknown";
};

// Pattern matching switch (Java 21)
Object obj = 42;
String desc = switch (obj) {
    case Integer i when i > 0 -> "Positive: " + i;
    case String s -> "String: " + s;
    case null -> "Null";
    default -> "Other";
};
```

**Key Takeaway**: Modern switch expressions with `->` are cleaner than traditional `case:` with `break`.

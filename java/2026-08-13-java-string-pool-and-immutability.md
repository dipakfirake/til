# Java String Pool and Immutability

> _2026-08-13_ | Category: **java**

How String pooling saves memory.

```java
String s1 = "hello";            // String pool
String s2 = "hello";            // Same pool reference
String s3 = new String("hello"); // New heap object

System.out.println(s1 == s2);      // true (same reference)
System.out.println(s1 == s3);      // false (different objects)
System.out.println(s1.equals(s3)); // true (same content)

String s4 = s3.intern();          // Add to pool
System.out.println(s1 == s4);     // true
```

### Why Strings are Immutable
1. **Thread safety** — shared without synchronization
2. **Caching** — hashCode computed once
3. **Security** — can't modify DB URLs, passwords after creation
4. **String pool** — works only because strings never change

**Key Takeaway**: Always use `.equals()` for String comparison, never `==`.

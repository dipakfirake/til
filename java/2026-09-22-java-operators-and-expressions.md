# Java Operators and Expressions

> _2026-09-22_ | Category: **java**

Arithmetic, relational, logical, and bitwise operators.

```java
int a = 10, b = 3;
System.out.println(a / b);   // 3 (integer division)
System.out.println(a % b);   // 1 (modulo)
System.out.println(a == b);  // false
System.out.println(a > b && b > 0); // true (logical AND)

// Ternary operator
String result = (a > b) ? "a is bigger" : "b is bigger";

// Bitwise
int flags = 0b1010;
System.out.println(flags & 0b1100); // 0b1000 = 8
```

**Key Takeaway**: Use `==` for primitives, `.equals()` for objects. Integer division truncates decimals.

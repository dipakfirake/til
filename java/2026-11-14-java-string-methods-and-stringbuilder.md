# Java String Methods and StringBuilder

> _2026-11-14_ | Category: **java**

Strings are immutable. Use StringBuilder for modifications.

```java
String s = "Hello World";
s.length();            // 11
s.charAt(0);           // 'H'
s.substring(0, 5);     // "Hello"
s.toLowerCase();       // "hello world"
s.split(" ");          // ["Hello", "World"]
s.contains("World");   // true
s.replace("World","Java"); // "Hello Java"
s.trim();              // removes whitespace

// StringBuilder for concatenation in loops
StringBuilder sb = new StringBuilder();
for (int i = 0; i < 1000; i++) {
    sb.append(i).append(",");
}
String result = sb.toString();
```

**Key Takeaway**: Never concatenate strings in a loop with `+`. Use `StringBuilder` — it's 100x faster.

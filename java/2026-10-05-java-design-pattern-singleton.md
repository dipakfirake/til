# Java Design Pattern - Singleton

> _2026-10-05_ | Category: **java**

Ensure only one instance exists.

```java
// 1. Enum Singleton (BEST — thread-safe, serialization-safe)
public enum DatabasePool {
    INSTANCE;
    private final HikariDataSource ds;
    DatabasePool() { ds = new HikariDataSource(config()); }
    public Connection getConnection() throws SQLException { return ds.getConnection(); }
}

// 2. Double-Checked Locking
public class Singleton {
    private static volatile Singleton instance;
    private Singleton() {}
    public static Singleton getInstance() {
        if (instance == null) {
            synchronized (Singleton.class) {
                if (instance == null) instance = new Singleton();
            }
        }
        return instance;
    }
}

// 3. Holder Pattern (lazy, thread-safe)
public class Config {
    private Config() {}
    private static class Holder { static final Config INSTANCE = new Config(); }
    public static Config getInstance() { return Holder.INSTANCE; }
}
```

**Key Takeaway**: Use Enum singleton for new code. In Spring, all beans are singletons by default — don't create your own.

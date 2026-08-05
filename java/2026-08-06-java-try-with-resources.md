# Java Try-with-Resources

> _2026-08-06_ | Category: **java**

Auto-close resources to prevent memory leaks.

```java
// Auto-closes all resources in reverse order
try (Connection conn = dataSource.getConnection();
     PreparedStatement ps = conn.prepareStatement("SELECT * FROM users WHERE id = ?");
     ) {
    ps.setInt(1, userId);
    try (ResultSet rs = ps.executeQuery()) {
        while (rs.next()) {
            String name = rs.getString("name");
        }
    }
} // conn, ps, rs all auto-closed here

// Custom AutoCloseable
public class DatabasePool implements AutoCloseable {
    public Connection getConnection() { /* ... */ }
    
    @Override
    public void close() {
        // cleanup all connections
    }
}
```

**Key Takeaway**: Any class implementing `AutoCloseable` works with try-with-resources. Always use it for I/O, DB, and network resources.

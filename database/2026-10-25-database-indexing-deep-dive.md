# Database Indexing Deep Dive

> _2026-10-25_ | Category: **database**

Speed up queries with proper indexes.

```sql
-- Single column index
CREATE INDEX idx_email ON users(email);

-- Composite index (column order matters!)
CREATE INDEX idx_status_date ON orders(status, created_at);

-- Partial index (PostgreSQL)
CREATE INDEX idx_active ON users(email) WHERE is_active = true;

-- EXPLAIN to verify
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'test@mail.com';
-- Look for: Index Scan (good) vs Seq Scan (bad)
```

### Composite Index Leftmost Prefix Rule
```sql
-- Index on (A, B, C) supports:
-- WHERE A = ?              YES
-- WHERE A = ? AND B = ?    YES
-- WHERE A = ? AND B = ? AND C = ?  YES
-- WHERE B = ?              NO! (doesn't use index)
-- WHERE C = ?              NO!
```

**Key Takeaway**: Index columns you WHERE, JOIN, and ORDER BY most. Too many indexes slow down writes.

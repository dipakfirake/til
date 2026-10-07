# SQL Transactions and ACID

> _2026-10-08_ | Category: **database**

Ensure data integrity with transactions.

```sql
START TRANSACTION;

UPDATE accounts SET balance = balance - 500 WHERE id = 1;
UPDATE accounts SET balance = balance + 500 WHERE id = 2;

-- If both succeed
COMMIT;
-- If anything fails
ROLLBACK;
```

| Property | Meaning |
|:---|:---|
| Atomicity | All or nothing |
| Consistency | Valid state before and after |
| Isolation | Concurrent txns don't interfere |
| Durability | Committed data survives crashes |

| Isolation Level | Dirty Read | Non-Repeatable | Phantom |
|:---|:---|:---|:---|
| READ UNCOMMITTED | Yes | Yes | Yes |
| READ COMMITTED | No | Yes | Yes |
| REPEATABLE READ | No | No | Yes |
| SERIALIZABLE | No | No | No |

**Key Takeaway**: MySQL default is REPEATABLE READ. Use SERIALIZABLE only when absolutely needed — it's the slowest.

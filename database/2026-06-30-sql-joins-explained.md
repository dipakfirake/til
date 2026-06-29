# SQL JOINs Explained

> _2026-06-30_ | Category: **database**

Combine data from multiple tables.

```sql
-- INNER JOIN: only matching
SELECT u.name, o.total FROM users u
INNER JOIN orders o ON u.id = o.user_id;

-- LEFT JOIN: all users + their orders (NULL if none)
SELECT u.name, COUNT(o.id) as order_count
FROM users u LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.name;

-- Self JOIN: find employees and their managers
SELECT e.name AS employee, m.name AS manager
FROM employees e LEFT JOIN employees m ON e.manager_id = m.id;
```

**Key Takeaway**: Always index JOIN columns for performance. LEFT JOIN = all left rows; RIGHT JOIN = all right rows.

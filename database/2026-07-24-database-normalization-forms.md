# Database Normalization Forms

> _2026-07-24_ | Category: **database**

Reduce redundancy and improve data integrity.

| Normal Form | Rule | Example |
|:---|:---|:---|
| 1NF | No repeating groups, atomic values | `skills TEXT` → separate `user_skills` table |
| 2NF | No partial dependency on composite key | Every non-key depends on FULL primary key |
| 3NF | No transitive dependency | Remove `dept_name` if `dept_id` exists |
| BCNF | Every determinant is a candidate key | Stricter 3NF |

```sql
-- Unnormalized (bad)
CREATE TABLE orders (
    id INT, customer_name TEXT, customer_email TEXT,
    product1 TEXT, price1 DECIMAL, product2 TEXT, price2 DECIMAL
);

-- Normalized (good)
CREATE TABLE customers (id INT PRIMARY KEY, name TEXT, email TEXT UNIQUE);
CREATE TABLE orders (id INT PRIMARY KEY, customer_id INT REFERENCES customers(id), created_at TIMESTAMP);
CREATE TABLE order_items (id INT PRIMARY KEY, order_id INT REFERENCES orders(id),
    product TEXT, price DECIMAL, quantity INT);
```

**Key Takeaway**: 3NF is enough for most apps. Denormalize strategically (read-heavy dashboards) only after measuring performance.

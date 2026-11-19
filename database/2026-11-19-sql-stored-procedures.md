# SQL Stored Procedures

> _2026-11-19_ | Category: **database**

Encapsulate business logic in the database.

```sql
DELIMITER //
CREATE PROCEDURE TransferMoney(
    IN from_account INT,
    IN to_account INT,
    IN amount DECIMAL(10,2),
    OUT success BOOLEAN
)
BEGIN
    DECLARE from_balance DECIMAL(10,2);
    
    START TRANSACTION;
    
    SELECT balance INTO from_balance FROM accounts WHERE id = from_account FOR UPDATE;
    
    IF from_balance >= amount THEN
        UPDATE accounts SET balance = balance - amount WHERE id = from_account;
        UPDATE accounts SET balance = balance + amount WHERE id = to_account;
        INSERT INTO transactions (from_id, to_id, amount, created_at) 
            VALUES (from_account, to_account, amount, NOW());
        SET success = TRUE;
        COMMIT;
    ELSE
        SET success = FALSE;
        ROLLBACK;
    END IF;
END //
DELIMITER ;

-- Usage
CALL TransferMoney(1, 2, 500.00, @result);
SELECT @result;
```

**Key Takeaway**: Stored procedures reduce network roundtrips and ensure atomicity. But they're hard to version-control and test — prefer application-level logic for complex business rules.

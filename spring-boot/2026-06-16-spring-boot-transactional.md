# Spring Boot @Transactional

> _2026-06-16_ | Category: **spring-boot**

Manage database transactions declaratively.

```java
@Service
public class TransferService {
    @Transactional // rolls back on RuntimeException
    public void transfer(Long fromId, Long toId, double amount) {
        Account from = accountRepo.findById(fromId).orElseThrow();
        Account to = accountRepo.findById(toId).orElseThrow();
        
        from.setBalance(from.getBalance() - amount);
        to.setBalance(to.getBalance() + amount);
        
        accountRepo.save(from);
        accountRepo.save(to);
        // If any exception here, BOTH saves are rolled back
    }
    
    @Transactional(readOnly = true) // optimization for reads
    public List<Account> getAll() { return accountRepo.findAll(); }
    
    @Transactional(propagation = Propagation.REQUIRES_NEW)
    public void logAudit(String msg) {
        // Runs in separate transaction
        auditRepo.save(new AuditLog(msg));
    }
}
```

**Key Takeaway**: `@Transactional` on class = all methods transactional. It only works on PUBLIC methods called from OUTSIDE the class (proxy-based).

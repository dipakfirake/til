# Spring Events - Loose Coupling

> _2026-08-28_ | Category: **spring-boot**

Publish/subscribe within your application.

```java
// Event
public record OrderCreatedEvent(Long orderId, Long userId, BigDecimal total) {}

// Publisher
@Service
public class OrderService {
    @Autowired private ApplicationEventPublisher publisher;
    
    @Transactional
    public Order create(CreateOrderRequest req) {
        Order order = orderRepo.save(buildOrder(req));
        publisher.publishEvent(new OrderCreatedEvent(order.getId(), req.getUserId(), order.getTotal()));
        return order;
    }
}

// Listeners (decoupled!)
@Component
public class EmailListener {
    @EventListener
    public void onOrderCreated(OrderCreatedEvent event) {
        emailService.sendConfirmation(event.userId(), event.orderId());
    }
}

@Component
public class InventoryListener {
    @Async @EventListener  // runs in separate thread
    public void onOrderCreated(OrderCreatedEvent event) {
        inventoryService.reserve(event.orderId());
    }
}
```

**Key Takeaway**: Events decouple services without message brokers. Use `@Async` for non-critical listeners to avoid slowing down the main flow.

# Java Design Pattern - Observer

> _2026-11-26_ | Category: **java**

Notify multiple objects when state changes.

```java
public interface EventListener {
    void onEvent(String eventType, String data);
}

public class EventManager {
    private Map<String, List<EventListener>> listeners = new HashMap<>();

    public void subscribe(String event, EventListener listener) {
        listeners.computeIfAbsent(event, k -> new ArrayList<>()).add(listener);
    }

    public void notify(String event, String data) {
        listeners.getOrDefault(event, List.of())
                 .forEach(l -> l.onEvent(event, data));
    }
}

// Usage
EventManager events = new EventManager();
events.subscribe("order.created", (type, data) -> sendEmail(data));
events.subscribe("order.created", (type, data) -> updateInventory(data));
events.notify("order.created", "Order #123");
```

**Key Takeaway**: Observer decouples event producers from consumers. Spring's `@EventListener` uses this pattern.

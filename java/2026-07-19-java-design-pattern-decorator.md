# Java Design Pattern - Decorator

> _2026-07-19_ | Category: **java**

Add behavior dynamically without changing original class.

```java
public interface Coffee {
    double cost();
    String description();
}

public class BasicCoffee implements Coffee {
    public double cost() { return 50; }
    public String description() { return "Basic Coffee"; }
}

// Decorator
public abstract class CoffeeDecorator implements Coffee {
    protected final Coffee coffee;
    public CoffeeDecorator(Coffee c) { this.coffee = c; }
}

public class Milk extends CoffeeDecorator {
    public Milk(Coffee c) { super(c); }
    public double cost() { return coffee.cost() + 15; }
    public String description() { return coffee.description() + " + Milk"; }
}

public class Whip extends CoffeeDecorator {
    public Whip(Coffee c) { super(c); }
    public double cost() { return coffee.cost() + 25; }
    public String description() { return coffee.description() + " + Whip"; }
}

// Stack decorators
Coffee order = new Whip(new Milk(new BasicCoffee()));
System.out.println(order.description()); // Basic Coffee + Milk + Whip
System.out.println(order.cost());        // 90
```

**Key Takeaway**: Decorator = wrapper classes. Used in Java I/O streams (BufferedReader wraps FileReader).

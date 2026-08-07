# C# Delegates and Events

> _2026-08-07_ | Category: **dotnet**

Type-safe function pointers and event handling.

```csharp
// Delegate
public delegate bool Predicate<T>(T item);

// Built-in delegates
Func<int, int, int> add = (a, b) => a + b;     // returns value
Action<string> log = msg => Console.WriteLine(msg); // void
Predicate<int> isEven = n => n % 2 == 0;        // returns bool

// Events
public class StockTicker {
    public event EventHandler<StockChangedEventArgs>? PriceChanged;
    
    public void UpdatePrice(string symbol, decimal price) {
        PriceChanged?.Invoke(this, new StockChangedEventArgs(symbol, price));
    }
}

public record StockChangedEventArgs(string Symbol, decimal Price);

// Subscribe
var ticker = new StockTicker();
ticker.PriceChanged += (sender, args) => {
    Console.WriteLine($"{args.Symbol}: ₹{args.Price}");
};
ticker.UpdatePrice("INFY", 1500.50m);
```

**Key Takeaway**: Use `Func<>`, `Action<>`, `Predicate<>` instead of custom delegates. Events provide publisher-subscriber pattern with loose coupling.

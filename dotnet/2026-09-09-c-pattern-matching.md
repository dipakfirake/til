# C# Pattern Matching

> _2026-09-09_ | Category: **dotnet**

Modern type checking and data extraction.

```csharp
// Type pattern
string Describe(object obj) => obj switch {
    int i when i > 0 => $"Positive: {i}",
    int i            => $"Non-positive: {i}",
    string s         => $"String({s.Length})",
    null             => "null",
    _                => $"Unknown: {obj.GetType()}"
};

// Property pattern
string GetDiscount(Customer c) => c switch {
    { Tier: "Gold", Years: > 5 }  => "30% off",
    { Tier: "Gold" }              => "20% off",
    { Tier: "Silver" }            => "10% off",
    _                              => "No discount"
};

// Relational + logical
string Classify(int temp) => temp switch {
    < 0          => "Freezing",
    >= 0 and < 20 => "Cold",
    >= 20 and < 35 => "Warm",
    >= 35         => "Hot"
};
```

**Key Takeaway**: Pattern matching replaces complex if-else chains with readable, declarative code.

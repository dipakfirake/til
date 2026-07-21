# C# Extension Methods

> _2026-07-22_ | Category: **dotnet**

Add methods to existing types without modifying them.

```csharp
public static class StringExtensions {
    public static bool IsValidEmail(this string email) {
        return !string.IsNullOrEmpty(email) && email.Contains('@') && email.Contains('.');
    }
    
    public static string Truncate(this string value, int maxLength) {
        return value.Length <= maxLength ? value : value[..maxLength] + "...";
    }
    
    public static string ToSlug(this string title) {
        return Regex.Replace(title.ToLower(), @"[^a-z0-9]+", "-").Trim('-');
    }
}

// Usage — looks like built-in methods!
"user@example.com".IsValidEmail();  // true
"Hello World Long Title".Truncate(10); // "Hello Worl..."
"My Blog Post Title!".ToSlug(); // "my-blog-post-title"

// Collection extensions
public static class EnumerableExtensions {
    public static IEnumerable<T> WhereNotNull<T>(this IEnumerable<T?> source) {
        return source.Where(item => item != null)!;
    }
}
```

**Key Takeaway**: Extension methods must be `static` in a `static` class. Use `this` keyword on first parameter. LINQ is entirely built with extension methods.

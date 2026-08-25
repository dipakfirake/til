# Entity Framework Core Basics

> _2026-08-26_ | Category: **dotnet**

ORM for .NET database operations.

```csharp
// DbContext
public class AppDbContext : DbContext {
    public DbSet<Product> Products { get; set; }
    public DbSet<Order> Orders { get; set; }
    
    protected override void OnModelCreating(ModelBuilder mb) {
        mb.Entity<Product>().HasIndex(p => p.Name).IsUnique();
        mb.Entity<Order>().HasOne(o => o.Customer).WithMany(c => c.Orders);
    }
}

// CRUD operations
// Create
context.Products.Add(new Product { Name = "Laptop", Price = 999 });
await context.SaveChangesAsync();

// Read
var products = await context.Products
    .Where(p => p.Price > 500)
    .OrderBy(p => p.Name)
    .ToListAsync();

// Update
var product = await context.Products.FindAsync(1);
product.Price = 899;
await context.SaveChangesAsync();

// Delete
context.Products.Remove(product);
await context.SaveChangesAsync();
```

**Key Takeaway**: Use migrations (`dotnet ef migrations add ...`) to version-control schema changes. Never use `EnsureCreated()` in production.

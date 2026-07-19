# Python Generators and yield

> _2026-07-20_ | Category: **python**

Lazy evaluation for memory efficiency.

```python
# Returns entire list (uses memory)
def get_squares(n):
    return [i**2 for i in range(n)]

# Generator (yields one at a time, O(1) memory)
def generate_squares(n):
    for i in range(n):
        yield i**2

# Usage
for sq in generate_squares(1000000):
    print(sq) # Only one square in memory at a time!

# Generator expression (like list comprehension but with parentheses)
gen = (i**2 for i in range(1000000))
```

**Key Takeaway**: Use generators for large datasets, infinite sequences, or reading huge files.

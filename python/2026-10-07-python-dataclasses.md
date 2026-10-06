# Python Dataclasses

> _2026-10-07_ | Category: **python**

Classes without boilerplate.

```python
from dataclasses import dataclass, field

@dataclass
class User:
    id: int
    name: str
    email: str
    is_active: bool = True
    friends: list[str] = field(default_factory=list) # avoid mutable default args!

    def greeting(self) -> str:
        return f"Hi, I'm {self.name}"

u1 = User(1, "Dipak", "d@example.com")
u2 = User(1, "Dipak", "d@example.com")

print(u1 == u2) # True (auto-generates __eq__)
print(u1)       # User(id=1, name='Dipak', email='d@example.com', is_active=True, friends=[])
```

**Key Takeaway**: Use `@dataclass` for classes that primarily store data. It auto-generates `__init__`, `__repr__`, and `__eq__`.

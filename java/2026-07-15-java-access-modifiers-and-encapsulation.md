# Java Access Modifiers and Encapsulation

> _2026-07-15_ | Category: **java**

Four access levels control visibility.

```java
public class Employee {
    public String name;       // Accessible everywhere
    protected int age;        // Same package + subclasses
    int department;           // Same package only (default)
    private double salary;    // Same class only
    
    // Encapsulation: private field + public getter/setter
    public double getSalary() { return salary; }
    public void setSalary(double salary) {
        if (salary >= 0) this.salary = salary;
    }
}
```

| Modifier | Class | Package | Subclass | World |
|:---|:---|:---|:---|:---|
| private | Yes | No | No | No |
| default | Yes | Yes | No | No |
| protected | Yes | Yes | Yes | No |
| public | Yes | Yes | Yes | Yes |

**Key Takeaway**: Default to `private`. Only widen access when needed.

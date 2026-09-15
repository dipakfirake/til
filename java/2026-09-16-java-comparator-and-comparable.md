# Java Comparator and Comparable

> _2026-09-16_ | Category: **java**

Sort objects with natural ordering or custom logic.

```java
// Comparable: natural ordering inside the class
public class Employee implements Comparable<Employee> {
    String name; int salary;
    public int compareTo(Employee o) { return Integer.compare(this.salary, o.salary); }
}
Collections.sort(employees); // uses compareTo

// Comparator: custom ordering outside the class
employees.sort(Comparator.comparing(Employee::getSalary).reversed()
                          .thenComparing(Employee::getName));

// Null-safe
employees.sort(Comparator.comparing(Employee::getName,
    Comparator.nullsLast(Comparator.naturalOrder())));

// Multiple fields
Comparator<Employee> comp = Comparator
    .comparing(Employee::getDepartment)
    .thenComparing(Employee::getSalary, Comparator.reverseOrder())
    .thenComparing(Employee::getName);
```

**Key Takeaway**: Use Comparable for default ordering, Comparator for custom/multiple sort strategies.

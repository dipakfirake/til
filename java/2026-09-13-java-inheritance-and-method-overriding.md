# Java Inheritance and Method Overriding

> _2026-09-13_ | Category: **java**

Inheritance enables code reuse. Subclass extends superclass.

```java
public class Animal {
    protected String name;
    public Animal(String name) { this.name = name; }
    public String speak() { return "..."; }
}

public class Dog extends Animal {
    public Dog(String name) { super(name); }
    
    @Override
    public String speak() { return name + " says Woof!"; }
}

public class Cat extends Animal {
    public Cat(String name) { super(name); }
    
    @Override
    public String speak() { return name + " says Meow!"; }
}

// Polymorphism
Animal pet = new Dog("Rex");
System.out.println(pet.speak()); // Rex says Woof!
```

**Key Takeaway**: Use `@Override` annotation always — compiler catches errors if method signature doesn't match.

# 370+ Programming Topics: Basics → Advanced → Production
# Categories: java, spring-boot, dotnet, react, javascript, typescript,
#             html-css, nodejs, mongodb, database, dsa, system-design, git, devops

from topics_extra import EXTRA_TOPICS
from topics_extra2 import EXTRA_TOPICS_2
from topics_extra3 import EXTRA_TOPICS_3

_BASE_TOPICS = [

# ═══════════════════════════════════════════════════════════════
# JAVA CORE — 50 topics (Basics → Advanced)
# ═══════════════════════════════════════════════════════════════
("java","Java Variables and Data Types","""Java has 8 primitive types and reference types.

```java
int age = 25;           // 32-bit integer
double salary = 50000.0; // 64-bit floating point
boolean active = true;   // true or false
char grade = 'A';        // single character
String name = "Dipak";   // Reference type (object)
long bigNum = 100000L;   // 64-bit integer
float pi = 3.14f;        // 32-bit floating point
```

**Key Takeaway**: Primitives are stored on stack (fast), objects on heap. Always use `String` (capital S) — it's a class, not a primitive."""),

("java","Java Operators and Expressions","""Arithmetic, relational, logical, and bitwise operators.

```java
int a = 10, b = 3;
System.out.println(a / b);   // 3 (integer division)
System.out.println(a % b);   // 1 (modulo)
System.out.println(a == b);  // false
System.out.println(a > b && b > 0); // true (logical AND)

// Ternary operator
String result = (a > b) ? "a is bigger" : "b is bigger";

// Bitwise
int flags = 0b1010;
System.out.println(flags & 0b1100); // 0b1000 = 8
```

**Key Takeaway**: Use `==` for primitives, `.equals()` for objects. Integer division truncates decimals."""),

("java","Java Control Flow - if-else and switch","""Decision making with if-else chains and modern switch expressions.

```java
// Enhanced switch (Java 14+)
String day = "MONDAY";
String type = switch (day) {
    case "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY" -> "Weekday";
    case "SATURDAY", "SUNDAY" -> "Weekend";
    default -> "Unknown";
};

// Pattern matching switch (Java 21)
Object obj = 42;
String desc = switch (obj) {
    case Integer i when i > 0 -> "Positive: " + i;
    case String s -> "String: " + s;
    case null -> "Null";
    default -> "Other";
};
```

**Key Takeaway**: Modern switch expressions with `->` are cleaner than traditional `case:` with `break`."""),

("java","Java Arrays and Array Operations","""Fixed-size, indexed collections of same type.

```java
int[] nums = {5, 3, 8, 1, 9};
String[] names = new String[3];

// Sort
Arrays.sort(nums); // {1, 3, 5, 8, 9}

// Binary search (array must be sorted)
int idx = Arrays.binarySearch(nums, 5); // 2

// Copy
int[] copy = Arrays.copyOf(nums, nums.length);

// 2D Array
int[][] matrix = {{1,2,3}, {4,5,6}};
System.out.println(matrix[1][2]); // 6

// Convert to List
List<Integer> list = Arrays.stream(nums).boxed().collect(Collectors.toList());
```

**Key Takeaway**: Arrays are fixed-size. Use `ArrayList` when you need dynamic sizing."""),

("java","Java String Methods and StringBuilder","""Strings are immutable. Use StringBuilder for modifications.

```java
String s = "Hello World";
s.length();            // 11
s.charAt(0);           // 'H'
s.substring(0, 5);     // "Hello"
s.toLowerCase();       // "hello world"
s.split(" ");          // ["Hello", "World"]
s.contains("World");   // true
s.replace("World","Java"); // "Hello Java"
s.trim();              // removes whitespace

// StringBuilder for concatenation in loops
StringBuilder sb = new StringBuilder();
for (int i = 0; i < 1000; i++) {
    sb.append(i).append(",");
}
String result = sb.toString();
```

**Key Takeaway**: Never concatenate strings in a loop with `+`. Use `StringBuilder` — it's 100x faster."""),

("java","Java OOP - Classes and Objects","""Classes are blueprints, objects are instances.

```java
public class BankAccount {
    private String owner;
    private double balance;
    
    public BankAccount(String owner, double balance) {
        this.owner = owner;
        this.balance = balance;
    }
    
    public void deposit(double amount) {
        if (amount > 0) this.balance += amount;
    }
    
    public boolean withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            return true;
        }
        return false;
    }
    
    public double getBalance() { return balance; }
}
```

**Key Takeaway**: Encapsulate fields as `private`, expose through methods. This protects data integrity."""),

("java","Java Inheritance and Method Overriding","""Inheritance enables code reuse. Subclass extends superclass.

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

**Key Takeaway**: Use `@Override` annotation always — compiler catches errors if method signature doesn't match."""),

("java","Java Interfaces and Abstract Classes","""Interfaces define contracts. Abstract classes provide partial implementation.

```java
public interface Payable {
    double calculatePay();
    default String getCurrency() { return "INR"; } // default method
}

public abstract class Employee implements Payable {
    protected String name;
    protected double baseSalary;
    public Employee(String name, double salary) {
        this.name = name; this.baseSalary = salary;
    }
    abstract String getRole(); // subclass must implement
}

public class Developer extends Employee {
    public Developer(String n, double s) { super(n, s); }
    public double calculatePay() { return baseSalary * 1.2; }
    String getRole() { return "Developer"; }
}
```

| Feature | Interface | Abstract Class |
|:---|:---|:---|
| Multiple inheritance | Yes | No |
| Constructors | No | Yes |
| Fields | Only constants | Any |"""),

("java","Java Polymorphism - Compile vs Runtime","""Compile-time (overloading) vs Runtime (overriding) polymorphism.

```java
public class Calculator {
    // Method Overloading (compile-time)
    public int add(int a, int b) { return a + b; }
    public double add(double a, double b) { return a + b; }
    public int add(int a, int b, int c) { return a + b + c; }
}

// Method Overriding (runtime)
public class Shape {
    public double area() { return 0; }
}
public class Circle extends Shape {
    double r;
    public Circle(double r) { this.r = r; }
    @Override
    public double area() { return Math.PI * r * r; }
}

// Runtime polymorphism in action
Shape s = new Circle(5);
System.out.println(s.area()); // 78.54 (Circle's area, not Shape's)
```

**Key Takeaway**: Overloading = same name, different params. Overriding = same signature, different class."""),

("java","Java Access Modifiers and Encapsulation","""Four access levels control visibility.

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

**Key Takeaway**: Default to `private`. Only widen access when needed."""),

("java","Java Collections Framework Overview","""Core interfaces: List, Set, Map, Queue.

```java
// List — ordered, allows duplicates
List<String> list = new ArrayList<>(List.of("a","b","c"));
list.add("d");
list.get(0); // "a"

// Set — no duplicates
Set<Integer> set = new HashSet<>(Set.of(1,2,3,2)); // {1,2,3}

// Map — key-value pairs
Map<String,Integer> map = new HashMap<>();
map.put("Java", 1);
map.getOrDefault("Python", 0); // 0

// Queue — FIFO
Queue<String> queue = new LinkedList<>();
queue.offer("first");
queue.poll(); // "first"

// Iterate any collection
list.forEach(System.out::println);
map.forEach((k,v) -> System.out.println(k + "=" + v));
```

**Key Takeaway**: Use `ArrayList` for random access, `LinkedList` for frequent inserts, `HashSet` for uniqueness."""),

("java","Java Generics - Type Safety","""Generics enable type-safe collections and methods.

```java
// Generic class
public class Box<T> {
    private T value;
    public Box(T value) { this.value = value; }
    public T getValue() { return value; }
}

Box<String> strBox = new Box<>("Hello");
Box<Integer> intBox = new Box<>(42);

// Generic method
public static <T extends Comparable<T>> T max(T a, T b) {
    return a.compareTo(b) > 0 ? a : b;
}

// Bounded wildcards
public double sum(List<? extends Number> nums) {
    return nums.stream().mapToDouble(Number::doubleValue).sum();
}
```

**PECS Rule**: Producer Extends, Consumer Super.
- Read from: `<? extends T>` — Producer
- Write to: `<? super T>` — Consumer"""),

("java","Java Exception Handling","""Checked exceptions must be handled; unchecked are optional.

```java
// Custom exception
public class InsufficientFundsException extends Exception {
    private double amount;
    public InsufficientFundsException(double amount) {
        super("Insufficient funds: need " + amount);
        this.amount = amount;
    }
}

// Usage with try-catch-finally
public void withdraw(double amount) throws InsufficientFundsException {
    if (amount > balance)
        throw new InsufficientFundsException(amount - balance);
    balance -= amount;
}

try {
    account.withdraw(1000);
} catch (InsufficientFundsException e) {
    log.error(e.getMessage());
} finally {
    // Always executes
}
```

**Key Takeaway**: Use checked exceptions for recoverable errors, unchecked (RuntimeException) for programming bugs."""),

("java","Java Lambda Expressions","""Lambdas enable functional programming in Java 8+.

```java
// Before: anonymous inner class
Runnable old = new Runnable() {
    public void run() { System.out.println("Hello"); }
};

// After: lambda
Runnable modern = () -> System.out.println("Hello");

// With parameters
Comparator<String> byLength = (a, b) -> a.length() - b.length();
List<String> names = List.of("Charlie","Bob","Alice");
names.stream().sorted(byLength).forEach(System.out::println);

// Method reference
names.forEach(System.out::println); // same as n -> System.out.println(n)

// Predicate
Predicate<Integer> isEven = n -> n % 2 == 0;
List<Integer> evens = List.of(1,2,3,4,5).stream().filter(isEven).toList();
```

**Key Takeaway**: Lambdas replace single-method interfaces. Use method references (`::`) when possible for clarity."""),

("java","Java Streams API","""Streams process collections declaratively.

```java
List<Employee> employees = getEmployees();

// Filter, map, collect
List<String> seniorDevNames = employees.stream()
    .filter(e -> e.getSalary() > 80000)
    .filter(e -> e.getDept().equals("Engineering"))
    .map(Employee::getName)
    .sorted()
    .collect(Collectors.toList());

// Reduce
int totalSalary = employees.stream()
    .mapToInt(Employee::getSalary)
    .sum();

// Grouping
Map<String, List<Employee>> byDept = employees.stream()
    .collect(Collectors.groupingBy(Employee::getDept));

// Parallel processing
long count = employees.parallelStream()
    .filter(e -> e.getAge() > 30)
    .count();
```

**Key Takeaway**: Streams are lazy — intermediate operations don't execute until a terminal operation (collect, forEach, reduce) is called."""),

("java","Java Optional","""Avoid NullPointerException with Optional.

```java
Optional<User> user = userRepository.findById(id);

// Chain operations safely
String city = user
    .map(User::getAddress)
    .map(Address::getCity)
    .orElse("Unknown");

// Throw if empty
User u = user.orElseThrow(() -> new NotFoundException("User " + id));

// Conditional action
user.ifPresent(u -> sendEmail(u.getEmail()));

// Filter
Optional<User> admin = user.filter(u -> u.getRole().equals("ADMIN"));

// Create
Optional<String> empty = Optional.empty();
Optional<String> present = Optional.of("Hello");
Optional<String> nullable = Optional.ofNullable(mayBeNull);
```

**Key Takeaway**: Use Optional as return type only, never as method parameter or field."""),

("java","Java Functional Interfaces","""An interface with exactly one abstract method.

```java
@FunctionalInterface
public interface Transformer<T, R> {
    R transform(T input);
}

// Built-in functional interfaces
Predicate<String> notEmpty = s -> !s.isEmpty();
Function<String, Integer> toLength = String::length;
Consumer<String> printer = System.out::println;
Supplier<UUID> idGenerator = UUID::randomUUID;
BiFunction<Integer,Integer,Integer> add = Integer::sum;
UnaryOperator<String> upper = String::toUpperCase;

// Chaining
Function<String, String> pipeline = 
    ((Function<String,String>) String::trim)
    .andThen(String::toLowerCase)
    .andThen(s -> s.replaceAll("\\s+", "-"));

String slug = pipeline.apply("  Hello World  "); // "hello-world"
```

**Key Takeaway**: Use built-in functional interfaces from `java.util.function` instead of creating custom ones."""),

("java","Java Enum with Methods","""Enums can have fields, constructors, and methods.

```java
public enum Planet {
    MERCURY(3.303e+23, 2.4397e6),
    VENUS(4.869e+24, 6.0518e6),
    EARTH(5.976e+24, 6.37814e6);

    private final double mass;
    private final double radius;

    Planet(double mass, double radius) {
        this.mass = mass;
        this.radius = radius;
    }

    double surfaceGravity() {
        return 6.67300E-11 * mass / (radius * radius);
    }

    double surfaceWeight(double otherMass) {
        return otherMass * surfaceGravity();
    }
}

// Usage
double weight = Planet.EARTH.surfaceWeight(75); // weight on Earth
```

**Key Takeaway**: Enums are more than constants — they can encapsulate logic. Use them instead of integer constants."""),

("java","Java Try-with-Resources","""Auto-close resources to prevent memory leaks.

```java
// Auto-closes all resources in reverse order
try (Connection conn = dataSource.getConnection();
     PreparedStatement ps = conn.prepareStatement("SELECT * FROM users WHERE id = ?");
     ) {
    ps.setInt(1, userId);
    try (ResultSet rs = ps.executeQuery()) {
        while (rs.next()) {
            String name = rs.getString("name");
        }
    }
} // conn, ps, rs all auto-closed here

// Custom AutoCloseable
public class DatabasePool implements AutoCloseable {
    public Connection getConnection() { /* ... */ }
    
    @Override
    public void close() {
        // cleanup all connections
    }
}
```

**Key Takeaway**: Any class implementing `AutoCloseable` works with try-with-resources. Always use it for I/O, DB, and network resources."""),

("java","Java Multithreading Basics","""Create threads with Thread class or Runnable interface.

```java
// Using Runnable (preferred)
Runnable task = () -> {
    System.out.println("Running in: " + Thread.currentThread().getName());
};
Thread t = new Thread(task, "worker-1");
t.start();

// Synchronized method
public class Counter {
    private int count = 0;
    public synchronized void increment() { count++; }
    public synchronized int getCount() { return count; }
}

// Thread communication
Object lock = new Object();
synchronized(lock) {
    while (!condition) lock.wait();  // release lock and wait
    // do work
    lock.notifyAll();  // wake waiting threads
}
```

**Key Takeaway**: Never call `run()` directly — call `start()`. Use `synchronized` or `java.util.concurrent` for thread safety."""),

("java","Java ExecutorService and Thread Pools","""Manage thread lifecycles with ExecutorService.

```java
// Fixed thread pool
ExecutorService executor = Executors.newFixedThreadPool(4);

// Submit tasks
Future<String> future = executor.submit(() -> {
    Thread.sleep(1000);
    return "Result from thread: " + Thread.currentThread().getName();
});

// Get result (blocks until complete)
String result = future.get(5, TimeUnit.SECONDS);

// Submit multiple tasks
List<Callable<Integer>> tasks = List.of(
    () -> compute(1), () -> compute(2), () -> compute(3)
);
List<Future<Integer>> results = executor.invokeAll(tasks);

// Always shutdown
executor.shutdown();
executor.awaitTermination(10, TimeUnit.SECONDS);
```

**Key Takeaway**: Never create threads manually in production. Use ExecutorService with bounded thread pools."""),

("java","Java CompletableFuture","""Async programming without blocking.

```java
CompletableFuture<User> userFuture = CompletableFuture
    .supplyAsync(() -> userService.findById(id))
    .thenApply(user -> { user.setLastLogin(now()); return user; })
    .exceptionally(ex -> { log.error("Failed", ex); return null; });

// Combine two independent async calls
CompletableFuture<String> nameFuture = CompletableFuture.supplyAsync(() -> getName(id));
CompletableFuture<Integer> ageFuture = CompletableFuture.supplyAsync(() -> getAge(id));

CompletableFuture<String> combined = nameFuture
    .thenCombine(ageFuture, (name, age) -> name + " is " + age);

// Wait for all
CompletableFuture.allOf(future1, future2, future3).join();
```

**Key Takeaway**: Use `thenApply` for sync transform, `thenCompose` for async chaining, `thenCombine` for parallel merge."""),

("java","Java Records","""Immutable data carriers with zero boilerplate (Java 14+).

```java
// Before: 50+ lines
public class Point { private final int x, y; /* constructor, getters, equals, hashCode, toString */ }

// After: 1 line
public record Point(int x, int y) {}

Point p = new Point(3, 4);
p.x();        // 3 (accessor, not getX)
p.toString();  // Point[x=3, y=4]

// Custom validation
public record Email(String value) {
    public Email {  // compact constructor
        if (!value.contains("@")) throw new IllegalArgumentException("Invalid email");
        value = value.toLowerCase(); // normalize
    }
}

// With methods
public record Range(int min, int max) {
    public boolean contains(int n) { return n >= min && n <= max; }
}
```

**Key Takeaway**: Use records for DTOs, value objects, and API responses. They auto-generate equals, hashCode, toString."""),

("java","Java Sealed Classes","""Restrict which classes can extend (Java 17).

```java
public sealed class Shape permits Circle, Rectangle, Triangle {}
public final class Circle extends Shape { double radius; }
public final class Rectangle extends Shape { double w, h; }
public non-sealed class Triangle extends Shape { double base, height; }

// Exhaustive pattern matching (Java 21)
double area(Shape s) {
    return switch (s) {
        case Circle c    -> Math.PI * c.radius * c.radius;
        case Rectangle r -> r.w * r.h;
        case Triangle t  -> 0.5 * t.base * t.height;
        // No default needed! Compiler knows all subtypes
    };
}
```

**Key Takeaway**: Sealed classes + pattern matching = type-safe algebraic data types in Java."""),

("java","Java Virtual Threads","""Lightweight threads for high-concurrency I/O (Java 21).

```java
// Platform thread: heavy, OS-managed
Thread.ofPlatform().start(() -> handleRequest());

// Virtual thread: ultra-lightweight, JVM-managed
Thread.ofVirtual().start(() -> handleRequest());

// Handle 100K concurrent requests
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    for (int i = 0; i < 100_000; i++) {
        executor.submit(() -> {
            var data = callExternalAPI();  // blocking I/O is fine!
            saveToDatabase(data);
            return data;
        });
    }
}
```

**Key Takeaway**: Virtual threads make blocking I/O efficient. Use for HTTP calls, DB queries. NOT for CPU-bound work."""),

("java","Java HashMap Internals","""How HashMap works under the hood.

```java
Map<String, Integer> map = new HashMap<>();
// Default: capacity=16, loadFactor=0.75
// Rehash when size > 16 * 0.75 = 12

map.put("key", 1);
// 1. hashCode("key") = 106079
// 2. index = hash & (capacity-1) = bucket position
// 3. Store Entry(key, value, hash, next) in bucket
```

### Collision Resolution
- Java 7: LinkedList (O(n) worst case)
- Java 8+: LinkedList → **Red-Black Tree** when bucket size ≥ 8 (O(log n))

### Custom key class must override:
```java
@Override public int hashCode() { return Objects.hash(field1, field2); }
@Override public boolean equals(Object o) { /* compare fields */ }
```

**Key Takeaway**: Always override both `hashCode()` and `equals()` together when using custom objects as Map keys."""),

("java","Java ConcurrentHashMap","""Thread-safe map without locking entire table.

```java
ConcurrentHashMap<String, Integer> map = new ConcurrentHashMap<>();

// Atomic operations
map.put("counter", 0);
map.compute("counter", (k, v) -> v + 1);       // atomic increment
map.merge("counter", 1, Integer::sum);           // atomic merge
map.computeIfAbsent("cache", k -> expensiveOp()); // lazy compute
map.putIfAbsent("key", value);                   // only if missing

// Parallel bulk operations (Java 8+)
map.forEach(2, (k, v) -> System.out.println(k + "=" + v)); // parallelism threshold=2
long count = map.reduceValues(2, v -> v > 10 ? 1L : 0L, Long::sum);
```

| Feature | HashMap | ConcurrentHashMap |
|:---|:---|:---|
| Thread-safe | No | Yes |
| Null key/value | Allowed | NOT allowed |
| Locking | None | Bucket-level CAS |

**Key Takeaway**: Use ConcurrentHashMap in multi-threaded code. Never use `Collections.synchronizedMap()` — it's slower."""),

("java","Java Garbage Collection","""JVM memory management and GC algorithms.

```
Heap Layout:
┌──────────────────────────┐
│ Young Gen (Eden + S0,S1) │ ← new objects, Minor GC
├──────────────────────────┤
│ Old Generation           │ ← long-lived objects, Major GC
├──────────────────────────┤
│ Metaspace                │ ← class metadata
└──────────────────────────┘
```

| GC | Best For | Pause |
|:---|:---|:---|
| G1 (default) | General purpose | Medium |
| ZGC | Low latency | <10ms |
| Shenandoah | Low latency | <10ms |
| Parallel | Max throughput | High |

```bash
# JVM GC flags
java -XX:+UseG1GC -Xms512m -Xmx2g -jar app.jar
java -XX:+UseZGC -jar app.jar  # Ultra-low latency
```

**Key Takeaway**: Don't call `System.gc()`. Trust the JVM. Tune only after profiling with VisualVM or JFR."""),

("java","Java Reflection API","""Inspect and modify classes at runtime.

```java
Class<?> clazz = Class.forName("com.app.User");

// Get all methods
Method[] methods = clazz.getDeclaredMethods();
for (Method m : methods) {
    System.out.println(m.getName() + " - " + m.getReturnType());
}

// Invoke private method
Method privateMethod = clazz.getDeclaredMethod("secretMethod", String.class);
privateMethod.setAccessible(true);
Object result = privateMethod.invoke(instance, "arg");

// Create instance dynamically
Constructor<?> ctor = clazz.getConstructor(String.class, int.class);
Object user = ctor.newInstance("Dipak", 24);

// Read private field
Field field = clazz.getDeclaredField("salary");
field.setAccessible(true);
double salary = (double) field.get(user);
```

**Key Takeaway**: Reflection is powerful but slow. Used by frameworks (Spring, Hibernate). Avoid in application code."""),

("java","Java Design Pattern - Builder","""Construct complex objects step by step.

```java
public class HttpRequest {
    private final String url;
    private final String method;
    private final Map<String,String> headers;
    private final String body;

    private HttpRequest(Builder b) {
        this.url=b.url; this.method=b.method;
        this.headers=b.headers; this.body=b.body;
    }

    public static class Builder {
        private final String url;
        private String method = "GET";
        private Map<String,String> headers = new HashMap<>();
        private String body;

        public Builder(String url) { this.url = url; }
        public Builder method(String m) { method=m; return this; }
        public Builder header(String k, String v) { headers.put(k,v); return this; }
        public Builder body(String b) { body=b; return this; }
        public HttpRequest build() { return new HttpRequest(this); }
    }
}

HttpRequest req = new HttpRequest.Builder("https://api.example.com")
    .method("POST")
    .header("Content-Type", "application/json")
    .body("{\"name\":\"Dipak\"}")
    .build();
```"""),

("java","Java Design Pattern - Factory Method","""Create objects without specifying exact class.

```java
public interface Notification {
    void send(String message);
}

public class EmailNotification implements Notification {
    public void send(String msg) { System.out.println("Email: " + msg); }
}
public class SMSNotification implements Notification {
    public void send(String msg) { System.out.println("SMS: " + msg); }
}
public class PushNotification implements Notification {
    public void send(String msg) { System.out.println("Push: " + msg); }
}

// Factory
public class NotificationFactory {
    public static Notification create(String type) {
        return switch (type.toUpperCase()) {
            case "EMAIL" -> new EmailNotification();
            case "SMS"   -> new SMSNotification();
            case "PUSH"  -> new PushNotification();
            default -> throw new IllegalArgumentException("Unknown: " + type);
        };
    }
}

Notification n = NotificationFactory.create("EMAIL");
n.send("Hello!");
```

**Key Takeaway**: Factory pattern decouples object creation from usage. Great for plugins and extensibility."""),

("java","Java Design Pattern - Observer","""Notify multiple objects when state changes.

```java
public interface EventListener {
    void onEvent(String eventType, String data);
}

public class EventManager {
    private Map<String, List<EventListener>> listeners = new HashMap<>();

    public void subscribe(String event, EventListener listener) {
        listeners.computeIfAbsent(event, k -> new ArrayList<>()).add(listener);
    }

    public void notify(String event, String data) {
        listeners.getOrDefault(event, List.of())
                 .forEach(l -> l.onEvent(event, data));
    }
}

// Usage
EventManager events = new EventManager();
events.subscribe("order.created", (type, data) -> sendEmail(data));
events.subscribe("order.created", (type, data) -> updateInventory(data));
events.notify("order.created", "Order #123");
```

**Key Takeaway**: Observer decouples event producers from consumers. Spring's `@EventListener` uses this pattern."""),

("java","Java Design Pattern - Strategy","""Swap algorithms at runtime.

```java
@FunctionalInterface
public interface SortStrategy {
    void sort(int[] array);
}

public class Sorter {
    private SortStrategy strategy;
    
    public Sorter(SortStrategy strategy) { this.strategy = strategy; }
    public void setStrategy(SortStrategy s) { this.strategy = s; }
    public void sort(int[] arr) { strategy.sort(arr); }
}

// Usage — swap strategies at runtime
Sorter sorter = new Sorter(Arrays::sort);          // default
sorter.sort(data);

sorter.setStrategy(arr -> { /* custom quicksort */ }); // swap
sorter.sort(data);

// Real-world: payment processing
PaymentProcessor processor = new PaymentProcessor(new CreditCardPayment());
processor.setStrategy(new UPIPayment()); // switch to UPI
processor.pay(500);
```

**Key Takeaway**: Strategy replaces if-else chains with polymorphism. Functions/lambdas make it even simpler in Java 8+."""),

("java","Java Serialization and Deserialization","""Convert objects to bytes and back.

```java
// Serializable
public class User implements Serializable {
    private static final long serialVersionUID = 1L;
    private String name;
    private transient String password; // excluded from serialization
}

// Serialize
try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("user.dat"))) {
    oos.writeObject(user);
}

// Deserialize
try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream("user.dat"))) {
    User user = (User) ois.readObject();
}
```

### Modern Alternative: JSON
```java
// Jackson
ObjectMapper mapper = new ObjectMapper();
String json = mapper.writeValueAsString(user);
User user = mapper.readValue(json, User.class);
```

**Key Takeaway**: Avoid Java serialization in production — use JSON (Jackson/Gson) instead. It's safer, readable, and cross-platform."""),

("java","Java Annotations - Custom Annotations","""Create and process custom annotations.

```java
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface Cacheable {
    int ttlSeconds() default 300;
    String key() default "";
}

// Usage
public class UserService {
    @Cacheable(ttlSeconds = 600, key = "user")
    public User findById(Long id) { return repo.findById(id); }
}

// Process at runtime with reflection
for (Method m : UserService.class.getDeclaredMethods()) {
    if (m.isAnnotationPresent(Cacheable.class)) {
        Cacheable c = m.getAnnotation(Cacheable.class);
        System.out.println(m.getName() + " cached for " + c.ttlSeconds() + "s");
    }
}
```

**Key Takeaway**: Frameworks like Spring use annotations heavily. Understanding custom annotations helps debug and extend frameworks."""),

("java","Java Pattern Matching","""Modern type checks with automatic casting (Java 16+).

```java
// Old way
if (obj instanceof String) {
    String s = (String) obj;
    System.out.println(s.length());
}

// New way — automatic binding
if (obj instanceof String s) {
    System.out.println(s.length()); // s already cast!
}

// Guarded patterns
if (obj instanceof String s && s.length() > 5) {
    System.out.println("Long string: " + s);
}

// Switch with patterns (Java 21)
String format(Object obj) {
    return switch (obj) {
        case Integer i    -> "int: %d".formatted(i);
        case Double d     -> "double: %.2f".formatted(d);
        case String s     -> "string: %s".formatted(s);
        case int[] arr    -> "array[%d]".formatted(arr.length);
        case null         -> "null";
        default           -> obj.toString();
    };
}
```"""),

("java","Java File I/O with NIO","""Modern file operations with java.nio.

```java
Path path = Path.of("data", "users.txt");

// Read entire file
String content = Files.readString(path);
List<String> lines = Files.readAllLines(path);

// Write
Files.writeString(path, "Hello World", StandardOpenOption.CREATE);
Files.write(path, List.of("line1","line2"), StandardOpenOption.APPEND);

// Stream large files (memory efficient)
try (Stream<String> stream = Files.lines(path)) {
    stream.filter(line -> line.contains("error"))
          .forEach(System.out::println);
}

// Walk directory tree
try (Stream<Path> walk = Files.walk(Path.of("src"))) {
    walk.filter(p -> p.toString().endsWith(".java"))
        .forEach(System.out::println);
}

// Copy, move, delete
Files.copy(source, target, StandardCopyOption.REPLACE_EXISTING);
Files.move(source, target);
Files.deleteIfExists(path);
```"""),

("java","Java Comparator and Comparable","""Sort objects with natural ordering or custom logic.

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

**Key Takeaway**: Use Comparable for default ordering, Comparator for custom/multiple sort strategies."""),

("java","Java String Pool and Immutability","""How String pooling saves memory.

```java
String s1 = "hello";            // String pool
String s2 = "hello";            // Same pool reference
String s3 = new String("hello"); // New heap object

System.out.println(s1 == s2);      // true (same reference)
System.out.println(s1 == s3);      // false (different objects)
System.out.println(s1.equals(s3)); // true (same content)

String s4 = s3.intern();          // Add to pool
System.out.println(s1 == s4);     // true
```

### Why Strings are Immutable
1. **Thread safety** — shared without synchronization
2. **Caching** — hashCode computed once
3. **Security** — can't modify DB URLs, passwords after creation
4. **String pool** — works only because strings never change

**Key Takeaway**: Always use `.equals()` for String comparison, never `==`."""),

("java","Java Iterator and Iterable","""Traverse collections with Iterator pattern.

```java
// Implement Iterable for custom collection
public class NumberRange implements Iterable<Integer> {
    private final int start, end;
    public NumberRange(int start, int end) { this.start=start; this.end=end; }
    
    @Override
    public Iterator<Integer> iterator() {
        return new Iterator<>() {
            int current = start;
            public boolean hasNext() { return current <= end; }
            public Integer next() { return current++; }
        };
    }
}

// Now works with for-each loop!
for (int n : new NumberRange(1, 5)) {
    System.out.println(n); // 1, 2, 3, 4, 5
}

// Also works with streams
StreamSupport.stream(new NumberRange(1,100).spliterator(), false)
    .filter(n -> n % 2 == 0)
    .forEach(System.out::println);
```

**Key Takeaway**: Implementing `Iterable` makes your class work with for-each loops and Stream API."""),

("java","Java Inner Classes and Anonymous Classes","""Four types of nested classes in Java.

```java
public class Outer {
    private int x = 10;
    
    // 1. Non-static inner class — access outer members
    class Inner {
        void show() { System.out.println(x); } // can access x
    }
    
    // 2. Static nested class — no access to outer instance
    static class StaticNested {
        void show() { System.out.println("Static nested"); }
    }
    
    void method() {
        // 3. Local class — inside a method
        class Local { void show() { System.out.println(x); } }
        
        // 4. Anonymous class — inline implementation
        Runnable r = new Runnable() {
            public void run() { System.out.println("Anonymous"); }
        };
        // Modern: just use lambda
        Runnable r2 = () -> System.out.println("Lambda");
    }
}
```

**Key Takeaway**: Prefer static nested classes over inner classes (no implicit reference to outer). Prefer lambdas over anonymous classes."""),

# ═══════════════════════════════════════════════════════════════
# SPRING BOOT — 40 topics
# ═══════════════════════════════════════════════════════════════
("spring-boot","Spring IoC Container and Beans","""Spring manages object creation and wiring through Inversion of Control.

```java
@Component          // Generic bean
@Service            // Business logic
@Repository         // Data access
@Controller         // Web controller
@Configuration      // Config class

// Bean lifecycle
@Component
public class AppStartup implements CommandLineRunner {
    @Override
    public void run(String... args) {
        System.out.println("App started!");
    }
}

@Bean
public RestTemplate restTemplate() {
    return new RestTemplate();
}
```

**Key Takeaway**: Spring creates and manages beans. You declare dependencies, Spring wires them. This is IoC — framework calls you, not the other way."""),

("spring-boot","Spring Dependency Injection Types","""Three ways to inject dependencies in Spring.

```java
// 1. Constructor injection (RECOMMENDED)
@Service
public class OrderService {
    private final UserRepository userRepo;
    private final PaymentService paymentService;
    
    public OrderService(UserRepository repo, PaymentService payment) {
        this.userRepo = repo;
        this.paymentService = payment;
    }
}

// 2. Setter injection
@Autowired
public void setMailService(MailService ms) { this.mailService = ms; }

// 3. Field injection (avoid)
@Autowired
private UserRepository userRepo; // hard to test!
```

| Type | Testable | Immutable | Recommended |
|:---|:---|:---|:---|
| Constructor | Yes | Yes | Yes |
| Setter | Yes | No | Sometimes |
| Field | No | No | Never |

**Key Takeaway**: Always use constructor injection — it makes dependencies explicit and enables easy unit testing."""),

("spring-boot","Spring Boot REST Controllers","""Build REST APIs with @RestController.

```java
@RestController
@RequestMapping("/api/v1/users")
public class UserController {
    private final UserService userService;
    
    public UserController(UserService service) { this.userService = service; }
    
    @GetMapping
    public List<User> getAll() { return userService.findAll(); }
    
    @GetMapping("/{id}")
    public User getById(@PathVariable Long id) { return userService.findById(id); }
    
    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public User create(@Valid @RequestBody CreateUserDTO dto) {
        return userService.create(dto);
    }
    
    @PutMapping("/{id}")
    public User update(@PathVariable Long id, @Valid @RequestBody UpdateUserDTO dto) {
        return userService.update(id, dto);
    }
    
    @DeleteMapping("/{id}")
    @ResponseStatus(HttpStatus.NO_CONTENT)
    public void delete(@PathVariable Long id) { userService.delete(id); }
}
```"""),

("spring-boot","Spring Data JPA - Repositories","""CRUD without writing SQL.

```java
@Entity
@Table(name = "products")
public class Product {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private double price;
    private String category;
}

public interface ProductRepository extends JpaRepository<Product, Long> {
    // Spring generates SQL automatically from method name!
    List<Product> findByCategory(String category);
    List<Product> findByPriceBetween(double min, double max);
    List<Product> findByNameContainingIgnoreCase(String keyword);
    Optional<Product> findByNameAndCategory(String name, String cat);
    
    @Query("SELECT p FROM Product p WHERE p.price > :min ORDER BY p.price DESC")
    List<Product> findExpensive(@Param("min") double min);
    
    @Query(value = "SELECT * FROM products WHERE category = ?1", nativeQuery = true)
    List<Product> findByCategoryNative(String category);
}
```

**Key Takeaway**: Name methods following Spring's convention and it generates queries automatically. Use `@Query` for complex cases."""),

("spring-boot","Spring Boot Entity Relationships","""Map database relationships with JPA annotations.

```java
// One-to-Many
@Entity
public class Author {
    @Id @GeneratedValue
    private Long id;
    private String name;
    
    @OneToMany(mappedBy = "author", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<Book> books = new ArrayList<>();
}

@Entity
public class Book {
    @Id @GeneratedValue
    private Long id;
    private String title;
    
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "author_id")
    private Author author;
}

// Many-to-Many
@Entity
public class Student {
    @ManyToMany
    @JoinTable(name = "enrollments",
        joinColumns = @JoinColumn(name = "student_id"),
        inverseJoinColumns = @JoinColumn(name = "course_id"))
    private Set<Course> courses = new HashSet<>();
}
```

**Key Takeaway**: Always use `FetchType.LAZY` for `@ManyToOne` and `@OneToMany` to avoid N+1 query problems."""),

("spring-boot","Spring Boot @Transactional","""Manage database transactions declaratively.

```java
@Service
public class TransferService {
    @Transactional // rolls back on RuntimeException
    public void transfer(Long fromId, Long toId, double amount) {
        Account from = accountRepo.findById(fromId).orElseThrow();
        Account to = accountRepo.findById(toId).orElseThrow();
        
        from.setBalance(from.getBalance() - amount);
        to.setBalance(to.getBalance() + amount);
        
        accountRepo.save(from);
        accountRepo.save(to);
        // If any exception here, BOTH saves are rolled back
    }
    
    @Transactional(readOnly = true) // optimization for reads
    public List<Account> getAll() { return accountRepo.findAll(); }
    
    @Transactional(propagation = Propagation.REQUIRES_NEW)
    public void logAudit(String msg) {
        // Runs in separate transaction
        auditRepo.save(new AuditLog(msg));
    }
}
```

**Key Takeaway**: `@Transactional` on class = all methods transactional. It only works on PUBLIC methods called from OUTSIDE the class (proxy-based)."""),

("spring-boot","Spring Boot Validation","""Validate request bodies with annotations.

```java
public class CreateUserRequest {
    @NotBlank(message = "Name is required")
    @Size(min = 2, max = 50)
    private String name;
    
    @Email(message = "Invalid email")
    @NotBlank
    private String email;
    
    @Min(value = 18, message = "Must be 18+")
    @Max(value = 120)
    private int age;
    
    @Pattern(regexp = "^[0-9]{10}$", message = "Must be 10 digits")
    private String phone;
    
    @NotNull @Size(min = 8)
    private String password;
}

@PostMapping("/users")
public ResponseEntity<?> create(@Valid @RequestBody CreateUserRequest req) {
    // Only reaches here if ALL validations pass
    return ResponseEntity.ok(userService.create(req));
}
```

**Key Takeaway**: Use `@Valid` on the parameter + constraint annotations on fields. Spring auto-returns 400 with validation errors."""),

("spring-boot","Spring Boot Global Exception Handling","""Centralized error handling with @ControllerAdvice.

```java
@RestControllerAdvice
public class GlobalExceptionHandler {
    @ExceptionHandler(ResourceNotFoundException.class)
    @ResponseStatus(HttpStatus.NOT_FOUND)
    public ErrorResponse handleNotFound(ResourceNotFoundException ex) {
        return new ErrorResponse(404, ex.getMessage(), LocalDateTime.now());
    }
    
    @ExceptionHandler(MethodArgumentNotValidException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public ErrorResponse handleValidation(MethodArgumentNotValidException ex) {
        String errors = ex.getBindingResult().getFieldErrors().stream()
            .map(e -> e.getField() + ": " + e.getDefaultMessage())
            .collect(Collectors.joining(", "));
        return new ErrorResponse(400, errors, LocalDateTime.now());
    }
    
    @ExceptionHandler(Exception.class)
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    public ErrorResponse handleAll(Exception ex) {
        return new ErrorResponse(500, "Internal server error", LocalDateTime.now());
    }
}
```"""),

("spring-boot","Spring Boot Profiles","""Environment-specific configuration.

```yaml
# application-dev.yml
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/app_dev
    username: root
  jpa:
    show-sql: true
    hibernate.ddl-auto: update

# application-prod.yml
spring:
  datasource:
    url: jdbc:mysql://prod-db:3306/app
    username: ${DB_USER}
    password: ${DB_PASS}
  jpa:
    show-sql: false
    hibernate.ddl-auto: validate
```

```bash
# Activate profile
java -jar app.jar --spring.profiles.active=prod
# Or environment variable
SPRING_PROFILES_ACTIVE=prod java -jar app.jar
```

**Key Takeaway**: Never hardcode credentials. Use profiles + environment variables for different environments."""),

("spring-boot","Spring Boot JWT Authentication","""Stateless authentication with JSON Web Tokens.

```java
@Service
public class JwtService {
    @Value("${jwt.secret}") private String secret;
    
    public String generateToken(UserDetails user) {
        return Jwts.builder()
            .setSubject(user.getUsername())
            .claim("role", user.getAuthorities())
            .setIssuedAt(new Date())
            .setExpiration(new Date(System.currentTimeMillis() + 86400000))
            .signWith(SignatureAlgorithm.HS256, secret)
            .compact();
    }
    
    public String extractUsername(String token) {
        return Jwts.parser().setSigningKey(secret)
            .parseClaimsJws(token).getBody().getSubject();
    }
    
    public boolean isValid(String token, UserDetails user) {
        return extractUsername(token).equals(user.getUsername()) 
            && !isExpired(token);
    }
}
```

**Key Takeaway**: JWT = stateless auth. Server doesn't store sessions. Token contains user info, signed with a secret key."""),

("spring-boot","Spring Boot AOP - Aspect Oriented Programming","""Handle cross-cutting concerns without polluting business logic.

```java
@Aspect
@Component
public class LoggingAspect {
    @Around("execution(* com.app.service.*.*(..))")
    public Object logTime(ProceedingJoinPoint jp) throws Throwable {
        long start = System.currentTimeMillis();
        Object result = jp.proceed();
        long ms = System.currentTimeMillis() - start;
        log.info("{}.{} took {}ms", jp.getSignature().getDeclaringTypeName(),
            jp.getSignature().getName(), ms);
        return result;
    }
    
    @Before("@annotation(Auditable)")
    public void audit(JoinPoint jp) {
        log.info("AUDIT: {} called by {}", jp.getSignature().getName(),
            SecurityContextHolder.getContext().getAuthentication().getName());
    }
}
```

**Key Takeaway**: AOP handles logging, security, metrics without modifying business code. Spring uses AOP internally for `@Transactional`, `@Cacheable`."""),

("spring-boot","Spring Boot Caching","""Reduce database calls with @Cacheable.

```java
@EnableCaching
@SpringBootApplication
public class App {}

@Service
public class ProductService {
    @Cacheable(value = "products", key = "#id")
    public Product findById(Long id) {
        log.info("DB call for id: {}", id); // only logs on cache MISS
        return productRepo.findById(id).orElseThrow();
    }
    
    @CachePut(value = "products", key = "#product.id")
    public Product update(Product product) {
        return productRepo.save(product); // updates cache
    }
    
    @CacheEvict(value = "products", key = "#id")
    public void delete(Long id) {
        productRepo.deleteById(id); // removes from cache
    }
    
    @CacheEvict(value = "products", allEntries = true)
    @Scheduled(fixedRate = 3600000)
    public void clearCache() {} // clear every hour
}
```

**Key Takeaway**: Default cache is in-memory (ConcurrentHashMap). Use Redis for production with `spring-boot-starter-data-redis`."""),

("spring-boot","Spring Boot Scheduling","""Run tasks on a schedule.

```java
@EnableScheduling
@SpringBootApplication
public class App {}

@Component
public class ScheduledTasks {
    @Scheduled(fixedRate = 60000)  // every 60 seconds
    public void checkExpiredSessions() {
        sessionService.removeExpired();
    }
    
    @Scheduled(cron = "0 0 9 * * MON-FRI")  // 9 AM weekdays
    public void sendDailyReport() {
        reportService.generateAndEmail();
    }
    
    @Scheduled(fixedDelay = 30000)  // 30s after LAST completion
    public void syncExternalData() {
        externalApi.sync();
    }
    
    @Scheduled(initialDelay = 5000, fixedRate = 60000)
    public void warmCache() {
        cacheService.warmUp();
    }
}
```

**Cron format**: `second minute hour day month weekday`
Example: `0 30 14 * * *` = 2:30 PM daily"""),

("spring-boot","Spring Boot Pagination and Sorting","""Paginate large result sets.

```java
@GetMapping("/products")
public Page<ProductDTO> list(
        @RequestParam(defaultValue = "0") int page,
        @RequestParam(defaultValue = "10") int size,
        @RequestParam(defaultValue = "id") String sortBy,
        @RequestParam(defaultValue = "asc") String dir) {
    
    Sort sort = dir.equals("desc") ? Sort.by(sortBy).descending() : Sort.by(sortBy).ascending();
    Pageable pageable = PageRequest.of(page, size, sort);
    return productRepo.findAll(pageable).map(this::toDTO);
}
```

Response:
```json
{
  "content": [{...}, {...}],
  "totalPages": 5,
  "totalElements": 48,
  "number": 0,
  "size": 10,
  "first": true,
  "last": false
}
```

**Key Takeaway**: Use `Page` for count queries, `Slice` when you only need hasNext (no count = faster)."""),

("spring-boot","Spring Boot Actuator","""Production monitoring endpoints.

```yaml
# application.yml
management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics,env
  endpoint:
    health:
      show-details: always
```

| Endpoint | Purpose |
|:---|:---|
| `/actuator/health` | App health + DB + disk |
| `/actuator/metrics` | JVM, HTTP, custom metrics |
| `/actuator/info` | App version, build info |
| `/actuator/env` | All config properties |

```java
// Custom health check
@Component
public class PaymentGatewayHealth implements HealthIndicator {
    public Health health() {
        boolean up = paymentGateway.ping();
        return up ? Health.up().withDetail("gateway","reachable").build()
                  : Health.down().withDetail("error","timeout").build();
    }
}
```

**Key Takeaway**: Secure actuator endpoints in production. Only expose `/health` publicly."""),

("spring-boot","Spring Boot DTO Pattern","""Separate API contracts from entities.

```java
// Entity (database)
@Entity
public class User {
    @Id @GeneratedValue private Long id;
    private String name;
    private String email;
    private String passwordHash;
    private LocalDateTime createdAt;
}

// Request DTO (input)
public record CreateUserRequest(
    @NotBlank String name,
    @Email String email,
    @Size(min=8) String password
) {}

// Response DTO (output) — no password!
public record UserResponse(Long id, String name, String email, LocalDateTime createdAt) {}

// Mapping
@Service
public class UserService {
    public UserResponse create(CreateUserRequest req) {
        User user = new User();
        user.setName(req.name());
        user.setEmail(req.email());
        user.setPasswordHash(encoder.encode(req.password()));
        user = repo.save(user);
        return new UserResponse(user.getId(), user.getName(), user.getEmail(), user.getCreatedAt());
    }
}
```

**Key Takeaway**: Never expose entities directly in APIs. DTOs protect sensitive fields and decouple DB schema from API contract."""),

("spring-boot","Spring Boot CORS Configuration","""Enable cross-origin requests for frontend apps.

```java
@Configuration
public class CorsConfig implements WebMvcConfigurer {
    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/api/**")
            .allowedOrigins("http://localhost:3000", "https://myapp.com")
            .allowedMethods("GET","POST","PUT","DELETE","OPTIONS")
            .allowedHeaders("*")
            .allowCredentials(true)
            .maxAge(3600);
    }
}

// Or per-controller
@CrossOrigin(origins = "http://localhost:3000")
@RestController
public class UserController { }

// Or per-method
@CrossOrigin(origins = "*")
@GetMapping("/public/data")
public List<Data> publicData() { }
```

**Key Takeaway**: Configure CORS on the backend, not frontend. In production, specify exact origins — never use `*` with credentials."""),

("spring-boot","Spring Boot Testing with MockMvc","""Test REST controllers without starting a server.

```java
@WebMvcTest(UserController.class)
class UserControllerTest {
    @Autowired private MockMvc mvc;
    @MockBean private UserService userService;
    @Autowired private ObjectMapper mapper;
    
    @Test
    void shouldCreateUser() throws Exception {
        CreateUserRequest req = new CreateUserRequest("Dipak","d@test.com","pass1234");
        UserResponse resp = new UserResponse(1L,"Dipak","d@test.com",LocalDateTime.now());
        when(userService.create(any())).thenReturn(resp);
        
        mvc.perform(post("/api/users")
                .contentType(MediaType.APPLICATION_JSON)
                .content(mapper.writeValueAsString(req)))
            .andExpect(status().isCreated())
            .andExpect(jsonPath("$.name").value("Dipak"))
            .andExpect(jsonPath("$.email").value("d@test.com"));
    }
    
    @Test
    void shouldReturn404() throws Exception {
        when(userService.findById(99L)).thenThrow(new NotFoundException("Not found"));
        mvc.perform(get("/api/users/99"))
            .andExpect(status().isNotFound());
    }
}
```"""),

("spring-boot","Spring Boot Flyway Database Migrations","""Version-control your database schema.

```sql
-- V1__Create_users_table.sql
CREATE TABLE users (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- V2__Add_role_to_users.sql
ALTER TABLE users ADD COLUMN role VARCHAR(20) DEFAULT 'USER';

-- V3__Create_orders_table.sql
CREATE TABLE orders (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    total DECIMAL(10,2),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

```yaml
# application.yml
spring:
  flyway:
    enabled: true
    locations: classpath:db/migration
```

**Key Takeaway**: Flyway runs migrations in order (V1, V2, V3...). Never modify an applied migration — create a new one. This keeps DB changes tracked like code."""),

("spring-boot","Spring Boot Microservices - Circuit Breaker","""Prevent cascading failures with Resilience4j.

```java
// pom.xml: spring-cloud-starter-circuitbreaker-resilience4j

@Service
public class PaymentService {
    @CircuitBreaker(name = "payment", fallbackMethod = "fallback")
    @Retry(name = "payment", maxAttempts = 3)
    @TimeLimiter(name = "payment")
    public CompletableFuture<PaymentResult> process(PaymentRequest req) {
        return CompletableFuture.supplyAsync(() -> 
            paymentGateway.charge(req) // may fail
        );
    }
    
    // Fallback when circuit opens
    public CompletableFuture<PaymentResult> fallback(PaymentRequest req, Throwable t) {
        log.warn("Payment service down, queuing for retry", t);
        return CompletableFuture.completedFuture(PaymentResult.queued());
    }
}
```

**Circuit States**: CLOSED (normal) → OPEN (failing, use fallback) → HALF_OPEN (testing recovery)

**Key Takeaway**: Circuit breaker stops calling a failing service, gives it time to recover, and provides fallback responses."""),

("spring-boot","Spring Boot WebSocket","""Real-time bidirectional communication.

```java
@Configuration
@EnableWebSocketMessageBroker
public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {
    public void registerStompEndpoints(StompEndpointRegistry reg) {
        reg.addEndpoint("/ws").setAllowedOrigins("*").withSockJS();
    }
    public void configureMessageBroker(MessageBrokerRegistry reg) {
        reg.enableSimpleBroker("/topic");
        reg.setApplicationDestinationPrefixes("/app");
    }
}

@Controller
public class ChatController {
    @MessageMapping("/chat.send")      // Client sends to /app/chat.send
    @SendTo("/topic/messages")          // Broadcast to all subscribers
    public ChatMessage send(ChatMessage msg) {
        return msg;
    }
}
```

```javascript
// Client
const socket = new SockJS('/ws');
const stompClient = Stomp.over(socket);
stompClient.subscribe('/topic/messages', (msg) => displayMessage(JSON.parse(msg.body)));
stompClient.send('/app/chat.send', {}, JSON.stringify({sender:'Dipak', content:'Hello!'}));
```"""),

# ═══════════════════════════════════════════════════════════════
# REACT — 30 topics
# ═══════════════════════════════════════════════════════════════
("react","JSX - JavaScript XML","""JSX lets you write HTML-like syntax in JavaScript.

```jsx
function Welcome({ name, age }) {
  const isAdult = age >= 18;
  return (
    <div className="card">
      <h1>Hello, {name}!</h1>
      {isAdult ? <p>Welcome aboard</p> : <p>Come back when you're 18</p>}
      <ul>
        {['React','Node','Java'].map(skill => (
          <li key={skill}>{skill}</li>
        ))}
      </ul>
      <p style={{ color: 'blue', fontSize: '14px' }}>Styled inline</p>
    </div>
  );
}
```

**Key Takeaway**: JSX is syntactic sugar for `React.createElement()`. Use `className` not `class`, `htmlFor` not `for`."""),

("react","React useState Hook","""Manage component state with useState.

```jsx
function Counter() {
  const [count, setCount] = useState(0);
  const [user, setUser] = useState({ name: '', email: '' });

  // Functional update (when new state depends on old)
  const increment = () => setCount(prev => prev + 1);
  
  // Update object state (spread to keep other fields)
  const updateName = (name) => setUser(prev => ({ ...prev, name }));

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={increment}>+1</button>
      <input value={user.name} onChange={e => updateName(e.target.value)} />
    </div>
  );
}
```

**Key Takeaway**: `setState` is async and batched. Use functional form `prev => ...` when new state depends on old state. Never mutate state directly."""),

("react","React useEffect Hook","""Handle side effects: API calls, subscriptions, timers.

```jsx
function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const controller = new AbortController();
    
    async function fetchUser() {
      setLoading(true);
      try {
        const res = await fetch(`/api/users/${userId}`, { signal: controller.signal });
        const data = await res.json();
        setUser(data);
      } catch (err) {
        if (err.name !== 'AbortError') console.error(err);
      } finally {
        setLoading(false);
      }
    }
    fetchUser();
    
    return () => controller.abort(); // Cleanup on unmount/re-render
  }, [userId]); // Re-run when userId changes

  if (loading) return <p>Loading...</p>;
  return <h1>{user?.name}</h1>;
}
```

**Key Takeaway**: Always return a cleanup function for subscriptions/timers. Empty deps `[]` = run once. No deps = run every render."""),

("react","React useContext - Global State","""Share data without prop drilling.

```jsx
const AuthContext = createContext(null);

function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const login = (userData) => setUser(userData);
  const logout = () => setUser(null);
  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

// Custom hook for clean usage
function useAuth() {
  const context = useContext(AuthContext);
  if (!context) throw new Error('useAuth must be inside AuthProvider');
  return context;
}

// Any nested component
function Navbar() {
  const { user, logout } = useAuth();
  return user ? <button onClick={logout}>Logout {user.name}</button> 
              : <Link to="/login">Login</Link>;
}
```

**Key Takeaway**: Context re-renders ALL consumers when value changes. Split contexts by concern to minimize re-renders."""),

("react","React useReducer for Complex State","""Better than useState for complex state logic.

```jsx
const initialState = { items: [], total: 0, loading: false, error: null };

function cartReducer(state, action) {
  switch (action.type) {
    case 'ADD_ITEM':
      return { ...state, items: [...state.items, action.payload],
               total: state.total + action.payload.price };
    case 'REMOVE_ITEM':
      const item = state.items.find(i => i.id === action.payload);
      return { ...state, items: state.items.filter(i => i.id !== action.payload),
               total: state.total - item.price };
    case 'SET_LOADING': return { ...state, loading: action.payload };
    case 'SET_ERROR': return { ...state, error: action.payload, loading: false };
    case 'CLEAR': return initialState;
    default: return state;
  }
}

function Cart() {
  const [state, dispatch] = useReducer(cartReducer, initialState);
  return <button onClick={() => dispatch({ type: 'ADD_ITEM', payload: product })}>Add</button>;
}
```

**Key Takeaway**: useReducer is better when state transitions are complex or depend on previous state. Think: multiple related state fields."""),

("react","React Custom Hooks","""Extract reusable logic into custom hooks.

```jsx
// useFetch — reusable data fetching
function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const controller = new AbortController();
    setLoading(true);
    fetch(url, { signal: controller.signal })
      .then(res => res.json())
      .then(setData)
      .catch(setError)
      .finally(() => setLoading(false));
    return () => controller.abort();
  }, [url]);

  return { data, loading, error };
}

// Usage in any component
function Products() {
  const { data, loading, error } = useFetch('/api/products');
  if (loading) return <Spinner />;
  if (error) return <Error message={error} />;
  return <ProductList items={data} />;
}
```

**Rules**: Name starts with `use`. Can call other hooks. Each call gets its own isolated state."""),

("react","React Router v6","""Client-side routing for SPAs.

```jsx
import { BrowserRouter, Routes, Route, Link, useParams, useNavigate, Navigate } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/products">Products</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/products" element={<Products />} />
        <Route path="/products/:id" element={<ProductDetail />} />
        <Route path="/admin" element={
          isAuth ? <Admin /> : <Navigate to="/login" replace />
        } />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}

function ProductDetail() {
  const { id } = useParams();
  const navigate = useNavigate();
  return (
    <div>
      <h1>Product {id}</h1>
      <button onClick={() => navigate(-1)}>Back</button>
    </div>
  );
}
```"""),

("react","React Performance - memo and useCallback","""Prevent unnecessary re-renders.

```jsx
// React.memo: skip re-render if props unchanged
const ExpensiveList = React.memo(({ items, onSelect }) => {
  console.log('Rendering list...'); // Only when items/onSelect change
  return items.map(item => (
    <div key={item.id} onClick={() => onSelect(item.id)}>{item.name}</div>
  ));
});

// useCallback: memoize function reference
function Parent() {
  const [count, setCount] = useState(0);
  const [items] = useState([{id:1,name:'A'},{id:2,name:'B'}]);
  
  // Without useCallback: new function every render → child re-renders
  const handleSelect = useCallback((id) => {
    console.log('Selected:', id);
  }, []); // stable reference
  
  return (
    <>
      <button onClick={() => setCount(c=>c+1)}>Count: {count}</button>
      <ExpensiveList items={items} onSelect={handleSelect} />
    </>
  );
}
```

**Key Takeaway**: Only optimize after measuring. React.memo + useCallback work together. Premature optimization adds complexity."""),

("react","React Error Boundaries","""Catch render errors gracefully.

```jsx
class ErrorBoundary extends React.Component {
  state = { hasError: false, error: null };
  
  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }
  
  componentDidCatch(error, info) {
    logErrorToService(error, info.componentStack);
  }
  
  render() {
    if (this.state.hasError) {
      return (
        <div className="error-fallback">
          <h2>Something went wrong</h2>
          <p>{this.state.error?.message}</p>
          <button onClick={() => this.setState({hasError:false})}>Try Again</button>
        </div>
      );
    }
    return this.props.children;
  }
}

// Usage
<ErrorBoundary>
  <UserProfile />  {/* If this crashes, fallback UI shows */}
</ErrorBoundary>
```

**Key Takeaway**: Error boundaries only catch rendering errors. They do NOT catch errors in event handlers, async code, or server-side rendering."""),

("react","React State Management with Redux Toolkit","""Modern Redux with less boilerplate.

```jsx
import { createSlice, configureStore } from '@reduxjs/toolkit';

const cartSlice = createSlice({
  name: 'cart',
  initialState: { items: [], total: 0 },
  reducers: {
    addItem: (state, action) => {
      state.items.push(action.payload); // Immer handles immutability!
      state.total += action.payload.price;
    },
    removeItem: (state, action) => {
      const idx = state.items.findIndex(i => i.id === action.payload);
      state.total -= state.items[idx].price;
      state.items.splice(idx, 1);
    },
    clearCart: (state) => { state.items = []; state.total = 0; }
  }
});

export const { addItem, removeItem, clearCart } = cartSlice.actions;
const store = configureStore({ reducer: { cart: cartSlice.reducer } });

// Component
function Cart() {
  const { items, total } = useSelector(state => state.cart);
  const dispatch = useDispatch();
  return <button onClick={() => dispatch(addItem(product))}>Add to Cart</button>;
}
```"""),

# ═══════════════════════════════════════════════════════════════
# JAVASCRIPT — 25 topics
# ═══════════════════════════════════════════════════════════════
("javascript","Closures in JavaScript","""A function that remembers its outer scope.

```javascript
function createCounter(initial = 0) {
  let count = initial;
  return {
    increment: () => ++count,
    decrement: () => --count,
    getCount: () => count,
    reset: () => { count = initial; }
  };
}

const counter = createCounter(10);
counter.increment(); // 11
counter.increment(); // 12
counter.getCount();  // 12

// Common pitfall
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100); // 3, 3, 3 (var is function-scoped!)
}
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100); // 0, 1, 2 (let is block-scoped)
}
```

**Key Takeaway**: Closures capture variables by reference, not value. Use `let` in loops to avoid the classic closure trap."""),

("javascript","Promises and async-await","""Handle asynchronous operations.

```javascript
// Promise chain
fetch('/api/users/1')
  .then(res => res.json())
  .then(user => fetch(`/api/posts?userId=${user.id}`))
  .then(res => res.json())
  .then(posts => console.log(posts))
  .catch(err => console.error(err));

// async/await (cleaner)
async function getUserPosts(userId) {
  try {
    const userRes = await fetch(`/api/users/${userId}`);
    const user = await userRes.json();
    const postsRes = await fetch(`/api/posts?userId=${user.id}`);
    return await postsRes.json();
  } catch (err) {
    console.error('Failed:', err);
    return [];
  }
}

// Parallel execution
const [users, posts] = await Promise.all([
  fetch('/api/users').then(r => r.json()),
  fetch('/api/posts').then(r => r.json())
]);
```

**Key Takeaway**: Use `Promise.all()` for independent async calls (parallel), `await` for sequential chains."""),

("javascript","Event Loop and Task Queues","""Why JS is single-threaded but non-blocking.

```javascript
console.log('1');                              // Sync (Call Stack)
setTimeout(() => console.log('2'), 0);         // Macro task
Promise.resolve().then(() => console.log('3'));  // Micro task
queueMicrotask(() => console.log('4'));         // Micro task
console.log('5');                              // Sync (Call Stack)

// Output: 1, 5, 3, 4, 2
```

### Execution Order
1. **Call Stack** — synchronous code runs first
2. **Microtask Queue** — Promises, queueMicrotask (runs after EACH macro task)
3. **Macrotask Queue** — setTimeout, setInterval, I/O

**Key Takeaway**: Microtasks (Promises) ALWAYS execute before macrotasks (setTimeout), even with 0ms delay."""),

("javascript","Destructuring and Spread","""Extract values and merge objects/arrays.

```javascript
// Object destructuring
const { name, age, address: { city } } = user;
const { role = 'user', theme = 'dark' } = settings; // defaults
const { name: userName, id: oderId } = response; // rename

// Array destructuring
const [first, second, ...rest] = [1, 2, 3, 4, 5];
// first=1, second=2, rest=[3,4,5]

// Spread
const merged = { ...defaults, ...userPrefs, timestamp: Date.now() };
const newArr = [...oldArr, newItem];
const clone = { ...original }; // shallow clone

// Function params
function createUser({ name, email, role = 'user' }) {
  return { name, email, role, createdAt: new Date() };
}
createUser({ name: 'Dipak', email: 'd@test.com' });
```

**Key Takeaway**: Spread creates shallow copies. For deep clone use `structuredClone()` (modern) or `JSON.parse(JSON.stringify())`."""),

("javascript","Array Methods - map filter reduce","""Functional array transformations.

```javascript
const products = [
  { name: 'Laptop', price: 999, inStock: true },
  { name: 'Phone', price: 699, inStock: false },
  { name: 'Tablet', price: 499, inStock: true },
];

// filter: keep matching items
const available = products.filter(p => p.inStock);

// map: transform each item
const names = products.map(p => p.name);
const discounted = products.map(p => ({ ...p, price: p.price * 0.9 }));

// reduce: accumulate to single value
const total = products.reduce((sum, p) => sum + p.price, 0); // 2197

// Chaining
const result = products
  .filter(p => p.inStock)
  .map(p => p.price)
  .reduce((sum, price) => sum + price, 0); // 1498

// find, some, every
const laptop = products.find(p => p.name === 'Laptop');
const anyExpensive = products.some(p => p.price > 500);     // true
const allInStock = products.every(p => p.inStock);           // false
```"""),

("javascript","Debounce and Throttle","""Control function execution frequency.

```javascript
// Debounce: wait for pause in calls
function debounce(fn, delay) {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), delay);
  };
}

// Throttle: limit to once per interval
function throttle(fn, limit) {
  let throttled = false;
  return (...args) => {
    if (!throttled) {
      fn(...args);
      throttled = true;
      setTimeout(() => throttled = false, limit);
    }
  };
}

// Usage
searchInput.addEventListener('input', debounce(fetchResults, 300));
window.addEventListener('scroll', throttle(updatePosition, 100));
```

| | Debounce | Throttle |
|:---|:---|:---|
| Fires | After silence | At intervals |
| Use case | Search input, resize | Scroll, mousemove |"""),

("javascript","ES6 Modules","""Organize code with import/export.

```javascript
// math.js — Named exports
export const PI = 3.14159;
export function add(a, b) { return a + b; }
export class Calculator { /* ... */ }

// Default export
export default class UserService {
  getUser(id) { /* ... */ }
}

// Import
import UserService from './UserService.js';           // default
import { PI, add } from './math.js';                  // named
import { add as sum } from './math.js';               // rename
import * as Math from './math.js';                    // all

// Dynamic import (code splitting)
const module = await import('./heavyModule.js');
module.doSomething();

// Re-export (barrel file)
export { default as UserService } from './UserService.js';
export { PI, add } from './math.js';
```

**Key Takeaway**: Use named exports for utilities, default export for main class/component. Dynamic imports enable lazy loading."""),

("javascript","Map Set and WeakMap","""Modern collection types beyond Object and Array.

```javascript
// Map: any type as key, ordered, iterable
const cache = new Map();
cache.set(userObj, 'cached data');    // object as key!
cache.set(42, 'number key');
cache.get(userObj);  // 'cached data'
cache.has(42);       // true
cache.size;          // 2

// Set: unique values
const set = new Set([1, 2, 3, 2, 1]); // Set(3) {1, 2, 3}
const unique = [...new Set(array)];     // remove duplicates

// Set operations
const a = new Set([1,2,3]), b = new Set([2,3,4]);
const union = new Set([...a, ...b]);                    // {1,2,3,4}
const intersection = new Set([...a].filter(x => b.has(x))); // {2,3}

// WeakMap: garbage-collectible keys
const metadata = new WeakMap();
metadata.set(element, { clicks: 0 }); // auto-removed when element is GC'd
```

**Key Takeaway**: Use Map over Object when keys aren't strings. Use Set for unique collections. WeakMap for caches that shouldn't prevent GC."""),

# ═══════════════════════════════════════════════════════════════
# .NET / C# — 20 topics
# ═══════════════════════════════════════════════════════════════
("dotnet","C# LINQ Essentials","""Language Integrated Query for collections.

```csharp
var students = new List<Student>();

// Filter + sort + project
var topStudents = students
    .Where(s => s.GPA > 3.5)
    .OrderByDescending(s => s.GPA)
    .Select(s => new { s.Name, s.GPA })
    .Take(10).ToList();

// Grouping
var byDept = students
    .GroupBy(s => s.Department)
    .Select(g => new { Dept = g.Key, Count = g.Count(), Avg = g.Average(s => s.GPA) });

// Aggregation
int total = numbers.Sum();
var first = students.FirstOrDefault(s => s.Id == 1);
bool any = students.Any(s => s.GPA > 3.8);
bool all = students.All(s => s.Age >= 18);

// Join
var result = students.Join(courses, s => s.CourseId, c => c.Id,
    (s, c) => new { s.Name, CourseName = c.Title });
```

**Key Takeaway**: LINQ is lazy — queries execute only when you enumerate (ToList, foreach, Count). Chain operations for readable data pipelines."""),

("dotnet","C# Async Await","""Non-blocking async programming.

```csharp
public async Task<UserProfile> GetDashboardAsync(int userId) {
    // Run in parallel
    var userTask = GetUserAsync(userId);
    var ordersTask = GetOrdersAsync(userId);
    var statsTask = GetStatsAsync(userId);
    
    await Task.WhenAll(userTask, ordersTask, statsTask);
    
    return new UserProfile(userTask.Result, ordersTask.Result, statsTask.Result);
}

public async Task<User> GetUserAsync(int id) {
    var user = await _context.Users.FindAsync(id);
    if (user == null) throw new NotFoundException($"User {id} not found");
    return user;
}
```

### Rules
1. Never use `.Result` or `.Wait()` — deadlock risk
2. Use `async Task` not `async void` (except event handlers)
3. All the way async — don't mix sync and async

**Key Takeaway**: Async doesn't mean multithreaded. It frees the thread during I/O waits, improving scalability."""),

("dotnet","ASP.NET Core Middleware Pipeline","""Request processing pipeline.

```csharp
var app = builder.Build();

app.UseExceptionHandler("/error");  // 1. Error handling
app.UseHttpsRedirection();           // 2. Force HTTPS
app.UseCors();                       // 3. CORS
app.UseAuthentication();             // 4. Who are you?
app.UseAuthorization();              // 5. Can you do this?
app.MapControllers();                // 6. Route to controller

// Custom middleware
app.Use(async (context, next) => {
    var sw = Stopwatch.StartNew();
    await next();
    sw.Stop();
    context.Response.Headers.Append("X-Response-Time", $"{sw.ElapsedMilliseconds}ms");
});
```

**Key Takeaway**: Order matters! Authentication must come before Authorization. Exception handler should be first to catch all errors."""),

("dotnet","ASP.NET Core Dependency Injection","""Built-in DI container.

```csharp
var builder = WebApplication.CreateBuilder(args);

// Service lifetimes
builder.Services.AddTransient<IEmailService, EmailService>();  // New each time
builder.Services.AddScoped<IOrderService, OrderService>();     // Per HTTP request
builder.Services.AddSingleton<ICacheService, CacheService>();  // App lifetime

// Constructor injection
[ApiController]
[Route("api/[controller]")]
public class OrdersController : ControllerBase {
    private readonly IOrderService _orderService;
    
    public OrdersController(IOrderService orderService) {
        _orderService = orderService;
    }
    
    [HttpGet("{id}")]
    public async Task<IActionResult> Get(int id) {
        var order = await _orderService.GetByIdAsync(id);
        return order == null ? NotFound() : Ok(order);
    }
}
```

| Lifetime | Scope | Use Case |
|:---|:---|:---|
| Transient | New every time | Lightweight, stateless |
| Scoped | Per request | DbContext, per-request data |
| Singleton | App lifetime | Caching, config |"""),

("dotnet","Entity Framework Core Basics","""ORM for .NET database operations.

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

**Key Takeaway**: Use migrations (`dotnet ef migrations add ...`) to version-control schema changes. Never use `EnsureCreated()` in production."""),

("dotnet","C# Pattern Matching","""Modern type checking and data extraction.

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

**Key Takeaway**: Pattern matching replaces complex if-else chains with readable, declarative code."""),

# ═══════════════════════════════════════════════════════════════
# NODE.JS — 15 topics
# ═══════════════════════════════════════════════════════════════
("nodejs","Express Middleware Chain","""Request pipeline in Express.

```javascript
const express = require('express');
const app = express();

// 1. Built-in middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// 2. Custom logging middleware
app.use((req, res, next) => {
  console.log(`${req.method} ${req.url} - ${new Date().toISOString()}`);
  next();
});

// 3. Auth middleware (reusable)
const auth = (req, res, next) => {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) return res.status(401).json({ error: 'No token' });
  try { req.user = jwt.verify(token, SECRET); next(); }
  catch { res.status(403).json({ error: 'Invalid token' }); }
};

app.get('/profile', auth, (req, res) => res.json(req.user));

// 4. Error middleware (4 params!)
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong' });
});
```"""),

("nodejs","Mongoose Schema Design","""MongoDB ODM for Node.js.

```javascript
const userSchema = new Schema({
  name: { type: String, required: true, trim: true },
  email: { type: String, required: true, unique: true, lowercase: true },
  password: { type: String, required: true, minlength: 8, select: false },
  role: { type: String, enum: ['user','admin'], default: 'user' },
  createdAt: { type: Date, default: Date.now }
});

// Pre-save hook
userSchema.pre('save', async function(next) {
  if (!this.isModified('password')) return next();
  this.password = await bcrypt.hash(this.password, 12);
  next();
});

// Instance method
userSchema.methods.comparePassword = async function(candidate) {
  return bcrypt.compare(candidate, this.password);
};

// Static method
userSchema.statics.findByEmail = function(email) {
  return this.findOne({ email });
};
```

**Key Takeaway**: Use hooks for cross-cutting concerns (hashing, timestamps). Use `select: false` to exclude sensitive fields by default."""),

("nodejs","MongoDB Aggregation Pipeline","""Complex data processing in MongoDB.

```javascript
const analytics = await Order.aggregate([
  { $match: { status: 'completed', date: { $gte: startOfMonth } } },
  { $unwind: '$items' },
  { $group: {
      _id: '$items.category',
      revenue: { $sum: { $multiply: ['$items.price','$items.qty'] } },
      orders: { $sum: 1 },
      avgValue: { $avg: '$total' }
  }},
  { $sort: { revenue: -1 } },
  { $limit: 10 },
  { $project: {
      category: '$_id', revenue: { $round: ['$revenue',2] },
      orders: 1, avgValue: { $round: ['$avgValue',2] }, _id: 0
  }}
]);
```

| Stage | Purpose |
|:---|:---|
| $match | Filter documents |
| $group | Aggregate (sum, avg, count) |
| $sort | Order results |
| $project | Reshape output |
| $lookup | JOIN collections |
| $unwind | Flatten arrays |"""),

# ═══════════════════════════════════════════════════════════════
# DATABASE / SQL — 15 topics
# ═══════════════════════════════════════════════════════════════
("database","SQL JOINs Explained","""Combine data from multiple tables.

```sql
-- INNER JOIN: only matching
SELECT u.name, o.total FROM users u
INNER JOIN orders o ON u.id = o.user_id;

-- LEFT JOIN: all users + their orders (NULL if none)
SELECT u.name, COUNT(o.id) as order_count
FROM users u LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.name;

-- Self JOIN: find employees and their managers
SELECT e.name AS employee, m.name AS manager
FROM employees e LEFT JOIN employees m ON e.manager_id = m.id;
```

**Key Takeaway**: Always index JOIN columns for performance. LEFT JOIN = all left rows; RIGHT JOIN = all right rows."""),

("database","SQL Window Functions","""Calculations across rows without grouping.

```sql
-- Rank employees by salary per department
SELECT name, department, salary,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) as rank,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) as rank_with_ties,
    DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) as dense_rank
FROM employees;

-- Running total
SELECT date, amount,
    SUM(amount) OVER (ORDER BY date) as running_total
FROM transactions;

-- Moving average
SELECT date, amount,
    AVG(amount) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) as moving_avg
FROM daily_sales;

-- Previous/Next row
SELECT date, amount,
    LAG(amount, 1) OVER (ORDER BY date) as prev_amount,
    LEAD(amount, 1) OVER (ORDER BY date) as next_amount
FROM transactions;
```"""),

("database","SQL Transactions and ACID","""Ensure data integrity with transactions.

```sql
START TRANSACTION;

UPDATE accounts SET balance = balance - 500 WHERE id = 1;
UPDATE accounts SET balance = balance + 500 WHERE id = 2;

-- If both succeed
COMMIT;
-- If anything fails
ROLLBACK;
```

| Property | Meaning |
|:---|:---|
| Atomicity | All or nothing |
| Consistency | Valid state before and after |
| Isolation | Concurrent txns don't interfere |
| Durability | Committed data survives crashes |

| Isolation Level | Dirty Read | Non-Repeatable | Phantom |
|:---|:---|:---|:---|
| READ UNCOMMITTED | Yes | Yes | Yes |
| READ COMMITTED | No | Yes | Yes |
| REPEATABLE READ | No | No | Yes |
| SERIALIZABLE | No | No | No |

**Key Takeaway**: MySQL default is REPEATABLE READ. Use SERIALIZABLE only when absolutely needed — it's the slowest."""),

("database","Database Indexing Deep Dive","""Speed up queries with proper indexes.

```sql
-- Single column index
CREATE INDEX idx_email ON users(email);

-- Composite index (column order matters!)
CREATE INDEX idx_status_date ON orders(status, created_at);

-- Partial index (PostgreSQL)
CREATE INDEX idx_active ON users(email) WHERE is_active = true;

-- EXPLAIN to verify
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'test@mail.com';
-- Look for: Index Scan (good) vs Seq Scan (bad)
```

### Composite Index Leftmost Prefix Rule
```sql
-- Index on (A, B, C) supports:
-- WHERE A = ?              YES
-- WHERE A = ? AND B = ?    YES
-- WHERE A = ? AND B = ? AND C = ?  YES
-- WHERE B = ?              NO! (doesn't use index)
-- WHERE C = ?              NO!
```

**Key Takeaway**: Index columns you WHERE, JOIN, and ORDER BY most. Too many indexes slow down writes."""),

("database","SQL Query Optimization","""Write faster queries.

```sql
-- 1. Avoid SELECT *
SELECT id, name, email FROM users; -- Only needed columns

-- 2. EXISTS over IN for subqueries
SELECT * FROM users u WHERE EXISTS (
    SELECT 1 FROM orders o WHERE o.user_id = u.id
); -- Stops at first match

-- 3. Cursor pagination over OFFSET
SELECT * FROM posts WHERE id > 20000 ORDER BY id LIMIT 20;
-- vs slow: OFFSET 20000 LIMIT 20

-- 4. Batch inserts
INSERT INTO logs (msg) VALUES ('a'),('b'),('c'),('d');

-- 5. Avoid functions on indexed columns
WHERE created_at >= '2024-01-01'     -- uses index
WHERE YEAR(created_at) = 2024       -- can't use index!

-- 6. Use EXPLAIN
EXPLAIN ANALYZE SELECT * FROM orders WHERE status = 'pending';
```

**Key Takeaway**: Run EXPLAIN on slow queries. Look for full table scans and missing indexes."""),

# ═══════════════════════════════════════════════════════════════
# DSA — 30 topics
# ═══════════════════════════════════════════════════════════════
("dsa","Two Pointer Technique","""Solve array problems in O(n) instead of O(n²).

```java
// Pattern 1: Opposite ends (sorted array)
public int[] twoSum(int[] nums, int target) {
    int l = 0, r = nums.length - 1;
    while (l < r) {
        int sum = nums[l] + nums[r];
        if (sum == target) return new int[]{l, r};
        else if (sum < target) l++;
        else r--;
    }
    return new int[]{-1, -1};
}

// Pattern 2: Fast & Slow
public int removeDuplicates(int[] nums) {
    int slow = 0;
    for (int fast = 1; fast < nums.length; fast++)
        if (nums[fast] != nums[slow]) nums[++slow] = nums[fast];
    return slow + 1;
}
```

**Use when**: Sorted arrays, pair finding, palindrome check, container with most water."""),

("dsa","Sliding Window","""Find optimal subarray/substring in O(n).

```java
// Fixed window: max sum of k elements
public int maxSum(int[] arr, int k) {
    int sum = 0, max = 0;
    for (int i = 0; i < arr.length; i++) {
        sum += arr[i];
        if (i >= k) sum -= arr[i - k];
        if (i >= k - 1) max = Math.max(max, sum);
    }
    return max;
}

// Variable window: longest substring without repeating
public int lengthOfLongestSubstring(String s) {
    Set<Character> set = new HashSet<>();
    int l = 0, max = 0;
    for (int r = 0; r < s.length(); r++) {
        while (set.contains(s.charAt(r))) set.remove(s.charAt(l++));
        set.add(s.charAt(r));
        max = Math.max(max, r - l + 1);
    }
    return max;
}
```

**Pattern**: Expand right, shrink left when constraint violated."""),

("dsa","Binary Search Variations","""Beyond simple sorted array search.

```java
// Find first occurrence
public int firstOccurrence(int[] arr, int target) {
    int lo = 0, hi = arr.length - 1, result = -1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] == target) { result = mid; hi = mid - 1; }
        else if (arr[mid] < target) lo = mid + 1;
        else hi = mid - 1;
    }
    return result;
}

// Binary search on answer: minimum capacity to ship in D days
public int shipWithinDays(int[] weights, int days) {
    int lo = Arrays.stream(weights).max().getAsInt();
    int hi = Arrays.stream(weights).sum();
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (canShip(weights, days, mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
```

**Key Takeaway**: "Find minimum X that satisfies condition" = Binary Search on Answer."""),

("dsa","Dynamic Programming - Patterns","""Break problems into overlapping subproblems.

```java
// 1. Fibonacci (Bottom-up, O(n) time, O(1) space)
public int fib(int n) {
    int prev2 = 0, prev1 = 1;
    for (int i = 2; i <= n; i++) {
        int curr = prev1 + prev2;
        prev2 = prev1; prev1 = curr;
    }
    return prev1;
}

// 2. Coin Change (minimum coins to make amount)
public int coinChange(int[] coins, int amount) {
    int[] dp = new int[amount + 1];
    Arrays.fill(dp, amount + 1);
    dp[0] = 0;
    for (int i = 1; i <= amount; i++)
        for (int c : coins)
            if (c <= i) dp[i] = Math.min(dp[i], dp[i - c] + 1);
    return dp[amount] > amount ? -1 : dp[amount];
}
```

**DP Steps**: 1. Define state → 2. Recurrence relation → 3. Base case → 4. Optimize space."""),

("dsa","Graph BFS and DFS","""Traverse graphs level-by-level or depth-first.

```java
// BFS — shortest path in unweighted graph
public int shortestPath(Map<Integer,List<Integer>> graph, int src, int dest) {
    Queue<Integer> queue = new LinkedList<>();
    Set<Integer> visited = new HashSet<>();
    queue.offer(src); visited.add(src);
    int dist = 0;
    while (!queue.isEmpty()) {
        int size = queue.size();
        for (int i = 0; i < size; i++) {
            int node = queue.poll();
            if (node == dest) return dist;
            for (int neighbor : graph.getOrDefault(node, List.of()))
                if (visited.add(neighbor)) queue.offer(neighbor);
        }
        dist++;
    }
    return -1;
}

// DFS — detect cycle in directed graph
public boolean hasCycle(Map<Integer,List<Integer>> graph, int node,
        Set<Integer> visited, Set<Integer> recursionStack) {
    visited.add(node); recursionStack.add(node);
    for (int n : graph.getOrDefault(node, List.of())) {
        if (recursionStack.contains(n)) return true;
        if (!visited.contains(n) && hasCycle(graph,n,visited,recursionStack)) return true;
    }
    recursionStack.remove(node);
    return false;
}
```"""),

("dsa","Trie Data Structure","""Efficient prefix search and autocomplete.

```java
class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isEnd = false;
}

class Trie {
    TrieNode root = new TrieNode();
    
    void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            int i = c - 'a';
            if (node.children[i] == null) node.children[i] = new TrieNode();
            node = node.children[i];
        }
        node.isEnd = true;
    }
    
    boolean search(String word) {
        TrieNode node = find(word);
        return node != null && node.isEnd;
    }
    
    boolean startsWith(String prefix) { return find(prefix) != null; }
    
    private TrieNode find(String s) {
        TrieNode node = root;
        for (char c : s.toCharArray()) {
            node = node.children[c - 'a'];
            if (node == null) return null;
        }
        return node;
    }
}
```

**Use cases**: Autocomplete, spell checker, IP routing, word games."""),

("dsa","Union-Find Disjoint Set","""Track connected components efficiently.

```java
class UnionFind {
    int[] parent, rank;
    int components;
    
    UnionFind(int n) {
        parent = new int[n]; rank = new int[n]; components = n;
        for (int i = 0; i < n; i++) parent[i] = i;
    }
    
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]); // path compression
        return parent[x];
    }
    
    boolean union(int x, int y) {
        int px = find(x), py = find(y);
        if (px == py) return false;
        if (rank[px] < rank[py]) { int t=px; px=py; py=t; }
        parent[py] = px;
        if (rank[px] == rank[py]) rank[px]++;
        components--;
        return true;
    }
}
```

**Use cases**: Number of islands, cycle detection, Kruskal's MST, network connectivity.
**Time**: Nearly O(1) per operation with path compression + union by rank."""),

("dsa","Heap and Priority Queue","""Efficiently find min/max elements.

```java
// Min-heap: smallest element at top
PriorityQueue<Integer> minHeap = new PriorityQueue<>();

// Max-heap: largest at top
PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());

// Kth largest element — O(n log k)
public int findKthLargest(int[] nums, int k) {
    PriorityQueue<Integer> pq = new PriorityQueue<>();
    for (int n : nums) {
        pq.offer(n);
        if (pq.size() > k) pq.poll();
    }
    return pq.peek();
}

// Top K frequent elements
public int[] topKFrequent(int[] nums, int k) {
    Map<Integer,Integer> freq = new HashMap<>();
    for (int n : nums) freq.merge(n, 1, Integer::sum);
    
    PriorityQueue<Map.Entry<Integer,Integer>> pq = 
        new PriorityQueue<>((a,b) -> b.getValue() - a.getValue());
    pq.addAll(freq.entrySet());
    
    int[] result = new int[k];
    for (int i = 0; i < k; i++) result[i] = pq.poll().getKey();
    return result;
}
```"""),

# ═══════════════════════════════════════════════════════════════
# SYSTEM DESIGN — 20 topics
# ═══════════════════════════════════════════════════════════════
("system-design","CAP Theorem","""In distributed systems, choose 2 of 3.

- **C**onsistency — every read gets latest write
- **A**vailability — every request gets a response  
- **P**artition Tolerance — works despite network failures

| DB | Type | Trade-off |
|:---|:---|:---|
| MySQL, PostgreSQL | CP | Consistent, may become unavailable |
| Cassandra, DynamoDB | AP | Available, may serve stale data |
| MongoDB | CP (default) | Configurable |

### Practical Rule
- **Banking/Payments** → CP (consistency critical)
- **Social Media Feed** → AP (availability matters, slight staleness OK)
- **Shopping Cart** → AP (availability, merge conflicts later)

**Key Takeaway**: Network partitions WILL happen. The real question is: do you sacrifice consistency or availability?"""),

("system-design","Load Balancing","""Distribute traffic across servers.

| Algorithm | How | Best For |
|:---|:---|:---|
| Round Robin | Sequential rotation | Equal servers |
| Weighted RR | More to stronger servers | Mixed specs |
| Least Connections | Fewest active requests | Variable request duration |
| IP Hash | Same client → same server | Session affinity |

### Nginx Config
```nginx
upstream backend {
    least_conn;
    server server1:8080 weight=3;
    server server2:8080 weight=1;
    server server3:8080 backup;
}
server {
    location /api/ {
        proxy_pass http://backend;
    }
}
```

### L4 vs L7
- **Layer 4**: TCP level, fast, routes by IP/port
- **Layer 7**: HTTP level, smart, routes by URL/headers/cookies

**Key Takeaway**: Use L7 load balancers for web apps (URL-based routing, SSL termination). L4 for raw TCP throughput."""),

("system-design","Caching Strategies","""Speed up reads and reduce database load.

### Cache-Aside (Lazy Loading)
```
App checks cache → miss → read DB → write to cache → return
```
Best for: Read-heavy workloads

### Write-Through
```
App writes to cache → cache writes to DB (sync) → return
```
Best for: Data consistency required

### Write-Behind
```
App writes to cache → return immediately → cache writes DB later (async)
```
Best for: Write-heavy, eventual consistency OK

### Cache Invalidation
| Strategy | Approach |
|:---|:---|
| TTL | Auto-expire after time |
| Event-based | Invalidate on data change |
| Version-based | Compare version numbers |

**Key Takeaway**: "There are only two hard things in CS: cache invalidation and naming things." Start with TTL-based, add event-based for hot paths."""),

("system-design","Microservices vs Monolith","""When to use which architecture.

| Aspect | Monolith | Microservices |
|:---|:---|:---|
| Deployment | Single unit | Independent services |
| Scaling | Entire app | Per service |
| Complexity | Simple start | Complex infra |
| Team | Small (< 5) | Multiple teams |
| DB | Shared | Per service |
| Communication | Function calls | HTTP/gRPC/MQ |

### Start Monolith, Extract Later
> "Don't start with microservices. Start with a modular monolith. Extract services when you have clear domain boundaries."

### When Microservices Make Sense
- Large org with independent teams
- Services need different tech stacks
- Parts need independent scaling
- Clear domain boundaries (DDD)

**Key Takeaway**: Microservices solve organizational problems, not technical ones. If one team manages everything, stay monolith."""),

("system-design","Database Sharding","""Horizontal partitioning across multiple databases.

### Sharding Strategies
```
Hash-based:  shard = hash(user_id) % num_shards
Range-based: shard1=[A-M], shard2=[N-Z]
Geographic:  shard_us, shard_eu, shard_asia
```

### Challenges
- **Cross-shard queries**: JOINs across shards are expensive
- **Rebalancing**: Adding shards requires data migration
- **Hotspots**: Uneven data distribution
- **Distributed transactions**: 2PC is slow

### Consistent Hashing
```
Nodes on a ring: hash(nodeId) → position
Keys: hash(key) → find next node clockwise
Add/remove node: only nearby keys move!
```

**Key Takeaway**: Shard only when you MUST (100M+ rows, high write throughput). Try read replicas and caching first."""),

("system-design","Message Queues - Kafka vs RabbitMQ","""Async communication between services.

| Feature | Kafka | RabbitMQ |
|:---|:---|:---|
| Model | Distributed log | Message broker |
| Throughput | Millions/sec | Thousands/sec |
| Retention | Days/weeks | Until consumed |
| Ordering | Per partition | Per queue |
| Best for | Event streaming | Task queues |

### When to Use Queues
- Decouple services (order → email, inventory, analytics)
- Handle traffic spikes (buffer requests)
- Retry failed operations
- Event-driven architecture

### Kafka Producer (Spring Boot)
```java
@Service
public class OrderEventProducer {
    @Autowired KafkaTemplate<String, OrderEvent> kafka;
    
    public void publish(OrderEvent event) {
        kafka.send("order-events", event.getOrderId(), event);
    }
}
```

**Key Takeaway**: Kafka for event streaming and log aggregation. RabbitMQ for task queues and RPC patterns."""),

("system-design","API Design Best Practices","""Design clean, consistent REST APIs.

```
GET    /api/v1/users           List users
GET    /api/v1/users/123       Get user
POST   /api/v1/users           Create user
PUT    /api/v1/users/123       Full update
PATCH  /api/v1/users/123       Partial update
DELETE /api/v1/users/123       Delete user
GET    /api/v1/users/123/orders Nested resource
```

### HTTP Status Codes
| Code | Meaning |
|:---|:---|
| 200 | OK |
| 201 | Created |
| 204 | No Content (delete) |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 409 | Conflict |
| 429 | Rate Limited |
| 500 | Server Error |

### Rules
1. Nouns not verbs (`/users` not `/getUsers`)
2. Plural (`/users` not `/user`)
3. Version your API (`/v1/`)
4. Consistent error format
5. Pagination, filtering, sorting as query params"""),

# ═══════════════════════════════════════════════════════════════
# GIT — 10 topics
# ═══════════════════════════════════════════════════════════════
("git","Git Branching Strategies","""Organize team development with branching models.

### Git Flow
```
main ──────────────────────── production
  └─ develop ─────────────── integration
       ├─ feature/login ──── new feature
       ├─ feature/cart ────── new feature
       └─ release/1.0 ────── staging
  └─ hotfix/bug-123 ──────── urgent fix
```

### Trunk-Based Development
```
main ──────────────────────── always deployable
  ├─ short-lived branch (1-2 days max)
  └─ feature flags for incomplete features
```

| Strategy | Best For |
|:---|:---|
| Git Flow | Release-based products |
| Trunk-Based | CI/CD, SaaS, startups |
| GitHub Flow | Open source, simple |

**Key Takeaway**: Trunk-based is modern best practice. Keep branches short-lived (< 2 days). Use feature flags over long-lived branches."""),

("git","Git Rebase vs Merge","""Two ways to integrate changes.

```bash
# Merge: preserves complete history
git checkout main
git merge feature    # creates merge commit

# Rebase: linear history
git checkout feature
git rebase main      # replay commits on top of main

# Interactive rebase: clean up before merging
git rebase -i HEAD~3
# pick abc1234 Add user model
# squash def5678 Fix typo        ← combine with previous
# pick ghi9012 Add user API
```

### Golden Rule
> **Never rebase shared/public branches.** Only rebase YOUR local feature branch.

### My Workflow
1. Work on feature branch
2. `git rebase main` to get latest
3. `git rebase -i` to squash messy commits
4. Create PR with clean history

**Key Takeaway**: Rebase for clean history on YOUR branches. Merge for shared branches. Never force-push to main."""),

("git","Essential Git Commands","""Commands that save hours.

```bash
# Undo last commit (keep changes staged)
git reset --soft HEAD~1

# Unstage file
git restore --staged file.txt

# Discard local changes
git restore file.txt

# Stash with message
git stash push -m "WIP: feature"
git stash list
git stash pop stash@{0}

# Find which commit introduced a bug
git bisect start
git bisect bad           # current is broken
git bisect good abc123   # this was fine
# Git binary searches through history!

# Cherry-pick specific commit
git cherry-pick abc1234

# Pretty log
git log --oneline --graph --all -20

# See what changed
git diff --stat HEAD~5..HEAD
```"""),

# ═══════════════════════════════════════════════════════════════
# DEVOPS — 10 topics
# ═══════════════════════════════════════════════════════════════
("devops","Docker Multi-Stage Builds","""Reduce image size by separating build and runtime.

```dockerfile
# Stage 1: Build (800MB+)
FROM maven:3.9-eclipse-temurin-17 AS builder
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:resolve    # cache dependencies
COPY src ./src
RUN mvn clean package -DskipTests

# Stage 2: Run (200MB)
FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
COPY --from=builder /app/target/*.jar app.jar
EXPOSE 8080
HEALTHCHECK CMD curl -f http://localhost:8080/actuator/health || exit 1
ENTRYPOINT ["java", "-jar", "app.jar"]
```

**Benefits**: 75% smaller image, no build tools in production, faster deployments, smaller attack surface.

**Key Takeaway**: Always use multi-stage builds. Layer dependencies before source code (Docker cache optimization)."""),

("devops","Docker Compose for Development","""Multi-container development environment.

```yaml
version: '3.8'
services:
  app:
    build: .
    ports: ["8080:8080"]
    environment:
      SPRING_DATASOURCE_URL: jdbc:mysql://db:3306/myapp
    depends_on:
      db: { condition: service_healthy }
    volumes: ["./src:/app/src"]  # hot reload
  
  db:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: myapp
    ports: ["3306:3306"]
    volumes: ["mysql_data:/var/lib/mysql"]
    healthcheck:
      test: mysqladmin ping -h localhost
      interval: 10s
      retries: 5
  
  redis:
    image: redis:7-alpine
    ports: ["6379:6379"]

volumes:
  mysql_data:
```

```bash
docker-compose up -d     # start background
docker-compose logs -f   # follow logs
docker-compose down -v   # stop + remove volumes
```"""),

("devops","GitHub Actions CI/CD","""Automate testing and deployment.

```yaml
name: CI/CD Pipeline
on:
  push: { branches: [main] }
  pull_request: { branches: [main] }

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with: { java-version: '17', distribution: 'temurin' }
      - run: mvn test
      
  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: mvn package -DskipTests
      - uses: actions/upload-artifact@v4
        with: { name: app, path: target/*.jar }
  
  deploy:
    needs: build
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
        with: { name: app }
      - run: echo "Deploy to production"
```

**Key Takeaway**: Run tests on every PR. Deploy only from main. Use `needs` for job dependencies and `if` for conditional steps."""),
]

# Combine all topics
TOPICS = _BASE_TOPICS + EXTRA_TOPICS + EXTRA_TOPICS_2 + EXTRA_TOPICS_3


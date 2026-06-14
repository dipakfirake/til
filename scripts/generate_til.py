import json
import random
import os
import hashlib
from datetime import datetime, timezone, timedelta

TOPICS = [
    {
        "category": "java",
        "title": "HashMap vs ConcurrentHashMap",
        "content": """## HashMap vs ConcurrentHashMap in Java

`HashMap` is not thread-safe — if multiple threads modify it simultaneously, it can lead to data corruption or infinite loops.

`ConcurrentHashMap` solves this by using segment-level locking (Java 7) or CAS operations with synchronized blocks (Java 8+).

```java
// Not thread-safe
Map<String, Integer> map = new HashMap<>();

// Thread-safe alternative
Map<String, Integer> concurrentMap = new ConcurrentHashMap<>();
concurrentMap.put("key", 1);
concurrentMap.computeIfAbsent("key2", k -> 2);
```

### Key Differences
| Feature | HashMap | ConcurrentHashMap |
|:---|:---|:---|
| Thread Safety | No | Yes |
| Null Keys | Allowed (1) | Not Allowed |
| Performance (single thread) | Faster | Slightly slower |
| Locking | None | Segment/Bucket level |

### When to Use
- Use `HashMap` for single-threaded scenarios
- Use `ConcurrentHashMap` in multithreaded applications where you need concurrent reads/writes"""
    },
    {
        "category": "java",
        "title": "Java Stream API - reduce() vs collect()",
        "content": """## Java Stream API: reduce() vs collect()

Both are terminal operations in Java Streams, but serve different purposes.

### reduce() — Combines elements into a single value
```java
List<Integer> numbers = List.of(1, 2, 3, 4, 5);

// Sum using reduce
int sum = numbers.stream()
    .reduce(0, Integer::sum);
// Result: 15

// Find max
Optional<Integer> max = numbers.stream()
    .reduce(Integer::max);
```

### collect() — Gathers elements into a collection
```java
List<String> names = List.of("Alice", "Bob", "Charlie", "Alice");

// Collect to Set (removes duplicates)
Set<String> uniqueNames = names.stream()
    .collect(Collectors.toSet());

// Group by first letter
Map<Character, List<String>> grouped = names.stream()
    .collect(Collectors.groupingBy(s -> s.charAt(0)));
```

### Rule of Thumb
- Use `reduce()` when you need a **single value** (sum, max, concatenation)
- Use `collect()` when you need a **collection** (List, Set, Map)"""
    },
    {
        "category": "spring-boot",
        "title": "Spring Boot @Transactional Propagation Types",
        "content": """## Understanding @Transactional Propagation in Spring Boot

The `propagation` attribute defines how transactions relate to each other.

```java
@Service
public class OrderService {

    @Transactional(propagation = Propagation.REQUIRED) // Default
    public void createOrder(Order order) {
        // Joins existing transaction or creates new one
        orderRepository.save(order);
        paymentService.processPayment(order);
    }

    @Transactional(propagation = Propagation.REQUIRES_NEW)
    public void sendNotification(Order order) {
        // Always creates a NEW transaction
        // Even if called within an existing transaction
        notificationRepository.save(new Notification(order));
    }
}
```

### Common Propagation Types
| Type | Behavior |
|:---|:---|
| `REQUIRED` (default) | Join existing txn, or create new |
| `REQUIRES_NEW` | Always create new txn, suspend existing |
| `MANDATORY` | Must run within existing txn, else exception |
| `NEVER` | Must NOT run within a txn, else exception |
| `SUPPORTS` | Use txn if exists, else run without |

### Gotcha
`@Transactional` only works when called from **outside** the class. Internal method calls bypass the proxy!"""
    },
    {
        "category": "spring-boot",
        "title": "Spring Boot Custom Exception Handling with @ControllerAdvice",
        "content": """## Global Exception Handling in Spring Boot

Instead of handling exceptions in every controller, use `@ControllerAdvice` for centralized error handling.

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleNotFound(ResourceNotFoundException ex) {
        ErrorResponse error = new ErrorResponse(
            HttpStatus.NOT_FOUND.value(),
            ex.getMessage(),
            LocalDateTime.now()
        );
        return new ResponseEntity<>(error, HttpStatus.NOT_FOUND);
    }

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ErrorResponse> handleValidation(MethodArgumentNotValidException ex) {
        String message = ex.getBindingResult()
            .getFieldErrors()
            .stream()
            .map(e -> e.getField() + ": " + e.getDefaultMessage())
            .collect(Collectors.joining(", "));

        ErrorResponse error = new ErrorResponse(404, message, LocalDateTime.now());
        return new ResponseEntity<>(error, HttpStatus.BAD_REQUEST);
    }
}
```

This ensures all APIs return consistent error responses — critical for production applications."""
    },
    {
        "category": "react",
        "title": "React useCallback vs useMemo",
        "content": """## useCallback vs useMemo in React

Both are optimization hooks, but they memoize different things.

### useCallback — Memoizes a **function**
```jsx
const handleClick = useCallback(() => {
  console.log('Button clicked:', count);
}, [count]); // Re-creates only when count changes
```

### useMemo — Memoizes a **computed value**
```jsx
const expensiveResult = useMemo(() => {
  return items.filter(item => item.price > 100)
              .sort((a, b) => b.price - a.price);
}, [items]); // Re-computes only when items change
```

### When to Use
- `useCallback` → When passing callbacks to child components that use `React.memo()`
- `useMemo` → When you have expensive calculations that shouldn't run on every render

### Don't Overuse!
Premature optimization adds complexity. Only use when you **measure** a performance issue."""
    },
    {
        "category": "react",
        "title": "Custom Hooks - Extracting Reusable Logic",
        "content": """## Creating Custom Hooks in React

Custom hooks let you extract component logic into reusable functions.

```jsx
// useLocalStorage.js — Persist state in localStorage
function useLocalStorage(key, initialValue) {
  const [storedValue, setStoredValue] = useState(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      return initialValue;
    }
  });

  const setValue = (value) => {
    setStoredValue(value);
    window.localStorage.setItem(key, JSON.stringify(value));
  };

  return [storedValue, setValue];
}

// Usage in any component
function App() {
  const [theme, setTheme] = useLocalStorage('theme', 'dark');
  return <button onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}>
    Current: {theme}
  </button>;
}
```

### Rules of Custom Hooks
1. Name must start with `use`
2. Can call other hooks inside
3. Each call gets its own isolated state"""
    },
    {
        "category": "javascript",
        "title": "Promise.all vs Promise.allSettled vs Promise.race",
        "content": """## Promise Combinators in JavaScript

### Promise.all — Fails fast
```javascript
// All must succeed, or it rejects with the first failure
const results = await Promise.all([
  fetch('/api/users'),
  fetch('/api/posts'),
  fetch('/api/comments')
]);
// If any one fails, entire Promise.all rejects
```

### Promise.allSettled — Never fails
```javascript
// Waits for ALL to complete, reports each result
const results = await Promise.allSettled([
  fetch('/api/users'),
  fetch('/api/might-fail'),
]);
// results: [{status: 'fulfilled', value: ...}, {status: 'rejected', reason: ...}]
```

### Promise.race — First one wins
```javascript
// Returns result of whichever finishes first
const fastest = await Promise.race([
  fetch('/api/server1'),
  fetch('/api/server2'),
  new Promise((_, reject) => setTimeout(() => reject('Timeout'), 5000))
]);
```

### When to Use
| Combinator | Use Case |
|:---|:---|
| `Promise.all` | All results needed, fail if any fails |
| `Promise.allSettled` | Need all results regardless of failures |
| `Promise.race` | Timeout patterns, fastest response wins |"""
    },
    {
        "category": "javascript",
        "title": "Debounce vs Throttle - Performance Optimization",
        "content": """## Debounce vs Throttle in JavaScript

Both limit how often a function executes, but differently.

### Debounce — Waits for silence
```javascript
function debounce(fn, delay) {
  let timer;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}

// Usage: Search input — only fires after user stops typing
const searchInput = document.getElementById('search');
searchInput.addEventListener('input', debounce((e) => {
  fetchResults(e.target.value);
}, 300));
```

### Throttle — Fires at regular intervals
```javascript
function throttle(fn, limit) {
  let inThrottle = false;
  return function (...args) {
    if (!inThrottle) {
      fn.apply(this, args);
      inThrottle = true;
      setTimeout(() => (inThrottle = false), limit);
    }
  };
}

// Usage: Scroll handler — fires at most once every 200ms
window.addEventListener('scroll', throttle(() => {
  updateScrollPosition();
}, 200));
```

### Quick Reference
| | Debounce | Throttle |
|:---|:---|:---|
| Fires | After inactivity period | At regular intervals |
| Best for | Search input, resize | Scroll, mousemove |"""
    },
    {
        "category": "system-design",
        "title": "CAP Theorem Explained Simply",
        "content": """## CAP Theorem — The Trade-off Triangle

In a distributed system, you can only guarantee **2 out of 3**:

- **C**onsistency — Every read receives the most recent write
- **A**vailability — Every request receives a response
- **P**artition Tolerance — System works despite network failures

### Real-World Examples

| Database | Type | Trade-off |
|:---|:---|:---|
| MySQL, PostgreSQL | CP | Consistent, but may become unavailable during partition |
| Cassandra, DynamoDB | AP | Always available, but may serve stale data |
| MongoDB | CP (default) | Configurable, defaults to consistency |

### Why Not All Three?
When a network partition happens (and it **will** in distributed systems), you must choose:
- **CP**: Reject requests until partition heals (sacrifice availability)
- **AP**: Serve possibly stale data (sacrifice consistency)

### Practical Takeaway
- **Banking/Payments** → Choose CP (consistency matters)
- **Social Media Feed** → Choose AP (availability matters, slight staleness is OK)"""
    },
    {
        "category": "system-design",
        "title": "Database Indexing - How It Actually Works",
        "content": """## Database Indexing Internals

An index is like a book's table of contents — it helps the database find data without scanning every row.

### B-Tree Index (Most Common)
```sql
-- Without index: Full table scan — O(n)
SELECT * FROM users WHERE email = 'john@example.com';

-- Create index
CREATE INDEX idx_email ON users(email);

-- With index: B-Tree lookup — O(log n)
SELECT * FROM users WHERE email = 'john@example.com';
```

### When Indexes Help
- `WHERE` clauses
- `JOIN` conditions
- `ORDER BY` and `GROUP BY`

### When Indexes Hurt
- Tables with heavy `INSERT/UPDATE/DELETE` (index must be updated)
- Small tables (full scan is faster than index lookup)
- Columns with low cardinality (e.g., boolean `is_active`)

### Composite Index Rule
```sql
-- Index on (A, B, C) supports:
-- WHERE A = ?            ✓
-- WHERE A = ? AND B = ?  ✓
-- WHERE B = ?            ✗ (leftmost prefix rule!)
```

**Golden rule**: Index columns you **filter** and **sort** by most frequently."""
    },
    {
        "category": "dsa",
        "title": "Two Pointer Technique for Array Problems",
        "content": """## Two Pointer Technique

One of the most powerful patterns for array/string problems. Reduces O(n²) brute force to O(n).

### Pattern 1: Opposite Ends (Sorted Array)
```java
// Two Sum in Sorted Array
public int[] twoSum(int[] nums, int target) {
    int left = 0, right = nums.length - 1;
    while (left < right) {
        int sum = nums[left] + nums[right];
        if (sum == target) return new int[]{left, right};
        else if (sum < target) left++;
        else right--;
    }
    return new int[]{-1, -1};
}
```

### Pattern 2: Same Direction (Fast & Slow)
```java
// Remove duplicates from sorted array — in place
public int removeDuplicates(int[] nums) {
    int slow = 0;
    for (int fast = 1; fast < nums.length; fast++) {
        if (nums[fast] != nums[slow]) {
            slow++;
            nums[slow] = nums[fast];
        }
    }
    return slow + 1;
}
```

### When to Use Two Pointers
- Sorted arrays with pair/triplet finding
- Removing duplicates in-place
- Palindrome checking
- Container with most water
- Merging sorted arrays"""
    },
    {
        "category": "dsa",
        "title": "Sliding Window Pattern",
        "content": """## Sliding Window — Subarray/Substring Problems

Used when you need to find a contiguous subarray/substring that satisfies a condition.

### Fixed Window: Max sum of k consecutive elements
```java
public int maxSumSubarray(int[] arr, int k) {
    int windowSum = 0, maxSum = 0;

    for (int i = 0; i < arr.length; i++) {
        windowSum += arr[i];
        if (i >= k) windowSum -= arr[i - k]; // Slide: remove leftmost
        if (i >= k - 1) maxSum = Math.max(maxSum, windowSum);
    }
    return maxSum;
}
```

### Variable Window: Longest substring without repeating chars
```java
public int lengthOfLongestSubstring(String s) {
    Set<Character> window = new HashSet<>();
    int left = 0, maxLen = 0;

    for (int right = 0; right < s.length(); right++) {
        while (window.contains(s.charAt(right))) {
            window.remove(s.charAt(left));
            left++;
        }
        window.add(s.charAt(right));
        maxLen = Math.max(maxLen, right - left + 1);
    }
    return maxLen;
}
```

### Identifying Sliding Window Problems
Keywords: "contiguous", "subarray", "substring", "window of size k", "maximum/minimum" in a range."""
    },
    {
        "category": "dotnet",
        "title": "Dependency Injection in ASP.NET Core",
        "content": """## Dependency Injection in ASP.NET Core

ASP.NET Core has DI built into the framework — no third-party container needed.

### Service Lifetimes
```csharp
var builder = WebApplication.CreateBuilder(args);

// Transient — New instance every time it's requested
builder.Services.AddTransient<IEmailService, EmailService>();

// Scoped — One instance per HTTP request
builder.Services.AddScoped<IOrderService, OrderService>();

// Singleton — One instance for the entire app lifetime
builder.Services.AddSingleton<ICacheService, CacheService>();
```

### Constructor Injection
```csharp
[ApiController]
[Route("api/[controller]")]
public class OrdersController : ControllerBase
{
    private readonly IOrderService _orderService;
    private readonly ILogger<OrdersController> _logger;

    // Dependencies injected via constructor
    public OrdersController(IOrderService orderService, ILogger<OrdersController> logger)
    {
        _orderService = orderService;
        _logger = logger;
    }

    [HttpGet("{id}")]
    public async Task<IActionResult> Get(int id)
    {
        var order = await _orderService.GetByIdAsync(id);
        return order == null ? NotFound() : Ok(order);
    }
}
```

### Choosing the Right Lifetime
| Lifetime | Use Case |
|:---|:---|
| Transient | Lightweight, stateless services |
| Scoped | Database contexts, per-request data |
| Singleton | Caching, configuration, HTTP clients |"""
    },
    {
        "category": "dotnet",
        "title": "Entity Framework Core - Eager vs Lazy vs Explicit Loading",
        "content": """## EF Core Loading Strategies

### Eager Loading — Load related data upfront
```csharp
// Include related entities in the query
var orders = await context.Orders
    .Include(o => o.Customer)
    .Include(o => o.OrderItems)
        .ThenInclude(oi => oi.Product)
    .ToListAsync();
```

### Lazy Loading — Load on access (be careful!)
```csharp
// Requires Microsoft.EntityFrameworkCore.Proxies
// Navigation properties loaded when first accessed
var order = await context.Orders.FindAsync(1);
var customer = order.Customer; // DB query happens HERE
```

### Explicit Loading — Load manually when needed
```csharp
var order = await context.Orders.FindAsync(1);

// Explicitly load related data
await context.Entry(order)
    .Reference(o => o.Customer)
    .LoadAsync();

await context.Entry(order)
    .Collection(o => o.OrderItems)
    .LoadAsync();
```

### Which to Choose?
| Strategy | Pros | Cons |
|:---|:---|:---|
| Eager | Predictable, fewer queries | May load too much data |
| Lazy | Simple code | N+1 query problem! |
| Explicit | Full control | Verbose code |

**Best Practice**: Default to **Eager Loading**, avoid Lazy Loading in production."""
    },
    {
        "category": "database",
        "title": "SQL JOIN Types Visual Guide",
        "content": """## SQL JOIN Types — When to Use Each

### INNER JOIN — Only matching rows
```sql
SELECT u.name, o.total
FROM users u
INNER JOIN orders o ON u.id = o.user_id;
-- Returns only users who have orders
```

### LEFT JOIN — All from left + matching from right
```sql
SELECT u.name, COALESCE(COUNT(o.id), 0) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.name;
-- Returns ALL users, even those without orders
```

### RIGHT JOIN — All from right + matching from left
```sql
SELECT u.name, o.total
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
-- Returns ALL orders, even orphaned ones
```

### FULL OUTER JOIN — Everything from both
```sql
SELECT u.name, o.total
FROM users u
FULL OUTER JOIN orders o ON u.id = o.user_id;
-- Returns all users AND all orders
```

### Performance Tip
Always ensure JOIN columns are indexed:
```sql
CREATE INDEX idx_orders_user_id ON orders(user_id);
```"""
    },
    {
        "category": "database",
        "title": "SQL Query Optimization Checklist",
        "content": """## SQL Query Optimization — Quick Checklist

### 1. Use EXPLAIN to analyze queries
```sql
EXPLAIN ANALYZE SELECT * FROM orders WHERE status = 'pending';
-- Look for: Seq Scan (bad) vs Index Scan (good)
```

### 2. Avoid SELECT * in production
```sql
-- Bad: fetches ALL columns
SELECT * FROM users;

-- Good: fetch only what you need
SELECT id, name, email FROM users;
```

### 3. Use EXISTS instead of IN for subqueries
```sql
-- Slower with large datasets
SELECT * FROM users WHERE id IN (SELECT user_id FROM orders);

-- Faster: stops at first match
SELECT * FROM users u WHERE EXISTS (
    SELECT 1 FROM orders o WHERE o.user_id = u.id
);
```

### 4. Pagination with OFFSET is slow for large pages
```sql
-- Slow for page 1000
SELECT * FROM posts ORDER BY id LIMIT 20 OFFSET 20000;

-- Faster: cursor-based pagination
SELECT * FROM posts WHERE id > 20000 ORDER BY id LIMIT 20;
```

### 5. Batch INSERT instead of single rows
```sql
-- Slow: 1000 round trips
INSERT INTO logs (msg) VALUES ('a');
INSERT INTO logs (msg) VALUES ('b');

-- Fast: 1 round trip
INSERT INTO logs (msg) VALUES ('a'), ('b'), ('c'), ...;
```"""
    },
    {
        "category": "git",
        "title": "Git Rebase vs Merge - When to Use Which",
        "content": """## Git Rebase vs Merge

### Merge — Preserves history
```bash
git checkout main
git merge feature-branch
# Creates a merge commit, preserves branch history
```

### Rebase — Linear history
```bash
git checkout feature-branch
git rebase main
# Replays your commits on top of main — clean, linear history
```

### Golden Rule
> **Never rebase public/shared branches.** Only rebase your local feature branches.

### Interactive Rebase — Clean up before merging
```bash
git rebase -i HEAD~3
# pick abc1234 Add user model
# squash def5678 Fix typo in user model
# pick ghi9012 Add user API endpoint
# Combines the typo fix into the first commit
```

### My Workflow
1. Work on feature branch
2. `git rebase main` to get latest changes
3. `git rebase -i` to squash/clean commits
4. Create PR with clean history"""
    },
    {
        "category": "git",
        "title": "Useful Git Commands I Use Daily",
        "content": """## Git Commands That Save Time

### Undo last commit (keep changes)
```bash
git reset --soft HEAD~1
```

### See what changed in a file
```bash
git diff HEAD~1 -- path/to/file.java
```

### Stash with a message
```bash
git stash push -m "WIP: half-done feature"
git stash list
git stash pop stash@{0}
```

### Find which commit broke something
```bash
git bisect start
git bisect bad          # current commit is broken
git bisect good abc123  # this old commit was fine
# Git will binary search through commits
```

### Cherry-pick a specific commit
```bash
git cherry-pick abc1234
# Applies just that one commit to current branch
```

### View pretty log
```bash
git log --oneline --graph --all --decorate -20
```

### Clean up merged branches
```bash
git branch --merged | grep -v main | xargs git branch -d
```"""
    },
    {
        "category": "devops",
        "title": "Docker Multi-Stage Builds for Java Apps",
        "content": """## Docker Multi-Stage Builds

Reduces image size dramatically by separating build and runtime.

### Without Multi-Stage (800MB+)
```dockerfile
FROM maven:3.9-eclipse-temurin-17
COPY . .
RUN mvn clean package -DskipTests
CMD ["java", "-jar", "target/app.jar"]
# Image includes Maven, source code, build tools — huge!
```

### With Multi-Stage (200MB)
```dockerfile
# Stage 1: Build
FROM maven:3.9-eclipse-temurin-17 AS builder
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:resolve
COPY src ./src
RUN mvn clean package -DskipTests

# Stage 2: Run
FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
COPY --from=builder /app/target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

### Benefits
- **75% smaller** image size
- No build tools in production image
- Faster deployments and pulls
- Smaller attack surface (security)"""
    },
    {
        "category": "spring-boot",
        "title": "Spring Boot Profiles for Environment Configuration",
        "content": """## Managing Environments with Spring Profiles

### Define profile-specific configs

**application-dev.yml**
```yaml
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/myapp_dev
    username: root
    password: root
  jpa:
    show-sql: true
```

**application-prod.yml**
```yaml
spring:
  datasource:
    url: jdbc:mysql://prod-server:3306/myapp
    username: ${DB_USER}
    password: ${DB_PASS}
  jpa:
    show-sql: false
```

### Activate a profile
```bash
# Command line
java -jar app.jar --spring.profiles.active=prod

# Environment variable
export SPRING_PROFILES_ACTIVE=prod

# In application.yml
spring:
  profiles:
    active: dev
```

### Profile-specific beans
```java
@Configuration
@Profile("dev")
public class DevConfig {
    @Bean
    public DataSource dataSource() {
        return new EmbeddedDatabaseBuilder()
            .setType(EmbeddedDatabaseType.H2)
            .build();
    }
}
```"""
    },
    {
        "category": "java",
        "title": "Java Optional - Avoiding NullPointerException",
        "content": """## Using Optional to Avoid NullPointerException

### Anti-Pattern: Null checks everywhere
```java
// Ugly and error-prone
User user = userRepository.findById(id);
if (user != null) {
    Address address = user.getAddress();
    if (address != null) {
        return address.getCity();
    }
}
return "Unknown";
```

### Better: Optional chaining
```java
String city = userRepository.findById(id)    // Returns Optional<User>
    .map(User::getAddress)
    .map(Address::getCity)
    .orElse("Unknown");
```

### Common Optional Methods
```java
Optional<User> opt = Optional.ofNullable(user);

opt.isPresent();                    // Check if value exists
opt.ifPresent(u -> log(u));         // Execute if present
opt.orElse(defaultUser);            // Fallback value
opt.orElseThrow(() -> new NotFoundException("User not found"));
opt.filter(u -> u.isActive());      // Conditional filter
opt.map(User::getName);             // Transform value
```

### Rules
- Never use `Optional` as a method parameter or field
- Use it as a **return type** to signal "might be empty"
- Never call `.get()` without checking `.isPresent()` first"""
    },
    {
        "category": "react",
        "title": "React Context API vs Redux - When to Choose What",
        "content": """## Context API vs Redux

### Context API — Built-in, simple
```jsx
const ThemeContext = createContext('light');

function App() {
  const [theme, setTheme] = useState('dark');
  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      <Dashboard />
    </ThemeContext.Provider>
  );
}

function Dashboard() {
  const { theme, setTheme } = useContext(ThemeContext);
  return <button onClick={() => setTheme('light')}>{theme}</button>;
}
```

### When to Use Context
- Theme, locale, auth state
- Data that doesn't change frequently
- Small to medium apps

### When to Use Redux
- Complex state with many updates
- State shared across many unrelated components
- Need middleware (logging, async, undo/redo)
- Large applications with multiple developers

### Rule of Thumb
> Start with Context + useReducer. Move to Redux only when Context re-renders become a problem."""
    },
    {
        "category": "system-design",
        "title": "Rate Limiting Strategies",
        "content": """## Rate Limiting — Protecting Your APIs

### Why Rate Limit?
- Prevent abuse and DDoS attacks
- Fair usage across users
- Protect downstream services

### Token Bucket Algorithm
```
Bucket capacity: 10 tokens
Refill rate: 1 token/second

Request comes in:
  - If tokens > 0: Allow request, remove 1 token
  - If tokens == 0: Reject (429 Too Many Requests)
```

### Implementation in Spring Boot
```java
@Component
public class RateLimitFilter extends OncePerRequestFilter {
    private final Map<String, Bucket> buckets = new ConcurrentHashMap<>();

    private Bucket createBucket() {
        return Bucket.builder()
            .addLimit(Bandwidth.classic(10, Refill.greedy(10, Duration.ofMinutes(1))))
            .build();
    }

    @Override
    protected void doFilterInternal(HttpServletRequest req,
            HttpServletResponse res, FilterChain chain) {
        String ip = req.getRemoteAddr();
        Bucket bucket = buckets.computeIfAbsent(ip, k -> createBucket());

        if (bucket.tryConsume(1)) {
            chain.doFilter(req, res);
        } else {
            res.setStatus(429);
            res.getWriter().write("Rate limit exceeded");
        }
    }
}
```

### Common Strategies
| Algorithm | Best For |
|:---|:---|
| Token Bucket | Smooth rate limiting with burst allowance |
| Fixed Window | Simple, easy to implement |
| Sliding Window | Most accurate, prevents boundary issues |"""
    },
    {
        "category": "dsa",
        "title": "Binary Search Beyond Sorted Arrays",
        "content": """## Binary Search — Not Just for Sorted Arrays

### Classic Binary Search
```java
public int binarySearch(int[] nums, int target) {
    int lo = 0, hi = nums.length - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;  // Prevents overflow
        if (nums[mid] == target) return mid;
        else if (nums[mid] < target) lo = mid + 1;
        else hi = mid - 1;
    }
    return -1;
}
```

### Binary Search on Answer
Find minimum capacity to ship packages in D days:
```java
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

private boolean canShip(int[] weights, int days, int capacity) {
    int currentLoad = 0, daysNeeded = 1;
    for (int w : weights) {
        if (currentLoad + w > capacity) {
            daysNeeded++;
            currentLoad = 0;
        }
        currentLoad += w;
    }
    return daysNeeded <= days;
}
```

### When to Think Binary Search
- "Find minimum/maximum value that satisfies condition"
- Monotonic function (if X works, X+1 also works)
- Search space can be halved each step"""
    },
    {
        "category": "javascript",
        "title": "JavaScript Event Loop Explained",
        "content": """## The Event Loop — Why JS is Single-Threaded But Non-Blocking

```javascript
console.log('1');                    // Synchronous

setTimeout(() => {
  console.log('2');                  // Macro task
}, 0);

Promise.resolve().then(() => {
  console.log('3');                  // Micro task
});

console.log('4');                    // Synchronous

// Output: 1, 4, 3, 2
```

### Execution Order
1. **Call Stack** — Runs synchronous code (1, 4)
2. **Microtask Queue** — Promises, queueMicrotask (3)
3. **Macrotask Queue** — setTimeout, setInterval, I/O (2)

### Why Does This Matter?
```javascript
// This BLOCKS the main thread!
while (true) { /* infinite loop */ }

// This does NOT block — it's async
setInterval(() => checkForUpdates(), 1000);
```

### Key Takeaway
Microtasks (Promises) always run before macrotasks (setTimeout), even if setTimeout has a 0ms delay."""
    }
]

COMMIT_PREFIXES = [
    "til: ",
    "learn: ",
    "notes: ",
    "study: ",
    "docs: ",
]

def get_today_topic(topics):
    ist = timezone(timedelta(hours=5, minutes=30))
    today = datetime.now(ist).strftime("%Y-%m-%d")
    seed = int(hashlib.md5(today.encode()).hexdigest(), 16)
    random.seed(seed)
    return random.choice(topics)

def create_til_entry(topic):
    ist = timezone(timedelta(hours=5, minutes=30))
    today = datetime.now(ist)
    date_str = today.strftime("%Y-%m-%d")
    
    category = topic["category"]
    title = topic["title"]
    content = topic["content"].strip()
    
    category_dir = os.path.join(os.getcwd(), category)
    os.makedirs(category_dir, exist_ok=True)
    
    safe_title = title.lower().replace(" ", "-").replace("/", "-").replace("(", "").replace(")", "").replace("---", "-").replace("--", "-")
    filename = f"{date_str}-{safe_title}.md"
    filepath = os.path.join(category_dir, filename)
    
    if os.path.exists(filepath):
        print(f"Already exists: {filepath}")
        return None, None
    
    header = f"# {title}\n\n_{date_str}_\n\n"
    full_content = header + content + "\n"
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(full_content)
    
    prefix = random.choice(COMMIT_PREFIXES)
    commit_msg = f"{prefix}{title}"
    
    return filepath, commit_msg

def main():
    topic = get_today_topic(TOPICS)
    filepath, commit_msg = create_til_entry(topic)
    
    if filepath:
        print(f"Created: {filepath}")
        print(f"COMMIT_MSG={commit_msg}")
        with open(os.environ.get("GITHUB_OUTPUT", "/dev/null"), "a") as f:
            f.write(f"commit_msg={commit_msg}\n")
            f.write(f"has_new=true\n")
    else:
        with open(os.environ.get("GITHUB_OUTPUT", "/dev/null"), "a") as f:
            f.write(f"has_new=false\n")

if __name__ == "__main__":
    main()

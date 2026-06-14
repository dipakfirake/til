# Additional 250 topics to reach 365+ total
# Categories: java, spring-boot, dotnet, react, javascript, typescript,
#             html-css, nodejs, mongodb, database, dsa, system-design, git, devops, python

EXTRA_TOPICS = [
# ═══════════════════════════════════════════════════════════════
# MORE JAVA (9 more → 50 total)
# ═══════════════════════════════════════════════════════════════
("java","Java Memory Model and volatile","""How threads see shared memory.

```java
// Without volatile: thread may cache stale value
private volatile boolean running = true;

// Thread A
new Thread(() -> {
    while (running) { doWork(); } // reads latest value
}).start();

// Thread B
running = false; // visible to Thread A immediately

// Happens-Before Rules:
// 1. volatile write → subsequent volatile read
// 2. synchronized unlock → subsequent lock
// 3. Thread.start() → first action in started thread
// 4. Thread action → Thread.join() return
```

**Key Takeaway**: `volatile` guarantees visibility across threads but NOT atomicity. Use `AtomicInteger` for atomic read-modify-write."""),

("java","Java Class Loading Mechanism","""How JVM loads classes on demand.

```
ClassLoader Hierarchy:
┌───────────────────┐
│ Bootstrap Loader  │ ← java.lang, java.util (rt.jar)
├───────────────────┤
│ Extension Loader  │ ← javax.*, ext directory
├───────────────────┤
│ Application Loader│ ← classpath (your code)
├───────────────────┤
│ Custom Loaders    │ ← plugins, hot-reload
└───────────────────┘
```

```java
// Check which classloader loaded a class
System.out.println(String.class.getClassLoader());      // null (Bootstrap)
System.out.println(MyClass.class.getClassLoader());     // AppClassLoader

// Custom classloader for plugins
ClassLoader loader = new URLClassLoader(new URL[]{pluginJar});
Class<?> cls = loader.loadClass("com.plugin.MyPlugin");
Object plugin = cls.getDeclaredConstructor().newInstance();
```

**Delegation**: Child asks parent first → loads only if parent can't.
**Key Takeaway**: Understanding classloading helps debug `ClassNotFoundException` and `NoClassDefFoundError`."""),

("java","Java WeakReference and SoftReference","""Control garbage collection behavior.

```java
// Strong reference — never GC'd while reachable
Object obj = new Object();

// Weak reference — GC'd at next collection
WeakReference<BigObject> weak = new WeakReference<>(new BigObject());
BigObject obj = weak.get(); // may return null!

// Soft reference — GC'd only when memory is low
SoftReference<byte[]> cache = new SoftReference<>(loadLargeData());

// WeakHashMap — entries removed when key is GC'd
Map<Key, Value> cache = new WeakHashMap<>();
// Perfect for caches that shouldn't prevent GC

// Example: image cache
private final Map<String, SoftReference<BufferedImage>> imageCache = new HashMap<>();

public BufferedImage getImage(String path) {
    SoftReference<BufferedImage> ref = imageCache.get(path);
    BufferedImage img = (ref != null) ? ref.get() : null;
    if (img == null) {
        img = loadImage(path);
        imageCache.put(path, new SoftReference<>(img));
    }
    return img;
}
```

**Key Takeaway**: WeakReference = temporary associations. SoftReference = memory-sensitive caches. Both help prevent memory leaks."""),

("java","Java Concurrency - ReentrantLock","""More flexible than synchronized.

```java
private final ReentrantLock lock = new ReentrantLock();
private final Condition notFull = lock.newCondition();
private final Condition notEmpty = lock.newCondition();

public void put(T item) throws InterruptedException {
    lock.lock();
    try {
        while (isFull()) notFull.await();
        add(item);
        notEmpty.signal();
    } finally {
        lock.unlock(); // ALWAYS in finally!
    }
}

// Try lock with timeout
if (lock.tryLock(5, TimeUnit.SECONDS)) {
    try { /* critical section */ }
    finally { lock.unlock(); }
} else {
    log.warn("Could not acquire lock");
}

// Fair lock (FIFO ordering)
ReentrantLock fairLock = new ReentrantLock(true);
```

| Feature | synchronized | ReentrantLock |
|:---|:---|:---|
| tryLock | No | Yes |
| Timeout | No | Yes |
| Fair ordering | No | Yes |
| Multiple conditions | No | Yes |"""),

("java","Java Stream Collectors","""Advanced collection operations.

```java
List<Employee> employees = getEmployees();

// Group by department
Map<String, List<Employee>> byDept = employees.stream()
    .collect(Collectors.groupingBy(Employee::getDept));

// Group and count
Map<String, Long> deptCounts = employees.stream()
    .collect(Collectors.groupingBy(Employee::getDept, Collectors.counting()));

// Group and sum salaries
Map<String, Double> deptSalaries = employees.stream()
    .collect(Collectors.groupingBy(Employee::getDept, Collectors.summingDouble(Employee::getSalary)));

// Partition (split into two groups)
Map<Boolean, List<Employee>> partition = employees.stream()
    .collect(Collectors.partitioningBy(e -> e.getSalary() > 50000));

// Join strings
String names = employees.stream()
    .map(Employee::getName)
    .collect(Collectors.joining(", ", "[", "]")); // [Alice, Bob, Charlie]

// Statistics
DoubleSummaryStatistics stats = employees.stream()
    .collect(Collectors.summarizingDouble(Employee::getSalary));
// stats.getAverage(), stats.getMax(), stats.getCount()
```"""),

("java","Java Design Pattern - Decorator","""Add behavior dynamically without changing original class.

```java
public interface Coffee {
    double cost();
    String description();
}

public class BasicCoffee implements Coffee {
    public double cost() { return 50; }
    public String description() { return "Basic Coffee"; }
}

// Decorator
public abstract class CoffeeDecorator implements Coffee {
    protected final Coffee coffee;
    public CoffeeDecorator(Coffee c) { this.coffee = c; }
}

public class Milk extends CoffeeDecorator {
    public Milk(Coffee c) { super(c); }
    public double cost() { return coffee.cost() + 15; }
    public String description() { return coffee.description() + " + Milk"; }
}

public class Whip extends CoffeeDecorator {
    public Whip(Coffee c) { super(c); }
    public double cost() { return coffee.cost() + 25; }
    public String description() { return coffee.description() + " + Whip"; }
}

// Stack decorators
Coffee order = new Whip(new Milk(new BasicCoffee()));
System.out.println(order.description()); // Basic Coffee + Milk + Whip
System.out.println(order.cost());        // 90
```

**Key Takeaway**: Decorator = wrapper classes. Used in Java I/O streams (BufferedReader wraps FileReader)."""),

("java","Java Design Pattern - Adapter","""Make incompatible interfaces work together.

```java
// Existing legacy code (can't modify)
public class LegacyPayment {
    public void makePayment(String xml) {
        // processes XML payment
    }
}

// New interface your app uses
public interface PaymentProcessor {
    void pay(PaymentRequest request);
}

// Adapter bridges the gap
public class LegacyPaymentAdapter implements PaymentProcessor {
    private final LegacyPayment legacy;
    
    public LegacyPaymentAdapter(LegacyPayment legacy) {
        this.legacy = legacy;
    }
    
    @Override
    public void pay(PaymentRequest request) {
        String xml = convertToXml(request);
        legacy.makePayment(xml);
    }
    
    private String convertToXml(PaymentRequest req) {
        return "<payment><amount>" + req.getAmount() + "</amount></payment>";
    }
}

// Usage
PaymentProcessor processor = new LegacyPaymentAdapter(new LegacyPayment());
processor.pay(new PaymentRequest(500, "INR"));
```

**Key Takeaway**: Adapter wraps old code to match new interface. Common in integrations with legacy systems and third-party libraries."""),

("java","Java Design Pattern - Singleton","""Ensure only one instance exists.

```java
// 1. Enum Singleton (BEST — thread-safe, serialization-safe)
public enum DatabasePool {
    INSTANCE;
    private final HikariDataSource ds;
    DatabasePool() { ds = new HikariDataSource(config()); }
    public Connection getConnection() throws SQLException { return ds.getConnection(); }
}

// 2. Double-Checked Locking
public class Singleton {
    private static volatile Singleton instance;
    private Singleton() {}
    public static Singleton getInstance() {
        if (instance == null) {
            synchronized (Singleton.class) {
                if (instance == null) instance = new Singleton();
            }
        }
        return instance;
    }
}

// 3. Holder Pattern (lazy, thread-safe)
public class Config {
    private Config() {}
    private static class Holder { static final Config INSTANCE = new Config(); }
    public static Config getInstance() { return Holder.INSTANCE; }
}
```

**Key Takeaway**: Use Enum singleton for new code. In Spring, all beans are singletons by default — don't create your own."""),

("java","Java Concurrent Collections","""Thread-safe collections beyond ConcurrentHashMap.

```java
// CopyOnWriteArrayList — reads never block
CopyOnWriteArrayList<String> list = new CopyOnWriteArrayList<>();
// Great for: many reads, rare writes (event listeners)

// BlockingQueue — producer-consumer
BlockingQueue<Task> queue = new LinkedBlockingQueue<>(100);
queue.put(task);    // blocks if full
Task t = queue.take(); // blocks if empty

// ConcurrentLinkedQueue — non-blocking FIFO
ConcurrentLinkedQueue<Event> events = new ConcurrentLinkedQueue<>();
events.offer(event); // never blocks

// CountDownLatch — wait for N tasks
CountDownLatch latch = new CountDownLatch(3);
// Each task calls: latch.countDown();
latch.await(); // waits for all 3

// CyclicBarrier — N threads wait for each other
CyclicBarrier barrier = new CyclicBarrier(3, () -> System.out.println("All arrived!"));
// Each thread calls: barrier.await();
```

| Collection | Use Case |
|:---|:---|
| ConcurrentHashMap | Thread-safe map |
| CopyOnWriteArrayList | Read-heavy lists |
| BlockingQueue | Producer-consumer |
| ConcurrentSkipListMap | Sorted concurrent map |"""),

# ═══════════════════════════════════════════════════════════════
# MORE SPRING BOOT (19 more → 40 total)
# ═══════════════════════════════════════════════════════════════
("spring-boot","Spring Boot Logging Best Practices","""Structured logging with SLF4J and Logback.

```java
@Service
@Slf4j // Lombok
public class OrderService {
    public Order createOrder(CreateOrderRequest req) {
        log.info("Creating order for user={} items={}", req.getUserId(), req.getItems().size());
        try {
            Order order = processOrder(req);
            log.info("Order created orderId={} total={}", order.getId(), order.getTotal());
            return order;
        } catch (Exception e) {
            log.error("Failed to create order userId={}", req.getUserId(), e);
            throw e;
        }
    }
}
```

```yaml
# application.yml
logging:
  level:
    root: INFO
    com.myapp: DEBUG
    org.hibernate.SQL: DEBUG
  pattern:
    console: "%d{HH:mm:ss} [%thread] %-5level %logger{36} - %msg%n"
  file:
    name: logs/app.log
```

**Key Takeaway**: Use `{}` placeholders, not string concatenation (avoids building string when log level is off). Include context (userId, orderId) in every log."""),

("spring-boot","Spring Boot Custom Annotations","""Create reusable meta-annotations.

```java
// Combine multiple annotations into one
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
@PreAuthorize("hasRole('ADMIN')")
@Cacheable(value = "adminData", key = "#id")
@Transactional(readOnly = true)
public @interface AdminReadOnly {}

// Usage
@AdminReadOnly
public Dashboard getDashboard(Long id) { return dashboardRepo.findById(id); }

// Rate limiting annotation
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface RateLimit {
    int requests() default 100;
    int seconds() default 60;
}

@Aspect @Component
public class RateLimitAspect {
    @Around("@annotation(limit)")
    public Object enforce(ProceedingJoinPoint jp, RateLimit limit) throws Throwable {
        String key = jp.getSignature().toShortString();
        if (isRateLimited(key, limit.requests(), limit.seconds()))
            throw new TooManyRequestsException();
        return jp.proceed();
    }
}
```"""),

("spring-boot","Spring Events - Loose Coupling","""Publish/subscribe within your application.

```java
// Event
public record OrderCreatedEvent(Long orderId, Long userId, BigDecimal total) {}

// Publisher
@Service
public class OrderService {
    @Autowired private ApplicationEventPublisher publisher;
    
    @Transactional
    public Order create(CreateOrderRequest req) {
        Order order = orderRepo.save(buildOrder(req));
        publisher.publishEvent(new OrderCreatedEvent(order.getId(), req.getUserId(), order.getTotal()));
        return order;
    }
}

// Listeners (decoupled!)
@Component
public class EmailListener {
    @EventListener
    public void onOrderCreated(OrderCreatedEvent event) {
        emailService.sendConfirmation(event.userId(), event.orderId());
    }
}

@Component
public class InventoryListener {
    @Async @EventListener  // runs in separate thread
    public void onOrderCreated(OrderCreatedEvent event) {
        inventoryService.reserve(event.orderId());
    }
}
```

**Key Takeaway**: Events decouple services without message brokers. Use `@Async` for non-critical listeners to avoid slowing down the main flow."""),

("spring-boot","Spring Boot API Versioning","""Manage breaking changes in APIs.

```java
// 1. URL versioning (most common)
@RestController @RequestMapping("/api/v1/users")
public class UserControllerV1 {
    @GetMapping("/{id}") public UserV1Response get(@PathVariable Long id) { }
}

@RestController @RequestMapping("/api/v2/users")
public class UserControllerV2 {
    @GetMapping("/{id}") public UserV2Response get(@PathVariable Long id) { }
}

// 2. Header versioning
@GetMapping(value = "/{id}", headers = "X-API-Version=2")
public UserV2Response getV2(@PathVariable Long id) { }

// 3. Content negotiation
@GetMapping(value = "/{id}", produces = "application/vnd.myapp.v2+json")
public UserV2Response getV2(@PathVariable Long id) { }
```

| Strategy | Pros | Cons |
|:---|:---|:---|
| URL `/v1/` | Simple, clear | URL changes |
| Header | Clean URLs | Hidden |
| Content-Type | REST purist | Complex |

**Key Takeaway**: URL versioning is simplest and most common. Version your DTOs, not your entities."""),

("spring-boot","Spring Security - OAuth2 Resource Server","""Validate JWT tokens from auth providers.

```yaml
spring:
  security:
    oauth2:
      resourceserver:
        jwt:
          issuer-uri: https://auth.example.com/
```

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        return http
            .csrf(csrf -> csrf.disable())
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/api/public/**").permitAll()
                .requestMatchers("/api/admin/**").hasRole("ADMIN")
                .anyRequest().authenticated()
            )
            .oauth2ResourceServer(oauth -> oauth.jwt(Customizer.withDefaults()))
            .sessionManagement(s -> s.sessionCreationPolicy(SessionCreationPolicy.STATELESS))
            .build();
    }
}

// Access user info in controller
@GetMapping("/me")
public Map<String,Object> me(@AuthenticationPrincipal Jwt jwt) {
    return Map.of("sub", jwt.getSubject(), "email", jwt.getClaimAsString("email"));
}
```"""),

("spring-boot","Spring Boot Integration Testing","""Test full application context.

```java
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@AutoConfigureMockMvc
class OrderIntegrationTest {
    @Autowired MockMvc mvc;
    @Autowired ObjectMapper mapper;
    @Autowired OrderRepository orderRepo;
    
    @BeforeEach
    void setup() { orderRepo.deleteAll(); }
    
    @Test
    void shouldCreateAndRetrieveOrder() throws Exception {
        var req = new CreateOrderRequest("user1", List.of(new Item("Laptop",999)));
        
        // Create
        String response = mvc.perform(post("/api/orders")
                .contentType(MediaType.APPLICATION_JSON)
                .content(mapper.writeValueAsString(req)))
            .andExpect(status().isCreated())
            .andExpect(jsonPath("$.id").exists())
            .andReturn().getResponse().getContentAsString();
        
        Long id = mapper.readTree(response).get("id").asLong();
        
        // Retrieve
        mvc.perform(get("/api/orders/" + id))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.items.length()").value(1))
            .andExpect(jsonPath("$.total").value(999));
    }
}
```

**Key Takeaway**: Use `@SpringBootTest` for integration, `@WebMvcTest` for controller unit tests. Always clean DB between tests."""),

("spring-boot","Spring Boot Rate Limiting with Bucket4j","""Protect APIs from abuse.

```java
// pom.xml: bucket4j-core

@Component
public class RateLimitInterceptor implements HandlerInterceptor {
    private final Map<String, Bucket> cache = new ConcurrentHashMap<>();
    
    private Bucket createBucket() {
        return Bucket.builder()
            .addLimit(Bandwidth.classic(100, Refill.greedy(100, Duration.ofMinutes(1))))
            .build();
    }
    
    @Override
    public boolean preHandle(HttpServletRequest req, HttpServletResponse res, Object handler) {
        String ip = req.getRemoteAddr();
        Bucket bucket = cache.computeIfAbsent(ip, k -> createBucket());
        
        if (bucket.tryConsume(1)) {
            long remaining = bucket.getAvailableTokens();
            res.setHeader("X-Rate-Limit-Remaining", String.valueOf(remaining));
            return true;
        }
        
        res.setStatus(429);
        res.setHeader("Retry-After", "60");
        return false;
    }
}
```

**Key Takeaway**: Rate limit by IP for public APIs, by API key for authenticated users. Use Redis for distributed rate limiting across multiple instances."""),

("spring-boot","Spring Boot Async Processing","""Run tasks in background threads.

```java
@EnableAsync
@SpringBootApplication
public class App {}

@Service
public class NotificationService {
    @Async("taskExecutor")
    public CompletableFuture<Boolean> sendEmail(String to, String subject, String body) {
        // Runs in background thread — caller doesn't wait
        emailClient.send(to, subject, body);
        return CompletableFuture.completedFuture(true);
    }
}

@Configuration
public class AsyncConfig {
    @Bean("taskExecutor")
    public Executor taskExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setCorePoolSize(5);
        executor.setMaxPoolSize(10);
        executor.setQueueCapacity(25);
        executor.setThreadNamePrefix("async-");
        executor.setRejectedExecutionHandler(new ThreadPoolExecutor.CallerRunsPolicy());
        executor.initialize();
        return executor;
    }
}
```

**Key Takeaway**: `@Async` methods MUST be called from outside the class (proxy limitation). Always configure a custom thread pool — don't use default."""),

("spring-boot","Spring Boot Configuration Properties","""Type-safe configuration.

```java
@ConfigurationProperties(prefix = "app.payment")
@Validated
public record PaymentProperties(
    @NotBlank String gatewayUrl,
    @NotBlank String apiKey,
    @Min(1) @Max(5) int maxRetries,
    Duration timeout,
    List<String> supportedCurrencies
) {}
```

```yaml
# application.yml
app:
  payment:
    gateway-url: https://pay.example.com
    api-key: ${PAYMENT_API_KEY}
    max-retries: 3
    timeout: 30s
    supported-currencies:
      - INR
      - USD
      - EUR
```

```java
@Service
public class PaymentService {
    private final PaymentProperties config;
    
    public PaymentService(PaymentProperties config) {
        this.config = config;
    }
    
    public void charge(BigDecimal amount, String currency) {
        if (!config.supportedCurrencies().contains(currency))
            throw new UnsupportedCurrencyException(currency);
        // use config.gatewayUrl(), config.timeout() etc.
    }
}
```

**Key Takeaway**: `@ConfigurationProperties` > `@Value`. It provides type safety, validation, and IDE autocomplete."""),

("spring-boot","Spring Data JPA Specifications","""Dynamic query building for complex filters.

```java
public class ProductSpec {
    public static Specification<Product> hasCategory(String cat) {
        return (root, query, cb) -> cat == null ? null : cb.equal(root.get("category"), cat);
    }
    
    public static Specification<Product> priceBetween(Double min, Double max) {
        return (root, query, cb) -> {
            if (min != null && max != null) return cb.between(root.get("price"), min, max);
            if (min != null) return cb.greaterThanOrEqualTo(root.get("price"), min);
            if (max != null) return cb.lessThanOrEqualTo(root.get("price"), max);
            return null;
        };
    }
    
    public static Specification<Product> nameContains(String keyword) {
        return (root, query, cb) -> keyword == null ? null :
            cb.like(cb.lower(root.get("name")), "%" + keyword.toLowerCase() + "%");
    }
}

// Usage: combine dynamically
@GetMapping("/search")
public Page<Product> search(String category, Double minPrice, Double maxPrice, String keyword, Pageable page) {
    Specification<Product> spec = Specification
        .where(ProductSpec.hasCategory(category))
        .and(ProductSpec.priceBetween(minPrice, maxPrice))
        .and(ProductSpec.nameContains(keyword));
    return productRepo.findAll(spec, page);
}
```"""),

("spring-boot","Spring Boot MapStruct for DTO Mapping","""Auto-generate mapping code.

```java
// Entity
@Entity
public class User {
    Long id; String name; String email; String passwordHash;
    LocalDateTime createdAt; Address address;
}

// DTO
public record UserResponse(Long id, String name, String email, String city, String memberSince) {}

// Mapper interface — MapStruct generates implementation!
@Mapper(componentModel = "spring")
public interface UserMapper {
    @Mapping(source = "address.city", target = "city")
    @Mapping(source = "createdAt", target = "memberSince", dateFormat = "MMM yyyy")
    UserResponse toResponse(User user);
    
    List<UserResponse> toResponseList(List<User> users);
    
    @Mapping(target = "id", ignore = true)
    @Mapping(target = "passwordHash", ignore = true)
    @Mapping(target = "createdAt", expression = "java(java.time.LocalDateTime.now())")
    User toEntity(CreateUserRequest request);
}

// Usage
@Service
public class UserService {
    private final UserMapper mapper;
    public UserResponse getUser(Long id) {
        return mapper.toResponse(userRepo.findById(id).orElseThrow());
    }
}
```

**Key Takeaway**: MapStruct generates compile-time code (no reflection = fast). Add `mapstruct-processor` to annotation processor path."""),

("spring-boot","Spring Boot Application Properties Guide","""Common configuration reference.

```yaml
# Server
server:
  port: 8080
  servlet.context-path: /api
  compression.enabled: true

# Database
spring:
  datasource:
    url: jdbc:mysql://${DB_HOST:localhost}:3306/myapp
    username: ${DB_USER:root}
    password: ${DB_PASS:secret}
    hikari:
      maximum-pool-size: 20
      minimum-idle: 5
      connection-timeout: 30000
  
  # JPA
  jpa:
    hibernate.ddl-auto: validate  # never 'create' in prod!
    show-sql: false
    properties.hibernate:
      format_sql: true
      default_batch_fetch_size: 16
  
  # Jackson
  jackson:
    serialization.write-dates-as-timestamps: false
    default-property-inclusion: non_null
    time-zone: Asia/Kolkata

# Custom
app:
  version: 1.0.0
  feature-flags:
    new-checkout: true
```

**Key Takeaway**: Use `${ENV_VAR:default}` syntax for environment-specific values. Never commit secrets — use env vars or vaults."""),

("spring-boot","Spring Boot Microservices - Service Discovery","""Register and discover services dynamically.

```yaml
# Eureka Server
@EnableEurekaServer
@SpringBootApplication
public class DiscoveryServer {}

# application.yml (Eureka Server)
server.port: 8761
eureka.client.register-with-eureka: false
eureka.client.fetch-registry: false
```

```yaml
# Client service
@EnableDiscoveryClient
@SpringBootApplication
public class OrderService {}

# application.yml (Client)
spring.application.name: order-service
eureka.client.service-url.defaultZone: http://localhost:8761/eureka/
```

```java
// Call another service by name (no hardcoded URL!)
@FeignClient(name = "user-service")
public interface UserClient {
    @GetMapping("/api/users/{id}")
    UserResponse getUser(@PathVariable Long id);
}

// Usage
UserResponse user = userClient.getUser(123);
// Eureka resolves "user-service" → http://192.168.1.5:8081
```

**Key Takeaway**: Service Discovery eliminates hardcoded URLs. Services register themselves and discover others by name."""),

("spring-boot","Spring Boot API Gateway Pattern","""Single entry point for microservices.

```yaml
# Spring Cloud Gateway
spring:
  cloud:
    gateway:
      routes:
        - id: user-service
          uri: lb://user-service
          predicates:
            - Path=/api/users/**
          filters:
            - StripPrefix=1
            - name: CircuitBreaker
              args: { name: userCB, fallbackUri: forward:/fallback }
        
        - id: order-service
          uri: lb://order-service
          predicates:
            - Path=/api/orders/**
          filters:
            - StripPrefix=1
            - name: RequestRateLimiter
              args:
                redis-rate-limiter:
                  replenishRate: 10
                  burstCapacity: 20
```

### Gateway Responsibilities
- **Routing**: /users → user-service, /orders → order-service
- **Auth**: Validate JWT before forwarding
- **Rate Limiting**: Protect backend services
- **Load Balancing**: Distribute across instances
- **Circuit Breaking**: Fallback on failures

**Key Takeaway**: API Gateway is the single entry point. Clients talk to gateway only, not individual services."""),

# ═══════════════════════════════════════════════════════════════
# MORE REACT (20 more → 30 total)
# ═══════════════════════════════════════════════════════════════
("react","React Props and Children","""Pass data and components to children.

```jsx
function Card({ title, children, variant = 'default', onClick }) {
  return (
    <div className={`card card-${variant}`} onClick={onClick}>
      <h3>{title}</h3>
      <div className="card-body">{children}</div>
    </div>
  );
}

// Usage
<Card title="Welcome" variant="primary" onClick={() => alert('clicked')}>
  <p>This is the card content</p>
  <button>Action</button>
</Card>

// Render prop pattern
function DataFetcher({ url, render }) {
  const [data, setData] = useState(null);
  useEffect(() => { fetch(url).then(r=>r.json()).then(setData); }, [url]);
  return render(data);
}

<DataFetcher url="/api/users" render={(users) => (
  users?.map(u => <UserCard key={u.id} user={u} />)
)} />
```

**Key Takeaway**: Props flow down (parent → child). Use `children` for composition. Render props for sharing logic."""),

("react","React Forms - Controlled vs Uncontrolled","""Two approaches to form handling.

```jsx
// Controlled: React manages state
function LoginForm() {
  const [form, setForm] = useState({ email: '', password: '' });
  const [errors, setErrors] = useState({});
  
  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm(prev => ({ ...prev, [name]: value }));
  };
  
  const handleSubmit = (e) => {
    e.preventDefault();
    const newErrors = {};
    if (!form.email) newErrors.email = 'Required';
    if (form.password.length < 8) newErrors.password = 'Min 8 chars';
    if (Object.keys(newErrors).length) { setErrors(newErrors); return; }
    submitLogin(form);
  };
  
  return (
    <form onSubmit={handleSubmit}>
      <input name="email" value={form.email} onChange={handleChange} />
      {errors.email && <span className="error">{errors.email}</span>}
      <input name="password" type="password" value={form.password} onChange={handleChange} />
      <button type="submit">Login</button>
    </form>
  );
}
```

**Key Takeaway**: Controlled components = React is source of truth. Use libraries like React Hook Form for complex forms."""),

("react","React useRef Hook","""Access DOM elements and persist values.

```jsx
function TextInput() {
  const inputRef = useRef(null);
  const renderCount = useRef(0);
  
  useEffect(() => { renderCount.current++; }); // doesn't trigger re-render
  
  const focusInput = () => inputRef.current.focus();
  
  return (
    <div>
      <input ref={inputRef} placeholder="Click button to focus me" />
      <button onClick={focusInput}>Focus</button>
      <p>Rendered {renderCount.current} times</p>
    </div>
  );
}

// Storing previous value
function usePrevious(value) {
  const ref = useRef();
  useEffect(() => { ref.current = value; });
  return ref.current;
}

function Counter() {
  const [count, setCount] = useState(0);
  const prevCount = usePrevious(count);
  return <p>Now: {count}, Before: {prevCount}</p>;
}
```

**Key Takeaway**: useRef doesn't cause re-renders. Use it for DOM access, storing interval IDs, and tracking previous values."""),

("react","React Code Splitting and Lazy Loading","""Load components on demand for faster initial load.

```jsx
import { lazy, Suspense } from 'react';

const Dashboard = lazy(() => import('./pages/Dashboard'));
const Settings = lazy(() => import('./pages/Settings'));
const Analytics = lazy(() => import('./pages/Analytics'));

function App() {
  return (
    <Suspense fallback={<LoadingSpinner />}>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/settings" element={<Settings />} />
        <Route path="/analytics" element={<Analytics />} />
      </Routes>
    </Suspense>
  );
}
```

**Before**: One 500KB bundle loaded upfront
**After**: 100KB initial + load pages on demand

**Key Takeaway**: Lazy load route-level components. Use `Suspense` for loading fallbacks. This can reduce initial bundle size by 60%+."""),

("react","React Testing with Jest and RTL","""Test components from the user's perspective.

```jsx
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

test('shows search results', async () => {
  render(<SearchPage />);
  
  const input = screen.getByPlaceholderText('Search...');
  await userEvent.type(input, 'React');
  
  const button = screen.getByRole('button', { name: /search/i });
  fireEvent.click(button);
  
  // Wait for async results
  await waitFor(() => {
    expect(screen.getByText('React Hooks Guide')).toBeInTheDocument();
  });
  
  expect(screen.getAllByRole('listitem')).toHaveLength(5);
  expect(screen.queryByText('No results')).not.toBeInTheDocument();
});
```

**Testing Library Philosophy**: 
- Query by role, label, text (what users see)
- NOT by className, testId (implementation details)

**Key Takeaway**: Test behavior, not implementation. "The more your tests resemble the way your software is used, the more confidence they give you." """),

("react","React useMemo Hook","""Cache expensive calculations.

```jsx
function ProductList({ products, searchTerm, sortBy }) {
  // Without useMemo: re-computes on EVERY render (even unrelated state changes)
  // With useMemo: re-computes only when products, searchTerm, or sortBy change
  const filteredAndSorted = useMemo(() => {
    console.log('Computing...');
    return products
      .filter(p => p.name.toLowerCase().includes(searchTerm.toLowerCase()))
      .sort((a, b) => {
        if (sortBy === 'price') return a.price - b.price;
        return a.name.localeCompare(b.name);
      });
  }, [products, searchTerm, sortBy]);

  return (
    <ul>
      {filteredAndSorted.map(p => (
        <li key={p.id}>{p.name} - ${p.price}</li>
      ))}
    </ul>
  );
}
```

**When to use**: Expensive computations, large list filtering/sorting, complex object creation.
**When NOT to use**: Simple calculations, primitive values. The memoization overhead isn't worth it."""),

("react","React Portals","""Render components outside the DOM hierarchy.

```jsx
import { createPortal } from 'react-dom';

function Modal({ isOpen, onClose, children }) {
  if (!isOpen) return null;
  
  return createPortal(
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={e => e.stopPropagation()}>
        <button className="modal-close" onClick={onClose}>&times;</button>
        {children}
      </div>
    </div>,
    document.getElementById('modal-root') // renders here, not in parent
  );
}

// Usage
function App() {
  const [showModal, setShowModal] = useState(false);
  return (
    <div style={{ overflow: 'hidden' }}> {/* overflow won't clip modal! */}
      <button onClick={() => setShowModal(true)}>Open Modal</button>
      <Modal isOpen={showModal} onClose={() => setShowModal(false)}>
        <h2>I'm rendered outside the parent!</h2>
      </Modal>
    </div>
  );
}
```

**Key Takeaway**: Portals are essential for modals, tooltips, and dropdowns. The component stays in React tree (events bubble up) but renders elsewhere in DOM."""),

("react","React Zustand State Management","""Minimal, flexible state management.

```jsx
import { create } from 'zustand';
import { devtools, persist } from 'zustand/middleware';

const useStore = create(
  devtools(
    persist(
      (set, get) => ({
        cart: [],
        total: 0,
        
        addItem: (item) => set((state) => ({
          cart: [...state.cart, item],
          total: state.total + item.price
        })),
        
        removeItem: (id) => set((state) => {
          const item = state.cart.find(i => i.id === id);
          return {
            cart: state.cart.filter(i => i.id !== id),
            total: state.total - item.price
          };
        }),
        
        clearCart: () => set({ cart: [], total: 0 }),
        itemCount: () => get().cart.length,
      }),
      { name: 'cart-storage' } // localStorage persistence
    )
  )
);

// Usage in any component (no Provider needed!)
function CartIcon() {
  const total = useStore(state => state.total);
  const count = useStore(state => state.cart.length);
  return <span>Cart ({count}) - ₹{total}</span>;
}
```

**Key Takeaway**: Zustand is simpler than Redux. No providers, no reducers, no actions. Just a hook."""),

# ═══════════════════════════════════════════════════════════════
# MORE JAVASCRIPT (17 more → 25 total)
# ═══════════════════════════════════════════════════════════════
("javascript","JavaScript Prototypes and Inheritance","""How objects inherit properties.

```javascript
function Animal(name) {
  this.name = name;
}
Animal.prototype.speak = function() {
  return `${this.name} makes a sound`;
};

function Dog(name, breed) {
  Animal.call(this, name); // super()
  this.breed = breed;
}
Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;
Dog.prototype.bark = function() { return `${this.name} barks!`; };

// Modern: ES6 classes (syntactic sugar over prototypes)
class Cat extends Animal {
  constructor(name, color) { super(name); this.color = color; }
  meow() { return `${this.name} meows!`; }
}

// Prototype chain
const cat = new Cat('Whiskers', 'orange');
cat.meow();  // own method
cat.speak(); // inherited from Animal.prototype
cat.toString(); // inherited from Object.prototype
```

**Key Takeaway**: Every object has a `__proto__` pointing to its prototype. ES6 classes are just cleaner syntax — prototypes still work underneath."""),

("javascript","JavaScript this Keyword","""Context-dependent reference.

```javascript
const user = {
  name: 'Dipak',
  greet() { console.log(`Hi, ${this.name}`); },           // this = user
  greetArrow: () => console.log(`Hi, ${this.name}`),      // this = outer scope!
  delayedGreet() {
    setTimeout(function() { console.log(this.name); }, 1000);  // this = window!
    setTimeout(() => { console.log(this.name); }, 1000);       // this = user (arrow)
  }
};

user.greet();        // "Hi, Dipak"
user.greetArrow();   // "Hi, undefined" (arrow captures outer this)

// Explicit binding
function greet(greeting) { console.log(`${greeting}, ${this.name}`); }
greet.call(user, 'Hello');     // "Hello, Dipak" (immediate)
greet.apply(user, ['Hello']);  // same, args as array
const bound = greet.bind(user); // returns new function
bound('Hey');                   // "Hey, Dipak"
```

**Key Takeaway**: Arrow functions don't have their own `this` — they inherit from enclosing scope. Use arrows in callbacks, regular functions in methods."""),

("javascript","JavaScript Generators and Iterators","""Lazy evaluation and custom iteration.

```javascript
function* fibonacci() {
  let a = 0, b = 1;
  while (true) {
    yield a;
    [a, b] = [b, a + b];
  }
}

const fib = fibonacci();
fib.next(); // { value: 0, done: false }
fib.next(); // { value: 1, done: false }
fib.next(); // { value: 1, done: false }

// Take first N values
function* take(gen, n) {
  for (let i = 0; i < n; i++) {
    const { value, done } = gen.next();
    if (done) return;
    yield value;
  }
}

console.log([...take(fibonacci(), 10)]); // [0,1,1,2,3,5,8,13,21,34]

// Async generator
async function* fetchPages(url) {
  let page = 1;
  while (true) {
    const res = await fetch(`${url}?page=${page}`);
    const data = await res.json();
    if (data.length === 0) return;
    yield data;
    page++;
  }
}

for await (const page of fetchPages('/api/items')) { process(page); }
```"""),

("javascript","JavaScript Proxy and Reflect","""Intercept object operations.

```javascript
const handler = {
  get(target, prop) {
    console.log(`Accessing: ${prop}`);
    return prop in target ? target[prop] : `Property ${prop} not found`;
  },
  set(target, prop, value) {
    if (prop === 'age' && (value < 0 || value > 150))
      throw new RangeError('Invalid age');
    target[prop] = value;
    return true;
  }
};

const user = new Proxy({}, handler);
user.name = 'Dipak';
user.age = 25;
user.age = -1;  // throws RangeError!

// Reactive state (Vue.js uses this!)
function reactive(obj) {
  return new Proxy(obj, {
    set(target, key, value) {
      target[key] = value;
      notifySubscribers(key, value); // trigger UI update
      return true;
    }
  });
}

const state = reactive({ count: 0 });
state.count = 1; // automatically triggers notification
```

**Key Takeaway**: Proxies enable validation, logging, reactive data binding, and API mocking. Vue 3's reactivity system is built on Proxy."""),

("javascript","JavaScript Error Handling Patterns","""Robust error handling strategies.

```javascript
// Custom error classes
class ApiError extends Error {
  constructor(statusCode, message, data = null) {
    super(message);
    this.name = 'ApiError';
    this.statusCode = statusCode;
    this.data = data;
  }
}

// Async error wrapper
async function tryCatch(promise) {
  try {
    const data = await promise;
    return [null, data];
  } catch (error) {
    return [error, null];
  }
}

// Usage
const [err, user] = await tryCatch(fetchUser(id));
if (err) {
  if (err instanceof ApiError && err.statusCode === 404) handleNotFound();
  else throw err;
}

// Global error handlers
window.addEventListener('unhandledrejection', (e) => {
  console.error('Unhandled promise:', e.reason);
  reportToSentry(e.reason);
});

process.on('uncaughtException', (err) => {
  console.error('Uncaught:', err);
  process.exit(1);
});
```"""),

("javascript","JavaScript Web Workers","""Run heavy computation off the main thread.

```javascript
// worker.js
self.onmessage = (e) => {
  const { data, type } = e.data;
  if (type === 'SORT') {
    const sorted = data.sort((a, b) => a - b); // heavy operation
    self.postMessage({ type: 'SORTED', result: sorted });
  }
};

// main.js
const worker = new Worker('worker.js');

worker.onmessage = (e) => {
  console.log('Sorted:', e.data.result); // receive result
  updateUI(e.data.result);
};

worker.onerror = (e) => console.error('Worker error:', e.message);

// Send data to worker (doesn't block UI)
const bigArray = Array.from({ length: 1000000 }, () => Math.random());
worker.postMessage({ type: 'SORT', data: bigArray });

// Terminate when done
worker.terminate();
```

**Key Takeaway**: Web Workers run in separate thread — no access to DOM. Use for sorting, image processing, crypto, parsing large JSON."""),

("javascript","JavaScript Design Patterns - Module","""Organize code with encapsulation.

```javascript
// Revealing Module Pattern
const ShoppingCart = (() => {
  let items = []; // private
  
  function addItem(item) { items.push(item); }
  function removeItem(id) { items = items.filter(i => i.id !== id); }
  function getTotal() { return items.reduce((sum, i) => sum + i.price, 0); }
  function getItems() { return [...items]; } // return copy
  
  return { addItem, removeItem, getTotal, getItems }; // public API
})();

ShoppingCart.addItem({ id: 1, name: 'Laptop', price: 999 });
ShoppingCart.getTotal(); // 999
ShoppingCart.items; // undefined (private!)

// Observer Pattern
class EventEmitter {
  #handlers = {};
  on(event, fn) { (this.#handlers[event] ??= []).push(fn); }
  off(event, fn) { this.#handlers[event] = this.#handlers[event]?.filter(f => f !== fn); }
  emit(event, ...args) { this.#handlers[event]?.forEach(fn => fn(...args)); }
}

const bus = new EventEmitter();
bus.on('login', (user) => console.log(`Welcome ${user}`));
bus.emit('login', 'Dipak');
```"""),

# ═══════════════════════════════════════════════════════════════
# TYPESCRIPT — 10 topics
# ═══════════════════════════════════════════════════════════════
("typescript","TypeScript Type Basics","""Static typing for JavaScript.

```typescript
// Primitives
let name: string = "Dipak";
let age: number = 25;
let active: boolean = true;

// Arrays
let scores: number[] = [90, 85, 92];
let names: Array<string> = ["Alice", "Bob"];

// Objects
interface User {
  id: number;
  name: string;
  email: string;
  age?: number;          // optional
  readonly createdAt: Date; // can't modify
}

// Function types
function greet(name: string, loud?: boolean): string {
  return loud ? name.toUpperCase() : name;
}

type MathFn = (a: number, b: number) => number;
const add: MathFn = (a, b) => a + b;

// Type assertion
const input = document.getElementById('email') as HTMLInputElement;
input.value = "test@mail.com";
```

**Key Takeaway**: TypeScript catches errors at compile time, not runtime. Use `interface` for objects, `type` for unions and complex types."""),

("typescript","TypeScript Generics","""Reusable, type-safe functions and classes.

```typescript
// Generic function
function firstElement<T>(arr: T[]): T | undefined {
  return arr[0];
}
firstElement([1,2,3]);       // number
firstElement(["a","b","c"]); // string

// Constrained generics
function longest<T extends { length: number }>(a: T, b: T): T {
  return a.length >= b.length ? a : b;
}
longest("hello", "hi");     // works: strings have length
longest([1,2], [1,2,3]);    // works: arrays have length

// Generic interface
interface ApiResponse<T> {
  data: T;
  status: number;
  message: string;
}

async function fetchUser(id: number): Promise<ApiResponse<User>> {
  const res = await fetch(`/api/users/${id}`);
  return res.json();
}

// Generic class
class Stack<T> {
  private items: T[] = [];
  push(item: T): void { this.items.push(item); }
  pop(): T | undefined { return this.items.pop(); }
  peek(): T | undefined { return this.items[this.items.length - 1]; }
}
```"""),

("typescript","TypeScript Utility Types","""Built-in type transformations.

```typescript
interface User {
  id: number;
  name: string;
  email: string;
  password: string;
  role: 'admin' | 'user';
}

// Partial: all properties optional
type UpdateUser = Partial<User>;

// Required: all properties required
type CompleteUser = Required<User>;

// Pick: select specific properties
type UserPreview = Pick<User, 'id' | 'name'>;

// Omit: exclude properties
type PublicUser = Omit<User, 'password'>;

// Record: key-value map
type UserRoles = Record<string, 'admin' | 'editor' | 'viewer'>;

// ReturnType
function getUser() { return { id: 1, name: "Dipak" }; }
type UserType = ReturnType<typeof getUser>; // { id: number; name: string }

// Exclude / Extract
type T = Exclude<'a'|'b'|'c', 'a'>; // 'b' | 'c'
type U = Extract<'a'|'b'|'c', 'a'|'f'>; // 'a'

// NonNullable
type V = NonNullable<string | null | undefined>; // string
```"""),

("typescript","TypeScript Discriminated Unions","""Type-safe handling of different shapes.

```typescript
type Shape = 
  | { kind: 'circle'; radius: number }
  | { kind: 'rectangle'; width: number; height: number }
  | { kind: 'triangle'; base: number; height: number };

function area(shape: Shape): number {
  switch (shape.kind) {
    case 'circle':    return Math.PI * shape.radius ** 2;
    case 'rectangle': return shape.width * shape.height;
    case 'triangle':  return 0.5 * shape.base * shape.height;
  }
}

// API response handling
type ApiResult<T> = 
  | { status: 'success'; data: T }
  | { status: 'error'; error: string }
  | { status: 'loading' };

function renderResult(result: ApiResult<User[]>) {
  switch (result.status) {
    case 'loading': return <Spinner />;
    case 'error':   return <Error message={result.error} />;
    case 'success': return <UserList users={result.data} />;
  }
}
```

**Key Takeaway**: Discriminated unions with a shared `kind`/`type`/`status` field enable exhaustive type checking in switch statements."""),

# ═══════════════════════════════════════════════════════════════
# MORE .NET (14 more → 20 total)
# ═══════════════════════════════════════════════════════════════
("dotnet","C# Records","""Immutable data types with value equality.

```csharp
// Record class (reference type, immutable)
public record User(string Name, string Email, int Age);

var user = new User("Dipak", "d@test.com", 25);
Console.WriteLine(user); // User { Name = Dipak, Email = d@test.com, Age = 25 }

// Value equality (not reference equality)
var user2 = new User("Dipak", "d@test.com", 25);
Console.WriteLine(user == user2); // True!

// Non-destructive mutation
var updated = user with { Email = "new@test.com" };

// Record with validation
public record Temperature(double Value, string Unit) {
    public Temperature {
        if (Unit != "C" && Unit != "F") throw new ArgumentException("Invalid unit");
    }
    public double ToCelsius() => Unit == "C" ? Value : (Value - 32) * 5 / 9;
}
```

**Key Takeaway**: Records auto-generate Equals, GetHashCode, ToString, and deconstruct. Perfect for DTOs, value objects, and API responses."""),

("dotnet","C# Delegates and Events","""Type-safe function pointers and event handling.

```csharp
// Delegate
public delegate bool Predicate<T>(T item);

// Built-in delegates
Func<int, int, int> add = (a, b) => a + b;     // returns value
Action<string> log = msg => Console.WriteLine(msg); // void
Predicate<int> isEven = n => n % 2 == 0;        // returns bool

// Events
public class StockTicker {
    public event EventHandler<StockChangedEventArgs>? PriceChanged;
    
    public void UpdatePrice(string symbol, decimal price) {
        PriceChanged?.Invoke(this, new StockChangedEventArgs(symbol, price));
    }
}

public record StockChangedEventArgs(string Symbol, decimal Price);

// Subscribe
var ticker = new StockTicker();
ticker.PriceChanged += (sender, args) => {
    Console.WriteLine($"{args.Symbol}: ₹{args.Price}");
};
ticker.UpdatePrice("INFY", 1500.50m);
```

**Key Takeaway**: Use `Func<>`, `Action<>`, `Predicate<>` instead of custom delegates. Events provide publisher-subscriber pattern with loose coupling."""),

("dotnet","C# Extension Methods","""Add methods to existing types without modifying them.

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

**Key Takeaway**: Extension methods must be `static` in a `static` class. Use `this` keyword on first parameter. LINQ is entirely built with extension methods."""),

("dotnet","ASP.NET Core Minimal APIs","""Lightweight HTTP endpoints without controllers.

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddDbContext<AppDb>();

var app = builder.Build();

app.MapGet("/api/todos", async (AppDb db) =>
    await db.Todos.ToListAsync());

app.MapGet("/api/todos/{id}", async (int id, AppDb db) =>
    await db.Todos.FindAsync(id) is Todo todo ? Results.Ok(todo) : Results.NotFound());

app.MapPost("/api/todos", async (Todo todo, AppDb db) => {
    db.Todos.Add(todo);
    await db.SaveChangesAsync();
    return Results.Created($"/api/todos/{todo.Id}", todo);
});

app.MapPut("/api/todos/{id}", async (int id, Todo input, AppDb db) => {
    var todo = await db.Todos.FindAsync(id);
    if (todo is null) return Results.NotFound();
    todo.Title = input.Title;
    todo.IsComplete = input.IsComplete;
    await db.SaveChangesAsync();
    return Results.NoContent();
});

app.MapDelete("/api/todos/{id}", async (int id, AppDb db) => {
    var todo = await db.Todos.FindAsync(id);
    if (todo is null) return Results.NotFound();
    db.Todos.Remove(todo);
    await db.SaveChangesAsync();
    return Results.NoContent();
});

app.Run();
```"""),

# ═══════════════════════════════════════════════════════════════
# MORE NODE.JS (12 more → 15 total)
# ═══════════════════════════════════════════════════════════════
("nodejs","Node.js Event Loop Deep Dive","""How Node.js handles concurrency.

```
Node.js Event Loop Phases:
┌───────────────────┐
│    timers         │ ← setTimeout, setInterval
├───────────────────┤
│    pending I/O    │ ← I/O callbacks
├───────────────────┤
│    idle, prepare  │ ← internal
├───────────────────┤
│    poll           │ ← incoming connections, data
├───────────────────┤
│    check          │ ← setImmediate
├───────────────────┤
│    close          │ ← socket.on('close')
└───────────────────┘
```

```javascript
console.log('1');                           // sync
setImmediate(() => console.log('2'));        // check phase
setTimeout(() => console.log('3'), 0);      // timers phase
process.nextTick(() => console.log('4'));    // before any phase!
Promise.resolve().then(() => console.log('5')); // microtask

// Output: 1, 4, 5, 3, 2
// nextTick > microtask > macrotask
```

**Key Takeaway**: `process.nextTick` fires before promises. Don't starve the event loop with heavy sync work — use Worker Threads."""),

("nodejs","Node.js Streams","""Process data chunk by chunk (memory efficient).

```javascript
const fs = require('fs');
const { Transform } = require('stream');

// Read 2GB file without loading into memory
const readStream = fs.createReadStream('huge-file.csv');
const writeStream = fs.createWriteStream('output.csv');

// Custom transform stream
const toUpperCase = new Transform({
  transform(chunk, encoding, callback) {
    callback(null, chunk.toString().toUpperCase());
  }
});

// Pipe: read → transform → write
readStream.pipe(toUpperCase).pipe(writeStream);

// Pipeline with error handling (preferred)
const { pipeline } = require('stream/promises');
await pipeline(
  fs.createReadStream('input.csv'),
  toUpperCase,
  fs.createWriteStream('output.csv')
);

// HTTP streaming
app.get('/download', (req, res) => {
  const stream = fs.createReadStream('large-file.zip');
  res.setHeader('Content-Type', 'application/zip');
  stream.pipe(res);
});
```

**Key Takeaway**: Streams process data in chunks — perfect for large files, real-time data, and HTTP responses. Always use `pipeline()` for proper error handling."""),

("nodejs","Express Rate Limiting","""Protect APIs from abuse.

```javascript
const rateLimit = require('express-rate-limit');

const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100,                  // 100 requests per window
  message: { error: 'Too many requests, try again later' },
  standardHeaders: true,     // X-RateLimit-* headers
  legacyHeaders: false,
});

const loginLimiter = rateLimit({
  windowMs: 60 * 60 * 1000, // 1 hour
  max: 5,                    // 5 login attempts
  message: { error: 'Too many login attempts' },
});

app.use('/api/', apiLimiter);
app.use('/api/auth/login', loginLimiter);
```

**Key Takeaway**: Rate limit by IP for public APIs, by API key for authenticated. Use Redis store for distributed rate limiting across multiple instances."""),

("nodejs","JWT Authentication in Node.js","""Stateless auth with JSON Web Tokens.

```javascript
const jwt = require('jsonwebtoken');

// Generate token
function generateToken(user) {
  return jwt.sign(
    { id: user.id, email: user.email, role: user.role },
    process.env.JWT_SECRET,
    { expiresIn: '24h' }
  );
}

// Login route
app.post('/api/auth/login', async (req, res) => {
  const { email, password } = req.body;
  const user = await User.findOne({ email }).select('+password');
  if (!user || !(await user.comparePassword(password)))
    return res.status(401).json({ error: 'Invalid credentials' });
  const token = generateToken(user);
  res.json({ token, user: { id: user.id, name: user.name } });
});

// Auth middleware
function protect(req, res, next) {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) return res.status(401).json({ error: 'Not authenticated' });
  try {
    req.user = jwt.verify(token, process.env.JWT_SECRET);
    next();
  } catch { res.status(403).json({ error: 'Invalid token' }); }
}

app.get('/api/profile', protect, (req, res) => res.json(req.user));
```"""),

("nodejs","WebSockets with Socket.io","""Real-time bidirectional communication.

```javascript
// Server
const { Server } = require('socket.io');
const io = new Server(httpServer, { cors: { origin: "*" } });

io.on('connection', (socket) => {
  console.log(`User connected: ${socket.id}`);
  
  socket.on('join-room', (room) => { socket.join(room); });
  
  socket.on('chat-message', ({ room, message, user }) => {
    io.to(room).emit('new-message', { message, user, time: new Date() });
  });
  
  socket.on('typing', ({ room, user }) => {
    socket.to(room).emit('user-typing', user);
  });
  
  socket.on('disconnect', () => {
    console.log(`User disconnected: ${socket.id}`);
  });
});

// Client
const socket = io('http://localhost:3000');
socket.emit('join-room', 'general');
socket.emit('chat-message', { room: 'general', message: 'Hello!', user: 'Dipak' });
socket.on('new-message', (data) => displayMessage(data));
```

**Key Takeaway**: Socket.io handles reconnection, fallback transports, and rooms automatically. Use namespaces for different features (chat, notifications)."""),

# ═══════════════════════════════════════════════════════════════
# MORE DATABASE (10 more → 15 total)
# ═══════════════════════════════════════════════════════════════
("database","Database Normalization Forms","""Reduce redundancy and improve data integrity.

| Normal Form | Rule | Example |
|:---|:---|:---|
| 1NF | No repeating groups, atomic values | `skills TEXT` → separate `user_skills` table |
| 2NF | No partial dependency on composite key | Every non-key depends on FULL primary key |
| 3NF | No transitive dependency | Remove `dept_name` if `dept_id` exists |
| BCNF | Every determinant is a candidate key | Stricter 3NF |

```sql
-- Unnormalized (bad)
CREATE TABLE orders (
    id INT, customer_name TEXT, customer_email TEXT,
    product1 TEXT, price1 DECIMAL, product2 TEXT, price2 DECIMAL
);

-- Normalized (good)
CREATE TABLE customers (id INT PRIMARY KEY, name TEXT, email TEXT UNIQUE);
CREATE TABLE orders (id INT PRIMARY KEY, customer_id INT REFERENCES customers(id), created_at TIMESTAMP);
CREATE TABLE order_items (id INT PRIMARY KEY, order_id INT REFERENCES orders(id),
    product TEXT, price DECIMAL, quantity INT);
```

**Key Takeaway**: 3NF is enough for most apps. Denormalize strategically (read-heavy dashboards) only after measuring performance."""),

("database","SQL Common Table Expressions (CTEs)","""Readable subqueries and recursion.

```sql
-- Simple CTE (readability)
WITH active_users AS (
    SELECT * FROM users WHERE last_login > NOW() - INTERVAL 30 DAY
),
user_orders AS (
    SELECT user_id, COUNT(*) as order_count, SUM(total) as total_spent
    FROM orders GROUP BY user_id
)
SELECT u.name, u.email, o.order_count, o.total_spent
FROM active_users u
JOIN user_orders o ON u.id = o.user_id
WHERE o.total_spent > 1000;

-- Recursive CTE: org chart hierarchy
WITH RECURSIVE org_chart AS (
    SELECT id, name, manager_id, 0 as level
    FROM employees WHERE manager_id IS NULL
    UNION ALL
    SELECT e.id, e.name, e.manager_id, oc.level + 1
    FROM employees e JOIN org_chart oc ON e.manager_id = oc.id
)
SELECT REPEAT('  ', level) || name as hierarchy FROM org_chart;
```

**Key Takeaway**: CTEs improve readability over nested subqueries. Recursive CTEs handle tree/graph data (org charts, categories, file systems)."""),

("database","SQL Stored Procedures","""Encapsulate business logic in the database.

```sql
DELIMITER //
CREATE PROCEDURE TransferMoney(
    IN from_account INT,
    IN to_account INT,
    IN amount DECIMAL(10,2),
    OUT success BOOLEAN
)
BEGIN
    DECLARE from_balance DECIMAL(10,2);
    
    START TRANSACTION;
    
    SELECT balance INTO from_balance FROM accounts WHERE id = from_account FOR UPDATE;
    
    IF from_balance >= amount THEN
        UPDATE accounts SET balance = balance - amount WHERE id = from_account;
        UPDATE accounts SET balance = balance + amount WHERE id = to_account;
        INSERT INTO transactions (from_id, to_id, amount, created_at) 
            VALUES (from_account, to_account, amount, NOW());
        SET success = TRUE;
        COMMIT;
    ELSE
        SET success = FALSE;
        ROLLBACK;
    END IF;
END //
DELIMITER ;

-- Usage
CALL TransferMoney(1, 2, 500.00, @result);
SELECT @result;
```

**Key Takeaway**: Stored procedures reduce network roundtrips and ensure atomicity. But they're hard to version-control and test — prefer application-level logic for complex business rules."""),

("database","SQL EXPLAIN and Query Plans","""Understand how MySQL executes your query.

```sql
EXPLAIN ANALYZE SELECT u.name, COUNT(o.id) as orders
FROM users u LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at > '2024-01-01'
GROUP BY u.name HAVING orders > 5
ORDER BY orders DESC;
```

| Column | Good Value | Bad Value |
|:---|:---|:---|
| type | ref, range, index | ALL (full scan!) |
| key | Uses index | NULL (no index) |
| rows | Low number | High (scanning many) |
| Extra | Using index | Using filesort, Using temporary |

### Optimization Steps
1. Add index: `CREATE INDEX idx_created ON users(created_at);`
2. Check: `EXPLAIN SELECT ...` — should show `range` not `ALL`
3. Composite: `CREATE INDEX idx_user_orders ON orders(user_id, status);`

**Key Takeaway**: Run EXPLAIN on every slow query. The `type` column is most important: `const` > `ref` > `range` > `index` > `ALL`."""),

# ═══════════════════════════════════════════════════════════════
# MORE MONGODB (10 topics)
# ═══════════════════════════════════════════════════════════════
("mongodb","MongoDB CRUD Operations","""Basic database operations.

```javascript
// Create
db.users.insertOne({ name: "Dipak", age: 25, skills: ["Java","React"] });
db.users.insertMany([{ name: "Alice" }, { name: "Bob" }]);

// Read
db.users.find({ age: { $gte: 18 } }).sort({ name: 1 }).limit(10);
db.users.findOne({ email: "d@test.com" });

// Query operators
db.products.find({
  price: { $gte: 100, $lte: 500 },
  category: { $in: ["electronics", "books"] },
  $or: [{ inStock: true }, { preOrder: true }]
});

// Update
db.users.updateOne({ _id: id }, { $set: { age: 26 }, $push: { skills: "Spring" } });
db.users.updateMany({ role: "guest" }, { $set: { active: false } });

// Delete
db.users.deleteOne({ _id: id });
db.users.deleteMany({ lastLogin: { $lt: new Date("2023-01-01") } });
```

**Key Takeaway**: Use `$set` for partial updates (don't replace entire document). Use `$push/$pull` for arrays."""),

("mongodb","MongoDB Schema Design - Embed vs Reference","""When to nest vs link documents.

```javascript
// EMBED: data accessed together, 1:few relationship
{
  _id: ObjectId("..."),
  name: "Dipak",
  address: {                    // embedded
    street: "MG Road",
    city: "Pune",
    state: "Maharashtra"
  },
  skills: ["Java", "React"]    // embedded array
}

// REFERENCE: data accessed independently, 1:many, many:many
{
  _id: ObjectId("..."),
  title: "MongoDB Schema Design",
  author_id: ObjectId("..."),   // reference
  category_ids: [ObjectId("..."), ObjectId("...")] // reference array
}
```

| Criteria | Embed | Reference |
|:---|:---|:---|
| Reads | Always together | Independent |
| Cardinality | 1:1, 1:few | 1:many, many:many |
| Size limit | < 16MB per doc | Unlimited |
| Atomicity | Automatic | Need transactions |
| Updates | Duplicated data risk | Single source of truth |

**Key Takeaway**: Embed for performance (fewer queries), reference for flexibility. If sub-document > 100 items, reference it."""),

("mongodb","MongoDB Indexes","""Speed up queries with proper indexing.

```javascript
// Single field index
db.users.createIndex({ email: 1 }, { unique: true });

// Compound index (order matters!)
db.orders.createIndex({ status: 1, createdAt: -1 });

// Text index for search
db.articles.createIndex({ title: "text", content: "text" });
db.articles.find({ $text: { $search: "mongodb tutorial" } });

// TTL index (auto-delete expired docs)
db.sessions.createIndex({ expiresAt: 1 }, { expireAfterSeconds: 0 });

// Partial index (index only matching docs)
db.orders.createIndex({ status: 1 }, { partialFilterExpression: { status: "pending" } });

// Check index usage
db.users.find({ email: "test@mail.com" }).explain("executionStats");
// Look for: IXSCAN (good) vs COLLSCAN (bad)
```

**Key Takeaway**: Index fields you filter, sort, and group by. But don't over-index — each index slows down writes and uses memory."""),

# ═══════════════════════════════════════════════════════════════
# MORE DSA (22 more → 30 total)
# ═══════════════════════════════════════════════════════════════
("dsa","Kadane's Algorithm - Maximum Subarray","""Find max sum contiguous subarray in O(n).

```java
public int maxSubArray(int[] nums) {
    int maxSum = nums[0];
    int currentSum = nums[0];
    
    for (int i = 1; i < nums.length; i++) {
        // Either extend current subarray or start new
        currentSum = Math.max(nums[i], currentSum + nums[i]);
        maxSum = Math.max(maxSum, currentSum);
    }
    return maxSum;
}

// Example: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
// maxSubArray = [4, -1, 2, 1] = 6
```

**Logic**: At each element, decide: "Is it better to extend the previous subarray or start fresh?"

**Key Takeaway**: Classic DP problem. Extend if `currentSum + nums[i] > nums[i]`, otherwise start new subarray."""),

("dsa","LRU Cache Implementation","""Least Recently Used cache with O(1) operations.

```java
class LRUCache {
    private int capacity;
    private Map<Integer, Node> map = new HashMap<>();
    private Node head = new Node(0,0), tail = new Node(0,0);
    
    public LRUCache(int capacity) {
        this.capacity = capacity;
        head.next = tail; tail.prev = head;
    }
    
    public int get(int key) {
        if (!map.containsKey(key)) return -1;
        Node node = map.get(key);
        remove(node);
        insertAtHead(node);
        return node.val;
    }
    
    public void put(int key, int value) {
        if (map.containsKey(key)) remove(map.get(key));
        if (map.size() == capacity) {
            map.remove(tail.prev.key);
            remove(tail.prev);
        }
        Node node = new Node(key, value);
        map.put(key, node);
        insertAtHead(node);
    }
    
    class Node { int key, val; Node prev, next;
        Node(int k, int v) { key=k; val=v; }
    }
    // remove() and insertAtHead() manipulate doubly linked list
}
```

**Key Takeaway**: HashMap + Doubly Linked List = O(1) get and put. This is a top interview question at FAANG companies."""),

("dsa","Valid Parentheses - Stack Pattern","""Classic stack problem.

```java
public boolean isValid(String s) {
    Stack<Character> stack = new Stack<>();
    Map<Character,Character> pairs = Map.of(')', '(', '}', '{', ']', '[');
    
    for (char c : s.toCharArray()) {
        if (pairs.containsValue(c)) {
            stack.push(c); // opening bracket
        } else if (pairs.containsKey(c)) {
            if (stack.isEmpty() || stack.pop() != pairs.get(c)) return false;
        }
    }
    return stack.isEmpty();
}

// Examples:
// "([])" → true
// "([)]" → false
// "{}" → true
```

### Stack Pattern Problems
- Valid parentheses
- Next greater element
- Min stack
- Evaluate reverse polish notation
- Largest rectangle in histogram

**Key Takeaway**: Whenever you need to match pairs, or track "nearest previous", think Stack."""),

("dsa","Topological Sort","""Order dependencies (course schedule, build systems).

```java
public int[] topologicalSort(int numCourses, int[][] prerequisites) {
    int[] inDegree = new int[numCourses];
    Map<Integer, List<Integer>> graph = new HashMap<>();
    
    for (int[] pre : prerequisites) {
        graph.computeIfAbsent(pre[1], k -> new ArrayList<>()).add(pre[0]);
        inDegree[pre[0]]++;
    }
    
    Queue<Integer> queue = new LinkedList<>();
    for (int i = 0; i < numCourses; i++)
        if (inDegree[i] == 0) queue.offer(i);
    
    int[] order = new int[numCourses];
    int idx = 0;
    while (!queue.isEmpty()) {
        int course = queue.poll();
        order[idx++] = course;
        for (int next : graph.getOrDefault(course, List.of())) {
            if (--inDegree[next] == 0) queue.offer(next);
        }
    }
    return idx == numCourses ? order : new int[0]; // empty if cycle
}
```

**Use cases**: Course schedule, build dependencies (Maven/Gradle), task scheduling, package installation."""),

("dsa","Dijkstra's Shortest Path","""Find shortest path in weighted graph.

```java
public int[] dijkstra(Map<Integer, List<int[]>> graph, int src, int n) {
    int[] dist = new int[n];
    Arrays.fill(dist, Integer.MAX_VALUE);
    dist[src] = 0;
    
    // Min-heap: [distance, node]
    PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) -> a[0] - b[0]);
    pq.offer(new int[]{0, src});
    
    while (!pq.isEmpty()) {
        int[] curr = pq.poll();
        int d = curr[0], u = curr[1];
        
        if (d > dist[u]) continue; // skip outdated
        
        for (int[] edge : graph.getOrDefault(u, List.of())) {
            int v = edge[0], w = edge[1];
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.offer(new int[]{dist[v], v});
            }
        }
    }
    return dist;
}
```

**Complexity**: O((V + E) log V) with binary heap.
**Limitation**: Doesn't work with negative weights — use Bellman-Ford instead."""),

("dsa","Merge Sort","""Stable, O(n log n) divide-and-conquer sort.

```java
public void mergeSort(int[] arr, int left, int right) {
    if (left >= right) return;
    int mid = left + (right - left) / 2;
    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);
    merge(arr, left, mid, right);
}

private void merge(int[] arr, int left, int mid, int right) {
    int[] temp = new int[right - left + 1];
    int i = left, j = mid + 1, k = 0;
    
    while (i <= mid && j <= right) {
        if (arr[i] <= arr[j]) temp[k++] = arr[i++];
        else temp[k++] = arr[j++];
    }
    while (i <= mid) temp[k++] = arr[i++];
    while (j <= right) temp[k++] = arr[j++];
    
    System.arraycopy(temp, 0, arr, left, temp.length);
}
```

| Algorithm | Best | Average | Worst | Space | Stable |
|:---|:---|:---|:---|:---|:---|
| MergeSort | O(nlogn) | O(nlogn) | O(nlogn) | O(n) | Yes |
| QuickSort | O(nlogn) | O(nlogn) | O(n²) | O(logn) | No |
| HeapSort | O(nlogn) | O(nlogn) | O(nlogn) | O(1) | No |"""),

("dsa","QuickSort with Partition","""Efficient in-place sorting.

```java
public void quickSort(int[] arr, int low, int high) {
    if (low < high) {
        int pivot = partition(arr, low, high);
        quickSort(arr, low, pivot - 1);
        quickSort(arr, pivot + 1, high);
    }
}

private int partition(int[] arr, int low, int high) {
    int pivot = arr[high]; // last element as pivot
    int i = low - 1;       // pointer for smaller elements
    
    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr, i, j);
        }
    }
    swap(arr, i + 1, high);
    return i + 1;
}

// Optimization: random pivot to avoid O(n²) worst case
int randomPivot = low + random.nextInt(high - low + 1);
swap(arr, randomPivot, high); // move to end, then partition normally
```

**Key Takeaway**: QuickSort is fastest in practice (cache-friendly, in-place). Use random pivot to avoid worst-case O(n²) on sorted input."""),

("dsa","Knapsack Problem - DP","""Classic optimization problem.

```java
// 0/1 Knapsack: each item used at most once
public int knapsack(int[] weights, int[] values, int capacity) {
    int n = weights.length;
    int[][] dp = new int[n + 1][capacity + 1];
    
    for (int i = 1; i <= n; i++) {
        for (int w = 0; w <= capacity; w++) {
            dp[i][w] = dp[i-1][w]; // don't take item i
            if (weights[i-1] <= w) {
                dp[i][w] = Math.max(dp[i][w], 
                    dp[i-1][w - weights[i-1]] + values[i-1]); // take item i
            }
        }
    }
    return dp[n][capacity];
}

// Space optimized: O(capacity) instead of O(n * capacity)
public int knapsackOptimized(int[] wt, int[] val, int cap) {
    int[] dp = new int[cap + 1];
    for (int i = 0; i < wt.length; i++)
        for (int w = cap; w >= wt[i]; w--) // reverse to avoid reuse
            dp[w] = Math.max(dp[w], dp[w - wt[i]] + val[i]);
    return dp[cap];
}
```

**Variants**: Unbounded knapsack, fractional knapsack (greedy), subset sum, coin change."""),

("dsa","Longest Common Subsequence","""Find longest sequence common to both strings.

```java
public int lcs(String s1, String s2) {
    int m = s1.length(), n = s2.length();
    int[][] dp = new int[m + 1][n + 1];
    
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (s1.charAt(i-1) == s2.charAt(j-1)) {
                dp[i][j] = dp[i-1][j-1] + 1;
            } else {
                dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }
    return dp[m][n];
}

// Example: "ABCBDAB" and "BDCAB"
// LCS = "BCAB" (length 4)
```

### Related Problems
- Edit Distance (Levenshtein)
- Longest Increasing Subsequence
- Shortest Common Supersequence
- Diff algorithms (git diff uses LCS)

**Key Takeaway**: LCS is the foundation for text diff tools, DNA sequence alignment, and plagiarism detection."""),

("dsa","Dutch National Flag - 3-Way Partition","""Sort array of 0s, 1s, and 2s in O(n).

```java
public void sortColors(int[] nums) {
    int low = 0, mid = 0, high = nums.length - 1;
    
    while (mid <= high) {
        switch (nums[mid]) {
            case 0: swap(nums, low++, mid++); break;
            case 1: mid++; break;
            case 2: swap(nums, mid, high--); break;
        }
    }
}

// Generalized: partition around pivot
// Used in QuickSort's 3-way partition for arrays with many duplicates
```

**Key Takeaway**: Three pointers: `low` (boundary of 0s), `mid` (current), `high` (boundary of 2s). No extra space needed."""),

# ═══════════════════════════════════════════════════════════════
# MORE SYSTEM DESIGN (13 more → 20 total)
# ═══════════════════════════════════════════════════════════════
("system-design","Rate Limiting Algorithms","""Control API request rates.

| Algorithm | How | Pros | Cons |
|:---|:---|:---|:---|
| Token Bucket | Bucket fills at fixed rate | Handles bursts | Memory per user |
| Leaky Bucket | Queue processes at fixed rate | Smooth output | No burst handling |
| Fixed Window | Count per time window | Simple | Boundary spike |
| Sliding Window | Rolling time window | Accurate | More memory |

```python
# Token Bucket (pseudocode)
class TokenBucket:
    def __init__(self, rate, capacity):
        self.tokens = capacity
        self.rate = rate  # tokens per second
        self.last_refill = time.now()
    
    def allow_request(self):
        self.refill()
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False
    
    def refill(self):
        elapsed = time.now() - self.last_refill
        self.tokens = min(self.capacity, self.tokens + elapsed * self.rate)
        self.last_refill = time.now()
```

**Key Takeaway**: Token Bucket is most common (AWS, Stripe use it). Use Redis for distributed rate limiting across multiple servers."""),

("system-design","WebSocket vs SSE vs Polling","""Real-time communication patterns.

| Method | Direction | Use Case |
|:---|:---|:---|
| Short Polling | Client → Server (repeated) | Simple status checks |
| Long Polling | Client waits for response | Chat (fallback) |
| SSE | Server → Client (one-way) | Notifications, live feed |
| WebSocket | Bidirectional | Chat, gaming, collaboration |

```javascript
// SSE (Server-Sent Events) — simple one-way streaming
// Server
app.get('/events', (req, res) => {
  res.setHeader('Content-Type', 'text/event-stream');
  res.setHeader('Cache-Control', 'no-cache');
  
  const interval = setInterval(() => {
    res.write(`data: ${JSON.stringify({ time: Date.now() })}\\n\\n`);
  }, 1000);
  
  req.on('close', () => clearInterval(interval));
});

// Client
const source = new EventSource('/events');
source.onmessage = (e) => console.log(JSON.parse(e.data));
```

**Key Takeaway**: Use SSE for server → client streaming (simpler than WebSocket). Use WebSocket only when client needs to send data too."""),

("system-design","CQRS Pattern","""Separate read and write models.

```
Write (Command):
Client → API → Command Handler → Write DB (normalized)
                                    ↓ (events)
Read (Query):                   Event Handler
Client → API → Query Handler → Read DB (denormalized, optimized for queries)
```

### Example: E-commerce
```
Write DB (MySQL):               Read DB (Elasticsearch/Redis):
┌─────────┐ ┌──────────┐       ┌─────────────────────┐
│ orders  │ │ products │  →    │ product_search_view  │
│ items   │ │ reviews  │  →    │ (pre-joined, cached) │
│ users   │ └──────────┘       └─────────────────────┘
└─────────┘
```

### When to Use
- Read/write patterns are very different
- Need different optimization for reads vs writes
- High read:write ratio (100:1)
- Complex queries that are expensive on normalized data

**Key Takeaway**: CQRS adds complexity. Use only when read and write loads/patterns are significantly different."""),

("system-design","Distributed Locks","""Coordinate access across multiple servers.

```java
// Redis distributed lock (Redisson)
RLock lock = redissonClient.getLock("order:" + orderId);

try {
    // Wait max 5s to acquire, auto-release after 30s
    if (lock.tryLock(5, 30, TimeUnit.SECONDS)) {
        try {
            processOrder(orderId);
        } finally {
            lock.unlock();
        }
    } else {
        throw new ConcurrencyException("Could not acquire lock");
    }
} catch (InterruptedException e) {
    Thread.currentThread().interrupt();
}
```

### Redis SET NX (simple version)
```
SET lock:order:123 "server1" NX PX 30000
# NX = only if not exists
# PX = auto-expire in 30 seconds
```

### Redlock Algorithm (for Redis cluster)
1. Try to acquire lock on N/2+1 Redis nodes
2. If majority acquired within timeout → lock acquired
3. Release on ALL nodes when done

**Key Takeaway**: Always set TTL on locks (prevent deadlocks). Use Redisson library — don't implement from scratch."""),

("system-design","Database Replication","""Improve read performance and availability.

```
Master-Slave (Single Master):
┌────────┐ writes ┌────────┐
│ Client │ ──────→│ Master │──┐
└────────┘        └────────┘  │ replicate
     │                        ↓
     │ reads   ┌─────────┐ ┌─────────┐
     └────────→│ Slave 1 │ │ Slave 2 │
               └─────────┘ └─────────┘
```

### Types
| Type | Latency | Consistency |
|:---|:---|:---|
| Synchronous | Higher | Strong |
| Asynchronous | Lower | Eventual |
| Semi-sync | Medium | At least 1 replica |

### MySQL Replication
```sql
-- On Master
SHOW MASTER STATUS;

-- On Slave
CHANGE MASTER TO
  MASTER_HOST='master-ip',
  MASTER_USER='repl_user',
  MASTER_LOG_FILE='mysql-bin.000001',
  MASTER_LOG_POS=107;
START SLAVE;
```

**Key Takeaway**: Use replication for read scaling and HA. Route writes to master, reads to slaves. Handle replication lag in application code."""),

("system-design","Idempotency in APIs","""Same request, same result — no side effects.

```java
@PostMapping("/api/payments")
public ResponseEntity<Payment> createPayment(
        @RequestHeader("Idempotency-Key") String idempotencyKey,
        @RequestBody PaymentRequest request) {
    
    // Check if already processed
    Optional<Payment> existing = paymentRepo.findByIdempotencyKey(idempotencyKey);
    if (existing.isPresent()) {
        return ResponseEntity.ok(existing.get()); // return cached result
    }
    
    // Process new payment
    Payment payment = paymentService.charge(request);
    payment.setIdempotencyKey(idempotencyKey);
    paymentRepo.save(payment);
    
    return ResponseEntity.status(201).body(payment);
}
```

### HTTP Method Idempotency
| Method | Idempotent | Safe |
|:---|:---|:---|
| GET | Yes | Yes |
| PUT | Yes | No |
| DELETE | Yes | No |
| POST | **No** | No |
| PATCH | **No** | No |

**Key Takeaway**: Always make payment/order APIs idempotent. Use client-generated UUID as idempotency key. Store and check before processing."""),

("system-design","N+1 Query Problem","""Most common database performance issue.

```java
// N+1 PROBLEM: 1 query for authors + N queries for books
List<Author> authors = authorRepo.findAll(); // 1 query
for (Author a : authors) {
    List<Book> books = a.getBooks(); // N queries (lazy loading!)
}

// FIX 1: JOIN FETCH
@Query("SELECT a FROM Author a JOIN FETCH a.books")
List<Author> findAllWithBooks(); // 1 query!

// FIX 2: Entity Graph
@EntityGraph(attributePaths = {"books"})
List<Author> findAll();

// FIX 3: Batch fetching
@BatchSize(size = 25) // fetch books in batches of 25
@OneToMany(mappedBy = "author")
private List<Book> books;
```

### How to Detect
- Enable `spring.jpa.show-sql=true` in dev
- Check for repeated queries in logs
- Use tools: p6spy, Hibernate Statistics

**Key Takeaway**: N+1 turns 1 query into 101 queries for 100 records. Always use JOIN FETCH or @EntityGraph for collections you'll access."""),

# ═══════════════════════════════════════════════════════════════
# MORE DEVOPS (7 more → 10 total)
# ═══════════════════════════════════════════════════════════════
("devops","Kubernetes Basics - Pods and Deployments","""Container orchestration fundamentals.

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  selector:
    matchLabels: { app: my-app }
  template:
    metadata:
      labels: { app: my-app }
    spec:
      containers:
        - name: app
          image: myapp:1.0.0
          ports: [{ containerPort: 8080 }]
          resources:
            requests: { cpu: "100m", memory: "128Mi" }
            limits: { cpu: "500m", memory: "512Mi" }
          livenessProbe:
            httpGet: { path: /health, port: 8080 }
            initialDelaySeconds: 30
---
apiVersion: v1
kind: Service
metadata:
  name: my-app-svc
spec:
  selector: { app: my-app }
  ports: [{ port: 80, targetPort: 8080 }]
  type: ClusterIP
```

```bash
kubectl apply -f deployment.yaml
kubectl get pods
kubectl logs my-app-xxx
kubectl scale deployment my-app --replicas=5
```"""),

("devops","Nginx Reverse Proxy","""Route traffic and terminate SSL.

```nginx
# /etc/nginx/sites-available/myapp
server {
    listen 80;
    server_name myapp.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl;
    server_name myapp.com;
    
    ssl_certificate /etc/letsencrypt/live/myapp.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/myapp.com/privkey.pem;
    
    # Frontend
    location / {
        root /var/www/myapp/build;
        try_files $uri /index.html;  # SPA routing
    }
    
    # Backend API
    location /api/ {
        proxy_pass http://localhost:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    # WebSocket
    location /ws/ {
        proxy_pass http://localhost:8080;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

**Key Takeaway**: Nginx handles SSL termination, static files, and routing to backend. Use `try_files` for SPA routing (React, Angular)."""),

("devops","Dockerfile Best Practices","""Write efficient, secure Docker images.

```dockerfile
# 1. Use specific base image tags (not :latest)
FROM node:20-alpine AS builder

# 2. Set working directory
WORKDIR /app

# 3. Copy dependency files FIRST (cache layers)
COPY package*.json ./
RUN npm ci --only=production

# 4. Copy source code AFTER dependencies
COPY . .
RUN npm run build

# 5. Multi-stage: production image
FROM node:20-alpine
WORKDIR /app
RUN addgroup -S app && adduser -S app -G app  # non-root user
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
USER app
EXPOSE 3000
CMD ["node", "dist/index.js"]
```

### Rules
1. Use `.dockerignore` (exclude node_modules, .git)
2. One process per container
3. Use `COPY` over `ADD`
4. Don't run as root
5. Pin dependency versions
6. Minimize layers (combine RUN commands)

**Key Takeaway**: Layer ordering matters for cache. Dependencies change less often than code — copy them first."""),

# ═══════════════════════════════════════════════════════════════
# MORE GIT (7 more → 10 total)
# ═══════════════════════════════════════════════════════════════
("git","Git Cherry-Pick","""Apply specific commits to another branch.

```bash
# Pick a single commit
git cherry-pick abc1234

# Pick multiple commits
git cherry-pick abc1234 def5678

# Pick a range
git cherry-pick abc1234..ghi9012

# Cherry-pick without committing (stage only)
git cherry-pick --no-commit abc1234

# Resolve conflicts during cherry-pick
git cherry-pick abc1234
# ... fix conflicts ...
git add .
git cherry-pick --continue
# Or abort
git cherry-pick --abort
```

### When to Use
- Backport a bug fix from develop to release branch
- Apply a specific feature commit without merging entire branch
- Recover a commit from a deleted branch

**Key Takeaway**: Cherry-pick creates a NEW commit (different hash) with same changes. Don't cherry-pick commits that will later be merged — you'll get duplicates."""),

("git","Git Bisect - Find Bug-Introducing Commit","""Binary search through commit history.

```bash
# Start bisect
git bisect start

# Current commit is broken
git bisect bad

# This old commit was fine
git bisect good v1.2.0

# Git checks out middle commit — test it
# If broken:
git bisect bad
# If working:
git bisect good

# Git narrows down until it finds the exact commit
# "abc1234 is the first bad commit"

# Done
git bisect reset

# AUTOMATED bisect with a test script!
git bisect start HEAD v1.2.0
git bisect run npm test
# Git automatically runs tests on each commit!
```

**Key Takeaway**: Bisect finds the bug in O(log n) steps. With `bisect run`, it's fully automatic — just provide a test script."""),

("git","Git Hooks for Automation","""Run scripts on Git events.

```bash
# .git/hooks/pre-commit (runs before every commit)
#!/bin/sh
npm run lint
if [ $? -ne 0 ]; then
    echo "Lint failed. Fix errors before committing."
    exit 1
fi

# .git/hooks/commit-msg (validate commit message)
#!/bin/sh
MSG=$(cat "$1")
if ! echo "$MSG" | grep -qE "^(feat|fix|docs|refactor|test|chore):"; then
    echo "Error: Commit must start with feat:|fix:|docs:|refactor:|test:|chore:"
    exit 1
fi
```

### Husky (team-wide hooks via npm)
```json
// package.json
{
  "husky": { "hooks": { "pre-commit": "lint-staged" } },
  "lint-staged": { "*.{js,jsx}": ["eslint --fix", "prettier --write"] }
}
```

**Key Takeaway**: Use Husky + lint-staged for team-wide hooks. Local hooks live in `.git/hooks/` and aren't shared — Husky solves this."""),

("git","Git Stash Advanced Usage","""Save work-in-progress without committing.

```bash
# Stash with description
git stash push -m "WIP: user authentication"

# Stash specific files
git stash push -m "WIP: styling" -- src/styles.css src/App.css

# Include untracked files
git stash push --include-untracked -m "WIP: new feature"

# List all stashes
git stash list
# stash@{0}: On feature: WIP: user authentication
# stash@{1}: On main: WIP: styling

# Apply (keep in stash) vs Pop (remove from stash)
git stash apply stash@{0}
git stash pop stash@{1}

# Show stash diff
git stash show -p stash@{0}

# Create branch from stash
git stash branch new-feature stash@{0}

# Drop specific stash
git stash drop stash@{0}
# Clear all stashes
git stash clear
```

**Key Takeaway**: Use `push -m` instead of just `stash` — descriptive messages help when you have multiple stashes."""),

("git","Conventional Commits","""Standardized commit messages for automation.

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

### Types
| Type | When |
|:---|:---|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `style` | Formatting (no code change) |
| `refactor` | Code change (no feature/fix) |
| `test` | Adding tests |
| `chore` | Build, CI, tooling |
| `perf` | Performance improvement |

### Examples
```
feat(auth): add Google OAuth login
fix(cart): prevent negative quantity
docs(readme): update installation steps
refactor(api): extract validation middleware
test(user): add integration tests for signup
feat!: drop support for Node 14  (BREAKING CHANGE)
```

**Key Takeaway**: Conventional commits enable auto-generated changelogs and semantic versioning. Tools: commitlint, standard-version."""),

# ═══════════════════════════════════════════════════════════════
# HTML/CSS — 5 topics
# ═══════════════════════════════════════════════════════════════
("html-css","CSS Flexbox Layout","""One-dimensional layout (row or column).

```css
.container {
  display: flex;
  flex-direction: row;       /* row | column */
  justify-content: center;   /* main axis */
  align-items: center;       /* cross axis */
  gap: 16px;                 /* spacing between items */
  flex-wrap: wrap;           /* allow wrapping */
}

.item {
  flex: 1;                   /* grow equally */
  flex: 0 0 200px;           /* fixed width, no grow/shrink */
}

/* Common patterns */
/* Navbar: logo left, links right */
.navbar { display: flex; justify-content: space-between; align-items: center; }

/* Center anything */
.center { display: flex; justify-content: center; align-items: center; min-height: 100vh; }

/* Card grid */
.grid { display: flex; flex-wrap: wrap; gap: 20px; }
.card { flex: 1 1 300px; } /* min 300px, grow to fill */
```

**Key Takeaway**: Flexbox = 1D layout. Use `justify-content` for main axis, `align-items` for cross axis. Use Grid for 2D layouts."""),

("html-css","CSS Grid Layout","""Two-dimensional layout system.

```css
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);    /* 3 equal columns */
  grid-template-rows: auto 1fr auto;         /* header, content, footer */
  gap: 20px;
  min-height: 100vh;
}

/* Named areas (dashboard layout) */
.dashboard {
  display: grid;
  grid-template-areas:
    "header header header"
    "sidebar main  aside"
    "footer footer footer";
  grid-template-columns: 250px 1fr 200px;
  grid-template-rows: 60px 1fr 40px;
}
.header  { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main    { grid-area: main; }

/* Responsive without media queries! */
.auto-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
}

/* Span multiple cells */
.featured { grid-column: span 2; grid-row: span 2; }
```

**Key Takeaway**: `auto-fit` + `minmax()` creates responsive grids without media queries. Use Grid for page layouts, Flexbox for component layouts."""),

("html-css","CSS Variables and Custom Properties","""Dynamic, reusable values in CSS.

```css
:root {
  /* Colors */
  --primary: #6366f1;
  --primary-light: #818cf8;
  --bg-dark: #0f172a;
  --text: #e2e8f0;
  
  /* Spacing */
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 32px;
  
  /* Typography */
  --font-sans: 'Inter', system-ui, sans-serif;
  --font-mono: 'Fira Code', monospace;
  
  /* Shadows */
  --shadow: 0 4px 6px -1px rgba(0,0,0,0.3);
  --radius: 12px;
}

.card {
  background: var(--bg-dark);
  color: var(--text);
  padding: var(--space-md);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  font-family: var(--font-sans);
}

/* Override in context */
.card:hover { --shadow: 0 8px 16px rgba(99,102,241,0.3); }

/* Dark/Light theme toggle */
[data-theme="light"] {
  --bg-dark: #ffffff;
  --text: #1e293b;
}
```

**Key Takeaway**: CSS variables enable theming (dark/light mode) with a single attribute change. They cascade and can be changed via JavaScript."""),

("html-css","CSS Animations and Transitions","""Add motion and interactivity.

```css
/* Transition: smooth property change */
.button {
  background: #6366f1;
  transform: translateY(0);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.button:hover {
  background: #818cf8;
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(99,102,241,0.4);
}

/* Keyframe animation */
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

.card {
  animation: fadeInUp 0.5s ease-out forwards;
  animation-delay: calc(var(--index) * 0.1s);
}

/* Pulse animation */
@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.05); }
}
.notification-dot {
  animation: pulse 2s infinite;
}

/* Skeleton loading */
@keyframes shimmer {
  0% { background-position: -200px 0; }
  100% { background-position: 200px 0; }
}
.skeleton {
  background: linear-gradient(90deg, #1e293b 25%, #334155 50%, #1e293b 75%);
  background-size: 400px 100%;
  animation: shimmer 1.5s infinite linear;
}
```"""),

("html-css","CSS Media Queries and Responsive Design","""Adapt layouts to different screens.

```css
/* Mobile First approach */
.container { padding: 16px; }
.grid { display: grid; grid-template-columns: 1fr; gap: 16px; }

/* Tablet */
@media (min-width: 768px) {
  .container { padding: 24px; max-width: 768px; margin: 0 auto; }
  .grid { grid-template-columns: repeat(2, 1fr); }
  .mobile-only { display: none; }
}

/* Desktop */
@media (min-width: 1024px) {
  .container { max-width: 1200px; }
  .grid { grid-template-columns: repeat(3, 1fr); gap: 24px; }
}

/* Dark mode (system preference) */
@media (prefers-color-scheme: dark) {
  :root { --bg: #0f172a; --text: #e2e8f0; }
}

/* Reduced motion (accessibility) */
@media (prefers-reduced-motion: reduce) {
  * { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
}

/* Container queries (modern!) */
@container (min-width: 400px) {
  .card { flex-direction: row; }
}
```

**Key Takeaway**: Design mobile-first, enhance with `min-width` queries. Always respect `prefers-reduced-motion` for accessibility."""),
]

# Spring Boot Integration Testing

> _2026-06-18_ | Category: **spring-boot**

Test full application context.

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

**Key Takeaway**: Use `@SpringBootTest` for integration, `@WebMvcTest` for controller unit tests. Always clean DB between tests.

# Spring Boot Testing with MockMvc

> _2026-08-29_ | Category: **spring-boot**

Test REST controllers without starting a server.

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
```

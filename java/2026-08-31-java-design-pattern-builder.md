# Java Design Pattern - Builder

> _2026-08-31_ | Category: **java**

Construct complex objects step by step.

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
    .body("{"name":"Dipak"}")
    .build();
```

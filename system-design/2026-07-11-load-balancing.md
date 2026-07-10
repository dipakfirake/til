# Load Balancing

> _2026-07-11_ | Category: **system-design**

Distribute traffic across servers.

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

**Key Takeaway**: Use L7 load balancers for web apps (URL-based routing, SSL termination). L4 for raw TCP throughput.

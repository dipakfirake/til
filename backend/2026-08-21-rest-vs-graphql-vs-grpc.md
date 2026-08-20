# REST vs GraphQL vs gRPC

> _2026-08-21_ | Category: **backend**

API Architectures.

| Feature | REST | GraphQL | gRPC |
|:---|:---|:---|:---|
| Protocol | HTTP/1.1 | HTTP/1.1 | HTTP/2 |
| Data Format| JSON | JSON | Protobuf (Binary) |
| Overfetching| Yes | No (Client specifies) | No |
| Best For | Public APIs, CRUD | Complex UIs, Mobile | Internal Microservices |

**GraphQL**: One endpoint `/graphql`. Client queries exactly what it wants: `query { user(id:1) { name, posts { title } } }`. Fixes underfetching/overfetching.
**gRPC**: Created by Google. Uses Protocol Buffers (strongly typed). Binary format makes it 10x faster and smaller than JSON. Ideal for fast service-to-service communication.

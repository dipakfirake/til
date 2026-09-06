# API Design Best Practices

> _2026-09-07_ | Category: **system-design**

Design clean, consistent REST APIs.

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
5. Pagination, filtering, sorting as query params

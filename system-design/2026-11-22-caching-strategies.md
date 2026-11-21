# Caching Strategies

> _2026-11-22_ | Category: **system-design**

Speed up reads and reduce database load.

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

**Key Takeaway**: "There are only two hard things in CS: cache invalidation and naming things." Start with TTL-based, add event-based for hot paths.

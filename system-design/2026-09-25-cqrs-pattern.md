# CQRS Pattern

> _2026-09-25_ | Category: **system-design**

Separate read and write models.

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

**Key Takeaway**: CQRS adds complexity. Use only when read and write loads/patterns are significantly different.

# Git Branching Strategies

> _2026-06-14_ | Category: **git**

Organize team development with branching models.

### Git Flow
```
main ──────────────────────── production
  └─ develop ─────────────── integration
       ├─ feature/login ──── new feature
       ├─ feature/cart ────── new feature
       └─ release/1.0 ────── staging
  └─ hotfix/bug-123 ──────── urgent fix
```

### Trunk-Based Development
```
main ──────────────────────── always deployable
  ├─ short-lived branch (1-2 days max)
  └─ feature flags for incomplete features
```

| Strategy | Best For |
|:---|:---|
| Git Flow | Release-based products |
| Trunk-Based | CI/CD, SaaS, startups |
| GitHub Flow | Open source, simple |

**Key Takeaway**: Trunk-based is modern best practice. Keep branches short-lived (< 2 days). Use feature flags over long-lived branches.

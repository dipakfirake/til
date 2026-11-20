# Git Hooks for Automation

> _2026-11-21_ | Category: **git**

Run scripts on Git events.

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

**Key Takeaway**: Use Husky + lint-staged for team-wide hooks. Local hooks live in `.git/hooks/` and aren't shared — Husky solves this.

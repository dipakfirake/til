# Git Cherry-Pick

> _2026-09-08_ | Category: **git**

Apply specific commits to another branch.

```bash
# Pick a single commit
git cherry-pick abc1234

# Pick multiple commits
git cherry-pick abc1234 def5678

# Pick a range
git cherry-pick abc1234..ghi9012

# Cherry-pick without committing (stage only)
git cherry-pick --no-commit abc1234

# Resolve conflicts during cherry-pick
git cherry-pick abc1234
# ... fix conflicts ...
git add .
git cherry-pick --continue
# Or abort
git cherry-pick --abort
```

### When to Use
- Backport a bug fix from develop to release branch
- Apply a specific feature commit without merging entire branch
- Recover a commit from a deleted branch

**Key Takeaway**: Cherry-pick creates a NEW commit (different hash) with same changes. Don't cherry-pick commits that will later be merged — you'll get duplicates.

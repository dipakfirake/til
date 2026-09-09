# Git Rebase vs Merge

> _2026-09-10_ | Category: **git**

Two ways to integrate changes.

```bash
# Merge: preserves complete history
git checkout main
git merge feature    # creates merge commit

# Rebase: linear history
git checkout feature
git rebase main      # replay commits on top of main

# Interactive rebase: clean up before merging
git rebase -i HEAD~3
# pick abc1234 Add user model
# squash def5678 Fix typo        ← combine with previous
# pick ghi9012 Add user API
```

### Golden Rule
> **Never rebase shared/public branches.** Only rebase YOUR local feature branch.

### My Workflow
1. Work on feature branch
2. `git rebase main` to get latest
3. `git rebase -i` to squash messy commits
4. Create PR with clean history

**Key Takeaway**: Rebase for clean history on YOUR branches. Merge for shared branches. Never force-push to main.

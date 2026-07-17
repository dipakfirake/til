# Essential Git Commands

> _2026-07-18_ | Category: **git**

Commands that save hours.

```bash
# Undo last commit (keep changes staged)
git reset --soft HEAD~1

# Unstage file
git restore --staged file.txt

# Discard local changes
git restore file.txt

# Stash with message
git stash push -m "WIP: feature"
git stash list
git stash pop stash@{0}

# Find which commit introduced a bug
git bisect start
git bisect bad           # current is broken
git bisect good abc123   # this was fine
# Git binary searches through history!

# Cherry-pick specific commit
git cherry-pick abc1234

# Pretty log
git log --oneline --graph --all -20

# See what changed
git diff --stat HEAD~5..HEAD
```

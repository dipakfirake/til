# Git Stash Advanced Usage

> _2026-07-13_ | Category: **git**

Save work-in-progress without committing.

```bash
# Stash with description
git stash push -m "WIP: user authentication"

# Stash specific files
git stash push -m "WIP: styling" -- src/styles.css src/App.css

# Include untracked files
git stash push --include-untracked -m "WIP: new feature"

# List all stashes
git stash list
# stash@{0}: On feature: WIP: user authentication
# stash@{1}: On main: WIP: styling

# Apply (keep in stash) vs Pop (remove from stash)
git stash apply stash@{0}
git stash pop stash@{1}

# Show stash diff
git stash show -p stash@{0}

# Create branch from stash
git stash branch new-feature stash@{0}

# Drop specific stash
git stash drop stash@{0}
# Clear all stashes
git stash clear
```

**Key Takeaway**: Use `push -m` instead of just `stash` — descriptive messages help when you have multiple stashes.

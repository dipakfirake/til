# Git Bisect - Find Bug-Introducing Commit

> _2026-09-15_ | Category: **git**

Binary search through commit history.

```bash
# Start bisect
git bisect start

# Current commit is broken
git bisect bad

# This old commit was fine
git bisect good v1.2.0

# Git checks out middle commit — test it
# If broken:
git bisect bad
# If working:
git bisect good

# Git narrows down until it finds the exact commit
# "abc1234 is the first bad commit"

# Done
git bisect reset

# AUTOMATED bisect with a test script!
git bisect start HEAD v1.2.0
git bisect run npm test
# Git automatically runs tests on each commit!
```

**Key Takeaway**: Bisect finds the bug in O(log n) steps. With `bisect run`, it's fully automatic — just provide a test script.

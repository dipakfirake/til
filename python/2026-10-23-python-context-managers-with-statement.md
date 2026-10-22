# Python Context Managers (with statement)

> _2026-10-23_ | Category: **python**

Resource management made safe.

```python
# Standard usage
with open("data.txt", "w") as f:
    f.write("Hello")
# f is automatically closed here, even if exception occurs!

# Creating custom context manager (Class based)
class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Elapsed: {time.time() - self.start}")

with Timer():
    time.sleep(1)

# Using contextlib (Generator based)
from contextlib import contextmanager

@contextmanager
def open_file(path, mode):
    f = open(path, mode)
    try:
        yield f
    finally:
        f.close()
```

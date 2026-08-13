# Event Sourcing

> _2026-08-14_ | Category: **system-design**

Store state as a sequence of events.

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
- Usually paired with CQRS.

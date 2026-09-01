# Leader Election

> _2026-09-02_ | Category: **system-design**

Who is in charge of the cluster?

In distributed systems, you often need ONE node to coordinate tasks (e.g., cron jobs) to avoid duplicate work.

Algorithms:
- **Paxos / Raft**: Consensus algorithms to agree on a leader.
- **ZooKeeper / etcd**: Distributed key-value stores that manage election via ephemeral nodes.

*How ZooKeeper works*:
Nodes try to create a file `/leader`. The first one wins. It holds a session lock. If it crashes, the session dies, the file is deleted, and others try to create it.

**Split Brain**: Network partitions can cause two leaders. Prevented using "Quorum" (N/2 + 1 nodes must agree).

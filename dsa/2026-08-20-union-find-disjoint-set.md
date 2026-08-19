# Union-Find Disjoint Set

> _2026-08-20_ | Category: **dsa**

Track connected components efficiently.

```java
class UnionFind {
    int[] parent, rank;
    int components;
    
    UnionFind(int n) {
        parent = new int[n]; rank = new int[n]; components = n;
        for (int i = 0; i < n; i++) parent[i] = i;
    }
    
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]); // path compression
        return parent[x];
    }
    
    boolean union(int x, int y) {
        int px = find(x), py = find(y);
        if (px == py) return false;
        if (rank[px] < rank[py]) { int t=px; px=py; py=t; }
        parent[py] = px;
        if (rank[px] == rank[py]) rank[px]++;
        components--;
        return true;
    }
}
```

**Use cases**: Number of islands, cycle detection, Kruskal's MST, network connectivity.
**Time**: Nearly O(1) per operation with path compression + union by rank.

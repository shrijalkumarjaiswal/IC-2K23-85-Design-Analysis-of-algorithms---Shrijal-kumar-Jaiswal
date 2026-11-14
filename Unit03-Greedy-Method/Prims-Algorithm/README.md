# Prim's Algorithm - Unit 3: Greedy Method

## Problem Statement

Find Minimum Spanning Tree (MST) of a connected, undirected, weighted graph using Prim's algorithm. MST connects all vertices with minimum total edge weight and no cycles.

## Algorithm / Approach

### Greedy Strategy

**Greedy Choice**: At each step, add the minimum weight edge that connects a vertex in the MST to a vertex outside the MST.

1. Start with any vertex in MST
2. Maintain a set of edges connecting MST vertices to non-MST vertices
3. Repeatedly pick minimum weight edge from this set
4. Add the new vertex to MST
5. Update the set with new edges from the added vertex
6. Stop when all vertices are in MST

### Data Structures

**Priority Queue (Min-Heap)**: O(E log V) - efficient for sparse graphs
- Store edges as (weight, from_vertex, to_vertex)
- Extract min in O(log E)

**Adjacency Matrix + Array**: O(V²) - efficient for dense graphs
- Track minimum key (edge weight) for each non-MST vertex
- Scan all vertices to find minimum

## Pseudocode

### Heap Version (O(E log V))

```
PRIMS_HEAP(graph, start):
    n ← number of vertices
    visited[1..n] ← FALSE
    min_heap ← empty priority queue
    push (0, start, start) to min_heap

    mst_edges ← empty list
    total_weight ← 0

    while min_heap not empty and |mst_edges| < n-1:
        (weight, u, v) ← extract_min(min_heap)

        if visited[v] then continue

        visited[v] ← TRUE

        if u ≠ v then
            add (u, v, weight) to mst_edges
            total_weight ← total_weight + weight
        end if

        for each (neighbor, w) in graph[v]:
            if not visited[neighbor] then
                push (w, v, neighbor) to min_heap
            end if
        end for
    end while

    return mst_edges, total_weight
```

### Matrix Version (O(V²))

```
PRIMS_MATRIX(adj_matrix, start):
    n ← number of vertices
    key[1..n] ← ∞
    parent[1..n] ← -1
    in_mst[1..n] ← FALSE

    key[start] ← 0

    repeat n times:
        // Find minimum key vertex not in MST
        u ← vertex with minimum key[v] where in_mst[v] = FALSE

        in_mst[u] ← TRUE

        for v = 1 to n:
            if adj_matrix[u][v] > 0 and not in_mst[v]
               and adj_matrix[u][v] < key[v] then
                key[v] ← adj_matrix[u][v]
                parent[v] ← u
            end if
        end for
    end repeat

    mst_edges ← empty list
    total_weight ← 0
    for v = 1 to n:
        if parent[v] ≠ -1 then
            add (parent[v], v, adj_matrix[parent[v]][v]) to mst_edges
            total_weight ← total_weight + adj_matrix[parent[v]][v]
        end if
    end for

    return mst_edges, total_weight
```

## Time & Space Complexity

| Implementation | Time | Space |
|----------------|------|-------|
| Min-Heap (Adj List) | O(E log V) | O(V + E) |
| Adjacency Matrix | O(V²) | O(V²) |

## Sample Input / Output

### Example Graph
```
Vertices: A,B,C,D,E,F,G

Edges:
A-B: 4    A-C: 8
B-C: 11   B-D: 8
C-D: 7    C-F: 1    C-G: 2
D-E: 2    D-F: 6
E-F: 10   E-G: 15
F-G: 5
```

### Execution Trace (Heap Version)
```
Start: A (vertex 0)

Step 1: Add A-B (4)     MST: {A,B}
Step 2: Add A-C (8)     MST: {A,B,C}
Step 3: Add C-F (1)     MST: {A,B,C,F}
Step 4: Add C-G (2)     MST: {A,B,C,F,G}
Step 5: Add D-E (2)     MST: {A,B,C,D,E,F,G} wait...
```

Actually correct trace:
```
Heap edges from A: (4,A,B), (8,A,C) → pick A-B(4)
From B: add B-C(11), B-D(8) → heap: (8,A,C), (8,B,D), (11,B,C) → pick A-C(8)
From C: add C-D(7), C-F(1), C-G(2) → heap: (1,C,F), (2,C,G), (7,C-D), (8,B,D), (11,B,C) → pick C-F(1)
From F: add F-D(6), F-E(10), F-G(5) → heap: (2,C,G), (5,F-G), (6,F-D), (7,C-D), (8,B-D)... → pick C-G(2)
From G: add G-E(15) → heap: (5,F-G), (6,F-D), (7,C-D), (8,B-D)... → pick F-G(5)? But G already in MST!
... F-G skipped (G visited)
Pick F-D(6) or C-D(7)? C-D(7) smaller → pick C-D(7)
From D: add D-E(2) → heap: (2,D-E), (5,F-G), (6,F-D), (8,B-D)... → pick D-E(2)
From E: done
```

### Result
```
Edge          Weight
A-B           4
A-C           8
C-F           1
C-G           2
C-D           7
D-E           2
-------------------------
TOTAL WEIGHT  24
```

## Prim's vs Kruskal's

| Aspect | Prim's | Kruskal's |
|--------|--------|-----------|
| Approach | Grow from vertex | Add edges by weight |
| Data Structure | Min-Heap | Union-Find |
| Time (Sparse) | O(E log V) | O(E log E) |
| Time (Dense) | O(V²) | O(E log E) |
| Best For | Dense graphs | Sparse graphs |

## Learning Outcomes

1. **Greedy Choice**: Minimum weight crossing edge
2. **Cut Property**: Lightest edge crossing any cut is in some MST
3. **Two Implementations**: Heap for sparse, matrix for dense
4. **MST Properties**: V-1 edges, connected, acyclic, minimum weight
5. **Applications**: Network design, clustering, approximation algorithms

## Files in this Directory

- `prims.py` - Both heap and matrix implementations with tests
- `README.md` - This documentation

## How to Run

```bash
python prims.py
```

This will:
1. Run textbook example with both implementations
2. Execute additional test cases
3. Compare Prim's vs Kruskal's
4. Run performance benchmarks
5. Display learning outcomes
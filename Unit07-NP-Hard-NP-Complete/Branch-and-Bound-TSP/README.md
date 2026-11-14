# Travelling Salesperson Problem (TSP) using Branch and Bound

## Description
Solves the NP-hard Travelling Salesperson Problem (TSP) using Least-Cost Branch and Bound (LCBB). Lower bounds at each state-space node are computed using reduced cost matrices. Subproblems with lower bounds exceeding the best known tour cost are dynamically pruned.

## Algorithm & Pseudocode
```text
SolveTSP_LCBB(CostMatrix):
    M = initialize_matrix(CostMatrix)
    root_cost = reduce_matrix(M)
    PQ.push(Node(matrix=M, path=[0], level=0, cost=root_cost))
    min_cost = infinity
    while PQ is not empty:
        curr = PQ.pop()
        if curr.cost >= min_cost:
            continue
        if curr.level == N - 1:
            total = curr.cost + curr.matrix[curr.vertex][0]
            if total < min_cost:
                min_cost = total
                best_path = curr.path + [0]
            continue
        for each unvisited vertex v:
            child_matrix = prepare_and_reduce(curr.matrix, curr.vertex, v)
            child_cost = curr.cost + curr.matrix[curr.vertex][v] + reduction
            if child_cost < min_cost:
                PQ.push(Node(child_matrix, curr.path + [v], curr.level + 1, child_cost, v))
```

## Complexity
- **Time Complexity:** $O(2^n \times n^2)$ worst-case; effective pruning drastically reduces explored branches on typical instances.
- **Space Complexity:** $O(n^2 \times 2^n)$ in worst case for matrices stored in priority queue.

## Sample Input / Output
### Input
```python
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
```

### Output
```text
TSP using Branch and Bound (Reduced Cost Matrix):
[0, 10, 15, 20]
[10, 0, 35, 25]
[15, 35, 0, 30]
[20, 25, 30, 0]

Optimal Tour: 0 -> 2 -> 3 -> 1 -> 0
Minimum Tour Cost: 80
```

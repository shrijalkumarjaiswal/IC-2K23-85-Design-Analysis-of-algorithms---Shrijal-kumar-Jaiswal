# Exhaustive Search (Brute Force)

## Description
Exhaustive search is a general problem-solving technique that systematically enumerates all possible candidates for the solution and checks whether each candidate satisfies the problem's statement. Applied here to the NP-hard Travelling Salesperson Problem (TSP).

## Algorithm & Pseudocode
```text
ExhaustiveSearchTSP(graph, start_vertex):
    min_cost = infinity
    best_tour = null
    for each permutation P of vertices {V \ {start_vertex}}:
        tour = [start_vertex] + P + [start_vertex]
        cost = calculate_tour_cost(tour, graph)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
    return best_tour, min_cost
```

## Complexity
- **Time Complexity:** $O((n-1)! \times n) = O(n!)$ for $n$ vertices.
- **Space Complexity:** $O(n)$ to store the current permutation and path.

## Sample Input / Output
### Input
Distance matrix for 4 cities:
```python
dist_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
```

### Output
```text
Optimal TSP Tour: 0 -> 1 -> 3 -> 2 -> 0
Minimum Tour Cost: 80
```


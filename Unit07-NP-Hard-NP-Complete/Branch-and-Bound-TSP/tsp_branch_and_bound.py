"""
Travelling Salesperson Problem (TSP) using Branch and Bound
Implements the classic LC Branch and Bound algorithm using Reduced Cost Matrix.
"""

import heapq
import copy

INF = float('inf')

class Node:
    def __init__(self, matrix, path, level, cost, vertex):
        self.matrix = matrix      # Reduced cost matrix
        self.path = path          # Visited path so far
        self.level = level        # Number of vertices visited
        self.cost = cost          # Lower bound cost of this node
        self.vertex = vertex      # Current vertex

    def __lt__(self, other):
        # Min-heap priority by cost (lower bound)
        return self.cost < other.cost

def reduce_matrix(matrix, n):
    reduction_cost = 0

    # 1. Row reduction
    for i in range(n):
        row_min = min(matrix[i])
        if row_min != INF and row_min > 0:
            reduction_cost += row_min
            for j in range(n):
                if matrix[i][j] != INF:
                    matrix[i][j] -= row_min

    # 2. Column reduction
    for j in range(n):
        col_min = min(matrix[i][j] for i in range(n))
        if col_min != INF and col_min > 0:
            reduction_cost += col_min
            for i in range(n):
                if matrix[i][j] != INF:
                    matrix[i][j] -= col_min

    return reduction_cost

def solve_tsp_branch_and_bound(adj_matrix):
    n = len(adj_matrix)
    
    # Initialize initial matrix (copy and set self-loops to INF)
    init_matrix = copy.deepcopy(adj_matrix)
    for i in range(n):
        for j in range(n):
            if i == j or init_matrix[i][j] == 0:
                init_matrix[i][j] = INF

    root_matrix = copy.deepcopy(init_matrix)
    root_cost = reduce_matrix(root_matrix, n)
    root = Node(root_matrix, [0], 0, root_cost, 0)

    pq = []
    heapq.heappush(pq, root)

    min_tour_cost = INF
    optimal_path = []

    while pq:
        curr = heapq.heappop(pq)

        # If current node lower bound is already >= best known cost, prune
        if curr.cost >= min_tour_cost:
            continue

        # If all vertices visited, return to start vertex 0
        if curr.level == n - 1:
            last_vertex = curr.vertex
            # Cost to return to 0
            if adj_matrix[last_vertex][0] != 0:
                total_cost = curr.cost + curr.matrix[last_vertex][0]
                if total_cost < min_tour_cost:
                    min_tour_cost = total_cost
                    optimal_path = curr.path + [0]
            continue

        # Explore all unvisited adjacent vertices
        for next_vertex in range(n):
            if next_vertex not in curr.path and curr.matrix[curr.vertex][next_vertex] != INF:
                # Prepare child matrix
                child_matrix = copy.deepcopy(curr.matrix)
                edge_cost = curr.matrix[curr.vertex][next_vertex]

                # Set row curr.vertex and col next_vertex to INF
                for k in range(n):
                    child_matrix[curr.vertex][k] = INF
                    child_matrix[k][next_vertex] = INF
                # Prevent returning directly to start prematurely (only before the last city)
                if curr.level < n - 2:
                    child_matrix[next_vertex][0] = INF

                # Reduce child matrix
                child_reduction = reduce_matrix(child_matrix, n)
                child_cost = curr.cost + edge_cost + child_reduction

                if child_cost < min_tour_cost:
                    child_path = curr.path + [next_vertex]
                    child_node = Node(child_matrix, child_path, curr.level + 1, child_cost, next_vertex)
                    heapq.heappush(pq, child_node)

    return optimal_path, min_tour_cost

if __name__ == "__main__":
    # Cost adjacency matrix
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    print("TSP using Branch and Bound (Reduced Cost Matrix):")
    for row in graph:
        print(row)

    path, cost = solve_tsp_branch_and_bound(graph)
    print(f"\nOptimal Tour: {' -> '.join(map(str, path))}")
    print(f"Minimum Tour Cost: {cost}")

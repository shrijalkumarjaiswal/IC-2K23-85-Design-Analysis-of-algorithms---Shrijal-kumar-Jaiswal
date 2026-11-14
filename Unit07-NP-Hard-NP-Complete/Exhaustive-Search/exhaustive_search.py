"""
Exhaustive Search (Brute Force) Demonstration
Demonstrates exhaustive search on the Travelling Salesperson Problem (TSP)
by generating all permutations of vertices to guarantee finding the global optimum.
"""

from itertools import permutations

def tsp_exhaustive_search(graph, start_vertex=0):
    n = len(graph)
    vertices = [i for i in range(n) if i != start_vertex]
    
    min_cost = float('inf')
    best_path = None
    
    # Check every possible tour permutation
    for perm in permutations(vertices):
        current_cost = 0
        current_path = [start_vertex] + list(perm) + [start_vertex]
        possible = True
        
        for i in range(len(current_path) - 1):
            u, v = current_path[i], current_path[i + 1]
            if graph[u][v] == 0 and u != v:
                possible = False
                break
            current_cost += graph[u][v]
            
        if possible and current_cost < min_cost:
            min_cost = current_cost
            best_path = current_path

    return best_path, min_cost

if __name__ == "__main__":
    # Cost adjacency matrix
    dist_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    print("Cost Adjacency Matrix:")
    for row in dist_matrix:
        print(row)
        
    path, cost = tsp_exhaustive_search(dist_matrix, start_vertex=0)
    print(f"\nOptimal TSP Tour: {' -> '.join(map(str, path))}")
    print(f"Minimum Tour Cost: {cost}")


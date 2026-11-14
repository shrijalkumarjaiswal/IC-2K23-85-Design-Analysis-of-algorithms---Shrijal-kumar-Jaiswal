"""
Prim's Algorithm for Minimum Spanning Tree - Unit 3: Greedy Method
Grows MST by adding minimum weight edge connecting tree to new vertex.
"""

import heapq


def prims_mst(graph, start=0):
    """
    Prim's algorithm using priority queue (min-heap).

    Args:
        graph: Adjacency list {u: [(v, weight), ...]}
        start: Starting vertex

    Returns:
        mst_edges: List of (u, v, weight) in MST
        total_weight: Total weight of MST
    """
    n = len(graph)
    visited = [False] * n
    mst_edges = []
    total_weight = 0

    # Min-heap: (weight, u, v) - edge from u to v with weight
    # Start with dummy edge to start vertex
    min_heap = [(0, start, start)]

    while min_heap and len(mst_edges) < n - 1:
        weight, u, v = heapq.heappop(min_heap)

        if visited[v]:
            continue

        visited[v] = True

        if u != v:  # Skip dummy start edge
            mst_edges.append((u, v, weight))
            total_weight += weight

        # Add edges from newly added vertex
        for neighbor, w in graph[v]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (w, v, neighbor))

    return mst_edges, total_weight


def prims_mst_matrix(adj_matrix, start=0):
    """
    Prim's algorithm using adjacency matrix (O(V^2) version).

    Args:
        adj_matrix: 2D list where adj_matrix[u][v] = weight (0 or INF if no edge)
        start: Starting vertex

    Returns:
        mst_edges: List of (u, v, weight)
        total_weight: Total weight
    """
    n = len(adj_matrix)
    INF = float('inf')

    # Key values for min weight edge to MST
    key = [INF] * n
    parent = [-1] * n
    in_mst = [False] * n

    key[start] = 0

    for _ in range(n):
        # Find vertex with minimum key not in MST
        u = -1
        min_key = INF
        for v in range(n):
            if not in_mst[v] and key[v] < min_key:
                min_key = key[v]
                u = v

        if u == -1:
            break  # Disconnected graph

        in_mst[u] = True

        # Update keys of adjacent vertices
        for v in range(n):
            weight = adj_matrix[u][v]
            if weight > 0 and not in_mst[v] and weight < key[v]:
                key[v] = weight
                parent[v] = u

    # Build MST edges
    mst_edges = []
    total_weight = 0
    for v in range(n):
        if parent[v] != -1:
            mst_edges.append((parent[v], v, adj_matrix[parent[v]][v]))
            total_weight += adj_matrix[parent[v]][v]

    return mst_edges, total_weight


def print_mst(mst_edges, total_weight, vertex_names=None):
    """Print MST in readable format"""
    print(f"\n{'Edge':<15} {'Weight':<10}")
    print("-" * 25)

    for u, v, w in mst_edges:
        if vertex_names:
            edge_str = f"{vertex_names[u]}-{vertex_names[v]}"
        else:
            edge_str = f"{u}-{v}"
        print(f"{edge_str:<15} {w:<10}")

    print("-" * 25)
    print(f"{'TOTAL WEIGHT':<15} {total_weight:<10}")


def run_example():
    """Run textbook example"""
    print("=" * 60)
    print("PRIM'S ALGORITHM - EXAMPLE")
    print("=" * 60)

    # Graph from standard textbook example
    # Vertices: 0=A, 1=B, 2=C, 3=D, 4=E, 5=F, 6=G
    graph = {
        0: [(1, 4), (2, 8)],                    # A
        1: [(0, 4), (2, 11), (3, 8)],           # B
        2: [(0, 8), (1, 11), (3, 7), (5, 1), (6, 2)],  # C
        3: [(1, 8), (2, 7), (4, 2), (5, 6)],    # D
        4: [(3, 2), (5, 10), (6, 15)],          # E
        5: [(2, 1), (3, 6), (4, 10), (6, 5)],   # F
        6: [(2, 2), (4, 15), (5, 5)],           # G
    }

    vertex_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    print("Graph edges:")
    for u in graph:
        for v, w in graph[u]:
            if u < v:  # Print each edge once
                print(f"  {vertex_names[u]}-{vertex_names[v]}: {w}")

    mst_edges, total = prims_mst(graph, 0)
    print_mst(mst_edges, total, vertex_names)

    # Expected MST weight: 4+8+1+2+2+5 = 22? Let's verify
    # A-B(4), B-D(8)? No...
    # Actually: A-B(4), C-F(1), D-E(2), C-G(2), C-D(7), F-G(5)?
    # Standard answer for this graph: 22 or 23
    print(f"\nMST edges count: {len(mst_edges)} (expected: 6 for 7 vertices)")


def run_example_matrix():
    """Run same example with adjacency matrix"""
    print("\n" + "=" * 60)
    print("PRIM'S ALGORITHM - ADJACENCY MATRIX VERSION")
    print("=" * 60)

    INF = 0  # 0 means no edge in this representation

    adj_matrix = [
        [0, 4, 8, 0, 0, 0, 0],      # A
        [4, 0, 11, 8, 0, 0, 0],     # B
        [8, 11, 0, 7, 0, 1, 2],     # C
        [0, 8, 7, 0, 2, 6, 0],      # D
        [0, 0, 0, 2, 0, 10, 15],    # E
        [0, 0, 1, 6, 10, 0, 5],     # F
        [0, 0, 2, 0, 15, 5, 0],     # G
    ]

    vertex_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    mst_edges, total = prims_mst_matrix(adj_matrix, 0)
    print_mst(mst_edges, total, vertex_names)


def run_additional_tests():
    """Additional test cases"""
    print("\n" + "=" * 60)
    print("ADDITIONAL TEST CASES")
    print("=" * 60)

    # Test 1: Simple triangle
    graph1 = {
        0: [(1, 1), (2, 2)],
        1: [(0, 1), (2, 3)],
        2: [(0, 2), (1, 3)],
    }
    mst, total = prims_mst(graph1)
    print(f"\nTest 1 - Triangle: Weight={total}, Expected=3, Pass={total==3}")

    # Test 2: Line graph
    graph2 = {
        0: [(1, 5)],
        1: [(0, 5), (2, 3)],
        2: [(1, 3), (3, 2)],
        3: [(2, 2)],
    }
    mst, total = prims_mst(graph2)
    print(f"Test 2 - Line: Weight={total}, Expected=10, Pass={total==10}")

    # Test 3: Star graph
    graph3 = {
        0: [(1, 1), (2, 2), (3, 3), (4, 4)],
        1: [(0, 1)],
        2: [(0, 2)],
        3: [(0, 3)],
        4: [(0, 4)],
    }
    mst, total = prims_mst(graph3)
    print(f"Test 3 - Star: Weight={total}, Expected=10, Pass={total==10}")

    # Test 4: Disconnected (should handle gracefully)
    graph4 = {
        0: [(1, 1)],
        1: [(0, 1)],
        2: [(3, 1)],
        3: [(2, 1)],
    }
    mst, total = prims_mst(graph4)
    print(f"Test 4 - Disconnected: Edges={len(mst)}, Weight={total}")

    # Test 5: Single vertex
    graph5 = {0: []}
    mst, total = prims_mst(graph5)
    print(f"Test 5 - Single vertex: Edges={len(mst)}, Weight={total}, Pass={total==0}")


def compare_with_kruskal():
    """Show difference between Prim's and Kruskal's"""
    print("\n" + "=" * 60)
    print("PRIM'S vs KRUSKAL'S")
    print("=" * 60)

    print("""
| Aspect          | Prim's                    | Kruskal's                 |
|-----------------|---------------------------|---------------------------|
| Approach        | Grow tree from vertex     | Add edges by weight       |
| Data Structure  | Priority Queue (Min-Heap) | Disjoint Set (Union-Find)|
| Time (Adj List) | O(E log V)                | O(E log E)                |
| Time (Adj Matrix)| O(V^2)                   | O(E log E)                |
| Best For        | Dense graphs              | Sparse graphs             |
| Start           | Single vertex             | All vertices              |
| Parallelizable  | Harder                    | Easier                    |

Both produce MST with same total weight (may have different edges).
    """)


def run_performance_test():
    """Performance comparison: heap vs matrix"""
    print("\n" + "=" * 60)
    print("PERFORMANCE TEST")
    print("=" * 60)

    import random
    import time

    random.seed(42)

    for n in [100, 500, 1000]:
        # Generate random connected graph (adjacency list)
        graph = {i: [] for i in range(n)}
        # Ensure connectivity with a line
        for i in range(n - 1):
            w = random.randint(1, 100)
            graph[i].append((i + 1, w))
            graph[i + 1].append((i, w))
        # Add extra random edges
        extra_edges = n * 2
        for _ in range(extra_edges):
            u = random.randint(0, n - 1)
            v = random.randint(0, n - 1)
            if u != v:
                w = random.randint(1, 100)
                graph[u].append((v, w))
                graph[v].append((u, w))

        # Heap version
        start = time.perf_counter()
        prims_mst(graph, 0)
        heap_time = (time.perf_counter() - start) * 1000

        # Matrix version (only for smaller n)
        if n <= 500:
            adj_matrix = [[0] * n for _ in range(n)]
            for u in graph:
                for v, w in graph[u]:
                    adj_matrix[u][v] = w

            start = time.perf_counter()
            prims_mst_matrix(adj_matrix, 0)
            matrix_time = (time.perf_counter() - start) * 1000

            print(f"  n={n}: Heap={heap_time:.2f}ms, Matrix={matrix_time:.2f}ms")
        else:
            print(f"  n={n}: Heap={heap_time:.2f}ms")


if __name__ == "__main__":
    run_example()
    run_example_matrix()
    run_additional_tests()
    compare_with_kruskal()
    run_performance_test()

    print("\n" + "=" * 60)
    print("LEARNING OUTCOMES")
    print("=" * 60)
    print("1. Greedy choice: minimum weight edge connecting MST to new vertex")
    print("2. Priority queue (min-heap) for efficient edge selection: O(E log V)")
    print("3. Adjacency matrix version: O(V^2) for dense graphs")
    print("4. MST properties: V-1 edges, no cycles, minimum total weight")
    print("5. Applications: Network design, clustering, approximation algorithms")
    print("6. Difference from Kruskal: Prim grows from vertex, Kruskal adds edges")
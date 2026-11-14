"""
Kruskal's Algorithm for Minimum Spanning Tree - Unit 3: Greedy Method
Adds edges in increasing weight order, using Union-Find to avoid cycles.
"""

class UnionFind:
    """Disjoint Set Union (Union-Find) with path compression and union by rank"""

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        """Find with path compression"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Union by rank. Returns True if merged, False if already in same set."""
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False

        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        return True


def kruskals_mst(edges, num_vertices):
    """
    Kruskal's algorithm for MST.

    Args:
        edges: List of (u, v, weight) tuples
        num_vertices: Number of vertices in graph

    Returns:
        mst_edges: List of (u, v, weight) in MST
        total_weight: Total weight of MST
    """
    # Sort edges by weight ascending
    sorted_edges = sorted(edges, key=lambda x: x[2])

    uf = UnionFind(num_vertices)
    mst_edges = []
    total_weight = 0

    for u, v, weight in sorted_edges:
        if uf.union(u, v):
            mst_edges.append((u, v, weight))
            total_weight += weight
            if len(mst_edges) == num_vertices - 1:
                break

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
    """Run textbook example (same graph as Prim's for comparison)"""
    print("=" * 60)
    print("KRUSKAL'S ALGORITHM - EXAMPLE")
    print("=" * 60)

    # Same graph as Prim's example
    # Vertices: 0=A, 1=B, 2=C, 3=D, 4=E, 5=F, 6=G
    edges = [
        (0, 1, 4),   # A-B
        (0, 2, 8),   # A-C
        (1, 2, 11),  # B-C
        (1, 3, 8),   # B-D
        (2, 3, 7),   # C-D
        (2, 5, 1),   # C-F
        (2, 6, 2),   # C-G
        (3, 4, 2),   # D-E
        (3, 5, 6),   # D-F
        (4, 5, 10),  # E-F
        (4, 6, 15),  # E-G
        (5, 6, 5),   # F-G
    ]

    vertex_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    num_vertices = 7

    print("Graph edges (sorted by weight):")
    for u, v, w in sorted(edges, key=lambda x: x[2]):
        print(f"  {vertex_names[u]}-{vertex_names[v]}: {w}")

    mst_edges, total = kruskals_mst(edges, num_vertices)
    print_mst(mst_edges, total, vertex_names)

    print(f"\nMST edges count: {len(mst_edges)} (expected: 6 for 7 vertices)")


def run_execution_trace():
    """Show step-by-step execution"""
    print("\n" + "=" * 60)
    print("STEP-BY-STEP EXECUTION TRACE")
    print("=" * 60)

    edges = [
        (0, 1, 4), (0, 2, 8), (1, 2, 11), (1, 3, 8),
        (2, 3, 7), (2, 5, 1), (2, 6, 2), (3, 4, 2),
        (3, 5, 6), (4, 5, 10), (4, 6, 15), (5, 6, 5),
    ]
    vertex_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    sorted_edges = sorted(edges, key=lambda x: x[2])
    uf = UnionFind(7)
    mst_edges = []
    total_weight = 0

    print(f"{'Step':<6} {'Edge':<12} {'Weight':<8} {'Action':<30} {'MST Weight'}")
    print("-" * 75)

    step = 0
    for u, v, w in sorted_edges:
        step += 1
        if uf.union(u, v):
            action = f"Added {vertex_names[u]}-{vertex_names[v]}"
            mst_edges.append((u, v, w))
            total_weight += w
        else:
            action = f"Skipped (cycle: {vertex_names[u]}-{vertex_names[v]})"

        print(f"{step:<6} {vertex_names[u]}-{vertex_names[v]:<10} {w:<8} {action:<30} {total_weight}")

        if len(mst_edges) == 6:
            break

    print("-" * 75)
    print(f"Final MST Weight: {total_weight}")


def run_additional_tests():
    """Additional test cases"""
    print("\n" + "=" * 60)
    print("ADDITIONAL TEST CASES")
    print("=" * 60)

    # Test 1: Simple triangle
    edges1 = [(0, 1, 1), (1, 2, 2), (0, 2, 3)]
    mst, total = kruskals_mst(edges1, 3)
    print(f"\nTest 1 - Triangle: Weight={total}, Expected=3, Pass={total==3}")

    # Test 2: Line graph
    edges2 = [(0, 1, 5), (1, 2, 3), (2, 3, 2)]
    mst, total = kruskals_mst(edges2, 4)
    print(f"Test 2 - Line: Weight={total}, Expected=10, Pass={total==10}")

    # Test 3: Star graph
    edges3 = [(0, 1, 1), (0, 2, 2), (0, 3, 3), (0, 4, 4)]
    mst, total = kruskals_mst(edges3, 5)
    print(f"Test 3 - Star: Weight={total}, Expected=10, Pass={total==10}")

    # Test 4: Disconnected graph
    edges4 = [(0, 1, 1), (2, 3, 1)]
    mst, total = kruskals_mst(edges4, 4)
    print(f"Test 4 - Disconnected: Edges={len(mst)}, Weight={total}")

    # Test 5: Single vertex
    edges5 = []
    mst, total = kruskals_mst(edges5, 1)
    print(f"Test 5 - Single vertex: Edges={len(mst)}, Weight={total}, Pass={total==0}")

    # Test 6: Multiple equal weight edges
    edges6 = [(0, 1, 1), (1, 2, 1), (2, 3, 1), (0, 3, 1)]
    mst, total = kruskals_mst(edges6, 4)
    print(f"Test 6 - Equal weights: Weight={total}, Edges={len(mst)}, Pass={total==3}")


def compare_with_prims():
    """Compare with Prim's on same graph"""
    print("\n" + "=" * 60)
    print("COMPARISON WITH PRIM'S (SAME GRAPH)")
    print("=" * 60)

    edges = [
        (0, 1, 4), (0, 2, 8), (1, 2, 11), (1, 3, 8),
        (2, 3, 7), (2, 5, 1), (2, 6, 2), (3, 4, 2),
        (3, 5, 6), (4, 5, 10), (4, 6, 15), (5, 6, 5),
    ]
    vertex_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    # Kruskal's
    mst_kruskal, total_k = kruskals_mst(edges, 7)

    # Prim's (using adjacency list)
    graph = {i: [] for i in range(7)}
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    import heapq
    def prims_mst(graph, start=0):
        n = len(graph)
        visited = [False] * n
        mst_edges = []
        total_weight = 0
        min_heap = [(0, start, start)]

        while min_heap and len(mst_edges) < n - 1:
            weight, u, v = heapq.heappop(min_heap)
            if visited[v]:
                continue
            visited[v] = True
            if u != v:
                mst_edges.append((u, v, weight))
                total_weight += weight
            for neighbor, w in graph[v]:
                if not visited[neighbor]:
                    heapq.heappush(min_heap, (w, v, neighbor))
        return mst_edges, total_weight

    mst_prim, total_p = prims_mst(graph, 0)

    print("Kruskal's MST:")
    for u, v, w in mst_kruskal:
        print(f"  {vertex_names[u]}-{vertex_names[v]}: {w}")
    print(f"  Total: {total_k}")

    print("\nPrim's MST:")
    for u, v, w in mst_prim:
        print(f"  {vertex_names[u]}-{vertex_names[v]}: {w}")
    print(f"  Total: {total_p}")

    print(f"\nSame total weight: {total_k == total_p}")
    print(f"Same edges: {set(mst_kruskal) == set(mst_prim)}")
    print("(Different MSTs possible with same weight)")


def run_performance_test():
    """Performance test"""
    print("\n" + "=" * 60)
    print("PERFORMANCE TEST")
    print("=" * 60)

    import random
    import time

    random.seed(42)

    for n in [100, 500, 1000, 5000]:
        # Generate random connected graph
        edges = []
        # Ensure connectivity
        for i in range(n - 1):
            w = random.randint(1, 1000)
            edges.append((i, i + 1, w))
        # Add extra edges
        for _ in range(n * 3):
            u = random.randint(0, n - 1)
            v = random.randint(0, n - 1)
            if u != v:
                w = random.randint(1, 1000)
                edges.append((u, v, w))

        start = time.perf_counter()
        mst, total = kruskals_mst(edges, n)
        elapsed = (time.perf_counter() - start) * 1000

        print(f"  n={n:>5}, E={len(edges):>5}: {elapsed:>8.2f} ms, MST edges={len(mst)}")


if __name__ == "__main__":
    run_example()
    run_execution_trace()
    run_additional_tests()
    compare_with_prims()
    run_performance_test()

    print("\n" + "=" * 60)
    print("LEARNING OUTCOMES")
    print("=" * 60)
    print("1. Greedy choice: minimum weight edge that doesn't form cycle")
    print("2. Union-Find (Disjoint Set) for cycle detection: O(alpha(V)) amortized")
    print("3. Time complexity: O(E log E) for sorting + O(E alpha(V)) for union-find")
    print("4. Space complexity: O(V) for union-find structure")
    print("5. MST properties: V-1 edges, no cycles, minimum total weight")
    print("6. Works on disconnected graphs (produces minimum spanning forest)")
    print("7. Easier to parallelize than Prim's")
    print("8. Applications: Network design, clustering, image segmentation")
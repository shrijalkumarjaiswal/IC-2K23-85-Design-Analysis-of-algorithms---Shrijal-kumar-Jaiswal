"""
Graph Representation: Adjacency Matrix and Adjacency List - Unit 5
"""

class GraphMatrix:
    def __init__(self, n, directed=False):
        self.n = n
        self.directed = directed
        self.matrix = [[0] * n for _ in range(n)]

    def add_edge(self, u, v, w=1):
        self.matrix[u][v] = w
        if not self.directed:
            self.matrix[v][u] = w

    def remove_edge(self, u, v):
        self.matrix[u][v] = 0
        if not self.directed:
            self.matrix[v][u] = 0

    def has_edge(self, u, v):
        return self.matrix[u][v] != 0

    def neighbors(self, u):
        return [(v, self.matrix[u][v]) for v in range(self.n) if self.matrix[u][v] != 0]

    def print_matrix(self):
        print("Adjacency Matrix:")
        for row in self.matrix:
            print("  ", row)


class GraphList:
    def __init__(self, n, directed=False):
        self.n = n
        self.directed = directed
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v, w=1):
        self.adj[u].append((v, w))
        if not self.directed:
            self.adj[v].append((u, w))

    def remove_edge(self, u, v):
        self.adj[u] = [(x, w) for x, w in self.adj[u] if x != v]
        if not self.directed:
            self.adj[v] = [(x, w) for x, w in self.adj[v] if x != u]

    def has_edge(self, u, v):
        return any(x == v for x, _ in self.adj[u])

    def neighbors(self, u):
        return self.adj[u]

    def print_list(self):
        print("Adjacency List:")
        for u in range(self.n):
            print(f"  {u}: {self.adj[u]}")


def run_example():
    print("=" * 60)
    print("GRAPH REPRESENTATION")
    print("=" * 60)

    # Same graph both ways
    edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4)]

    g_mat = GraphMatrix(5)
    g_list = GraphList(5)

    for u, v in edges:
        g_mat.add_edge(u, v)
        g_list.add_edge(u, v)

    g_mat.print_matrix()
    print()
    g_list.print_list()

    print(f"\nNeighbors of 1 (matrix): {g_mat.neighbors(1)}")
    print(f"Neighbors of 1 (list):   {g_list.neighbors(1)}")

    print(f"\nHas edge 0-2: {g_mat.has_edge(0, 2)} (matrix), {g_list.has_edge(0, 2)} (list)")
    print(f"Has edge 0-4: {g_mat.has_edge(0, 4)} (matrix), {g_list.has_edge(0, 4)} (list)")


def run_comparison():
    print("\n" + "=" * 60)
    print("COMPARISON")
    print("=" * 60)

    import sys

    # Space
    n = 1000
    edges_dense = n * (n - 1) // 2
    edges_sparse = n * 2

    mat_space = n * n * 8  # bytes for int
    list_space_dense = edges_dense * 2 * 16  # tuple overhead
    list_space_sparse = edges_sparse * 2 * 16

    print(f"Space for n={n}:")
    print(f"  Matrix:           {mat_space / 1e6:.1f} MB (always n²)")
    print(f"  List (dense):     {list_space_dense / 1e6:.1f} MB")
    print(f"  List (sparse):    {list_space_sparse / 1e6:.1f} MB")

    print("\nTime Complexity:")
    print("  | Operation       | Matrix | List (sparse) |")
    print("  |-----------------|--------|---------------|")
    print("  | Add edge        | O(1)   | O(1)          |")
    print("  | Remove edge     | O(1)   | O(deg)        |")
    print("  | Check edge      | O(1)   | O(deg)        |")
    print("  | Iterate neighbors| O(n)   | O(deg)        |")
    print("  | Space           | O(V²)  | O(V+E)        |")

    print("\nUse Matrix: Dense graphs, frequent edge queries")
    print("Use List:   Sparse graphs, traversal algorithms")


if __name__ == "__main__":
    run_example()
    run_comparison()
    print("\nLEARNING: Matrix O(V²) space, List O(V+E) space. List better for sparse.")
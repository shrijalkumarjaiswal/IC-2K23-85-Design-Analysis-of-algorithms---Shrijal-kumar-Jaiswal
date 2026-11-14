"""
Depth First Search (DFS) - Unit 5: Traversal & Search
Stack-based (iterative) and recursive implementations.
"""

import sys
sys.setrecursionlimit(10000)

from collections import deque


def dfs_recursive(graph, start):
    """Recursive DFS. Returns visit order."""
    n = len(graph)
    visited = [False] * n
    order = []

    def dfs(u):
        visited[u] = True
        order.append(u)
        for v, _ in graph[u]:
            if not visited[v]:
                dfs(v)

    dfs(start)
    return order, visited


def dfs_iterative(graph, start):
    """Iterative DFS using explicit stack."""
    n = len(graph)
    visited = [False] * n
    order = []
    stack = [start]

    while stack:
        u = stack.pop()
        if visited[u]:
            continue
        visited[u] = True
        order.append(u)
        # Push neighbors in reverse for consistent order
        for v, _ in reversed(graph[u]):
            if not visited[v]:
                stack.append(v)

    return order, visited


def dfs_iterative_postorder(graph, start):
    """Iterative DFS postorder (process after children)."""
    n = len(graph)
    visited = [False] * n
    postorder = []
    stack = [(start, False)]  # (node, processed_children)

    while stack:
        u, processed = stack.pop()
        if processed:
            postorder.append(u)
            continue
        if visited[u]:
            continue
        visited[u] = True
        stack.append((u, True))
        for v, _ in reversed(graph[u]):
            if not visited[v]:
                stack.append((v, False))

    return postorder, visited


def run_example():
    print("=" * 60)
    print("DFS - EXAMPLE")
    print("=" * 60)

    # Graph: 0-1, 0-2, 1-3, 1-4, 2-5, 2-6
    graph = [
        [(1, 1), (2, 1)],
        [(0, 1), (3, 1), (4, 1)],
        [(0, 1), (5, 1), (6, 1)],
        [(1, 1)],
        [(1, 1)],
        [(2, 1)],
        [(2, 1)],
    ]

    order_r, _ = dfs_recursive(graph, 0)
    order_i, _ = dfs_iterative(graph, 0)
    post, _ = dfs_iterative_postorder(graph, 0)

    print(f"Recursive:   {order_r}")
    print(f"Iterative:   {order_i}")
    print(f"Postorder:   {post}")


def run_tests():
    print("\n" + "=" * 60)
    print("TEST CASES")
    print("=" * 60)

    # Disconnected
    g1 = [[(1, 1)], [(0, 1)], [(3, 1)], [(2, 1)]]
    order_r, vis_r = dfs_recursive(g1, 0)
    order_i, vis_i = dfs_iterative(g1, 0)
    print(f"Disconnected from 0: Rec={order_r}, It={order_i}, Same={order_r==order_i}")

    # Cycle
    g2 = [[(1, 1)], [(2, 1)], [(0, 1)]]
    order_r, _ = dfs_recursive(g2, 0)
    order_i, _ = dfs_iterative(g2, 0)
    print(f"Cycle: Rec={order_r}, It={order_i}")

    # Single node
    g3 = [[]]
    order_r, _ = dfs_recursive(g3, 0)
    order_i, _ = dfs_iterative(g3, 0)
    print(f"Single node: Rec={order_r}, It={order_i}")


def run_performance():
    print("\n" + "=" * 60)
    print("PERFORMANCE")
    print("=" * 60)

    import random, time
    random.seed(42)

    for n, m in [(1000, 5000), (5000, 25000), (10000, 50000)]:
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u = random.randint(0, n - 1)
            v = random.randint(0, n - 1)
            if u != v:
                graph[u].append((v, 1))
                graph[v].append((u, 1))

        for func in [dfs_recursive, dfs_iterative]:
            start = time.perf_counter()
            func(graph, 0)
            elapsed = (time.perf_counter() - start) * 1000
            print(f"  {func.__name__}: V={n}, E={m}: {elapsed:.2f} ms")


if __name__ == "__main__":
    run_example()
    run_tests()
    run_performance()
    print("\nLEARNING: DFS uses stack (recursive call stack or explicit). O(V+E) time.")
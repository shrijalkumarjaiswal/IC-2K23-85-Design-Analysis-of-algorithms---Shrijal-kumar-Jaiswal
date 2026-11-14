"""
Breadth First Search (BFS) - Unit 5: Traversal & Search
Queue-based level-order traversal. Finds shortest path in unweighted graphs.
"""

from collections import deque


def bfs(graph, start):
    """BFS traversal. Returns (order, parent, distance)"""
    n = len(graph)
    visited = [False] * n
    parent = [-1] * n
    distance = [-1] * n
    order = []

    q = deque([start])
    visited[start] = True
    distance[start] = 0

    while q:
        u = q.popleft()
        order.append(u)
        for v, _ in graph[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                distance[v] = distance[u] + 1
                q.append(v)

    return order, parent, distance


def bfs_shortest_path(graph, start, target):
    """Find shortest path from start to target"""
    _, parent, dist = bfs(graph, start)
    if dist[target] == -1:
        return None, -1
    path = []
    v = target
    while v != -1:
        path.append(v)
        v = parent[v]
    path.reverse()
    return path, dist[target]


def run_example():
    print("=" * 60)
    print("BFS - EXAMPLE")
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

    order, parent, dist = bfs(graph, 0)
    print(f"BFS order from 0: {order}")
    print(f"Parent array: {parent}")
    print(f"Distance array: {dist}")

    path, d = bfs_shortest_path(graph, 0, 5)
    print(f"Shortest path 0->5: {path}, distance: {d}")


def run_tests():
    print("\n" + "=" * 60)
    print("TEST CASES")
    print("=" * 60)

    # Disconnected
    g1 = [[(1, 1)], [(0, 1)], [(3, 1)], [(2, 1)]]
    order, _, dist = bfs(g1, 0)
    print(f"Disconnected from 0: {order}, dist[3]={dist[3]} (expected -1)")

    # Single node
    g2 = [[]]
    order, _, dist = bfs(g2, 0)
    print(f"Single node: {order}, dist={dist}")

    # Cycle
    g3 = [[(1, 1)], [(2, 1)], [(0, 1)]]
    order, _, dist = bfs(g3, 0)
    print(f"Cycle: {order}, all visited: {all(d != -1 for d in dist)}")


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

        start = time.perf_counter()
        bfs(graph, 0)
        elapsed = (time.perf_counter() - start) * 1000
        print(f"  V={n}, E={m}: {elapsed:.2f} ms")


if __name__ == "__main__":
    run_example()
    run_tests()
    run_performance()
    print("\nLEARNING: BFS uses queue, O(V+E) time. Finds shortest path in unweighted graphs.")
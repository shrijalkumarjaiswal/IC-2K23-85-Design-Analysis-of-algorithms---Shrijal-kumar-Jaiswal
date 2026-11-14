"""
Single-Source Shortest Path (Bellman-Ford) - Unit 4: Dynamic Programming
Handles negative weights, detects negative cycles. DP: dist[v] = min(dist[v], dist[u] + w)
"""

INF = float('inf')


def bellman_ford(graph, source):
    """O(V*E) time, O(V) space. Returns (dist, parent, has_negative_cycle)"""
    n = len(graph)
    dist = [INF] * n
    parent = [-1] * n
    dist[source] = 0

    # Relax all edges V-1 times
    for _ in range(n - 1):
        updated = False
        for u in range(n):
            for v, w in graph[u]:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    parent[v] = u
                    updated = True
        if not updated:
            break

    # Check for negative cycles
    has_negative_cycle = False
    for u in range(n):
        for v, w in graph[u]:
            if dist[u] != INF and dist[u] + w < dist[v]:
                has_negative_cycle = True

    return dist, parent, has_negative_cycle


def get_path(parent, target):
    """Reconstruct path from source to target"""
    path = []
    v = target
    while v != -1:
        path.append(v)
        v = parent[v]
    path.reverse()
    return path


def run_example():
    print("=" * 60)
    print("BELLMAN-FORD - EXAMPLE")
    print("=" * 60)

    # Graph with negative weight but no negative cycle
    graph = [
        [(1, 6), (2, 7)],          # 0
        [(2, 8), (3, 5), (4, -4)], # 1
        [(3, -3), (4, 9)],         # 2
        [(1, -2)],                 # 3
        [(0, 2), (3, 7)]           # 4
    ]

    dist, parent, neg = bellman_ford(graph, 0)
    print(f"Negative cycle: {neg}")
    print("Distances from source 0:")
    for i, d in enumerate(dist):
        path = get_path(parent, i)
        print(f"  {i}: dist={d}, path={path}")


def run_tests():
    print("\n" + "=" * 60)
    print("TEST CASES")
    print("=" * 60)

    # Positive weights (like Dijkstra)
    g1 = [[(1, 4), (2, 1)], [(3, 1)], [(1, 2), (3, 5)], []]
    d1, _, _ = bellman_ford(g1, 0)
    print(f"Pos weights 0->3: {d1[3]} (expected 3)")

    # Negative cycle
    g2 = [[(1, 1)], [(2, -1)], [(0, -1)]]
    _, _, neg2 = bellman_ford(g2, 0)
    print(f"Negative cycle detected: {neg2}")

    # Disconnected
    g3 = [[(1, 1)], [], [(3, 1)], []]
    d3, _, _ = bellman_ford(g3, 0)
    print(f"Disconnected 0->3: {d3[3] == INF}")


def run_performance():
    print("\n" + "=" * 60)
    print("PERFORMANCE")
    print("=" * 60)

    import random, time
    random.seed(42)

    for n, m in [(100, 500), (200, 1000), (500, 2500)]:
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u = random.randint(0, n - 1)
            v = random.randint(0, n - 1)
            w = random.randint(-10, 10)
            if u != v:
                graph[u].append((v, w))

        start = time.perf_counter()
        bellman_ford(graph, 0)
        elapsed = (time.perf_counter() - start) * 1000
        print(f"  V={n}, E={m}: {elapsed:.2f} ms")


if __name__ == "__main__":
    run_example()
    run_tests()
    run_performance()
    print("\nLEARNING: DP relaxation V-1 times. Time O(VE), handles negative weights")
"""
Floyd-Warshall All-Pairs Shortest Path - Unit 4: Dynamic Programming
DP: dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) for all k
"""

INF = float('inf')


def floyd_warshall(graph):
    """O(V^3) time, O(V^2) space"""
    n = len(graph)
    dist = [row[:] for row in graph]
    nxt = [[-1 if graph[i][j] == INF else j for j in range(n)] for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    nxt[i][j] = nxt[i][k]

    return dist, nxt


def get_path(nxt, u, v):
    """Reconstruct path from u to v"""
    if nxt[u][v] == -1:
        return []
    path = [u]
    while u != v:
        u = nxt[u][v]
        path.append(u)
    return path


def run_example():
    print("=" * 60)
    print("FLOYD-WARSHALL - EXAMPLE")
    print("=" * 60)

    # Graph: 0=A, 1=B, 2=C, 3=D
    graph = [
        [0, 3, INF, 7],
        [8, 0, 2, INF],
        [5, INF, 0, 1],
        [2, INF, INF, 0]
    ]

    dist, nxt = floyd_warshall(graph)

    print("Distance matrix:")
    for row in dist:
        print("  ", [int(x) if x != INF else "INF" for x in row])

    print("\nPaths:")
    for i in range(4):
        for j in range(4):
            if i != j:
                path = get_path(nxt, i, j)
                print(f"  {i}->{j}: {path} (dist={dist[i][j]})")


def run_tests():
    print("\n" + "=" * 60)
    print("TEST CASES")
    print("=" * 60)

    # Triangle
    g1 = [[0, 1, 4], [1, 0, 2], [4, 2, 0]]
    d1, _ = floyd_warshall(g1)
    print(f"Triangle 0-2: {d1[0][2]} (expected 3)")

    # Negative weight (no negative cycle)
    g2 = [[0, -1], [1, 0]]
    d2, _ = floyd_warshall(g2)
    print(f"Negative: {d2[0][1]} (expected -1)")

    # Disconnected
    g3 = [[0, INF], [INF, 0]]
    d3, _ = floyd_warshall(g3)
    print(f"Disconnected: {d3[0][1] == INF}")


def run_performance():
    print("\n" + "=" * 60)
    print("PERFORMANCE")
    print("=" * 60)

    import random, time
    random.seed(42)

    for n in [50, 100, 200]:
        graph = [[0 if i == j else random.randint(1, 100) if random.random() < 0.3 else INF
                  for j in range(n)] for i in range(n)]
        for i in range(n):
            graph[i][i] = 0

        start = time.perf_counter()
        floyd_warshall(graph)
        elapsed = (time.perf_counter() - start) * 1000
        print(f"  n={n}: {elapsed:.2f} ms")


if __name__ == "__main__":
    run_example()
    run_tests()
    run_performance()
    print("\nLEARNING: DP[k][i][j] = min path using vertices 0..k. Time O(V^3)")
"""
Multistage Graph Shortest Path - Unit 4: Dynamic Programming
Find minimum cost path from source to sink in a DAG with stages.
"""

INF = float('inf')


def multistage_forward(graph, stages):
    """Forward DP: cost[v] = min cost from source to v"""
    n = len(graph)
    cost = [INF] * n
    cost[0] = 0
    prev = [-1] * n

    for i in range(1, n):
        # Check incoming edges
        for u in range(n):
            if graph[u][i] != INF and cost[u] != INF:
                if cost[u] + graph[u][i] < cost[i]:
                    cost[i] = cost[u] + graph[u][i]
                    prev[i] = u

    # Reconstruct path
    path = []
    v = n - 1
    while v != -1:
        path.append(v)
        v = prev[v]
    path.reverse()

    return cost[n - 1], path


def multistage_backward(graph, stages):
    """Backward DP: cost[v] = min cost from v to sink"""
    n = len(graph)
    cost = [INF] * n
    cost[n - 1] = 0
    nxt = [-1] * n

    for i in range(n - 2, -1, -1):
        for v in range(n):
            if graph[i][v] != INF and cost[v] != INF:
                if graph[i][v] + cost[v] < cost[i]:
                    cost[i] = graph[i][v] + cost[v]
                    nxt[i] = v

    # Reconstruct path
    path = []
    v = 0
    while v != -1:
        path.append(v)
        v = nxt[v]

    return cost[0], path


def run_example():
    print("=" * 60)
    print("MULTISTAGE GRAPH - EXAMPLE")
    print("=" * 60)

    # 5 stages: S={0}, A={1,2}, B={3,4}, C={5,6}, T={7}
    graph = [
        [INF, 1, 2, INF, INF, INF, INF, INF],   # 0
        [INF, INF, INF, 3, 4, INF, INF, INF],   # 1
        [INF, INF, INF, 5, 1, INF, INF, INF],   # 2
        [INF, INF, INF, INF, INF, 2, 3, INF],   # 3
        [INF, INF, INF, INF, INF, 4, 2, INF],   # 4
        [INF, INF, INF, INF, INF, INF, INF, 3], # 5
        [INF, INF, INF, INF, INF, INF, INF, 2], # 6
        [INF, INF, INF, INF, INF, INF, INF, INF] # 7
    ]

    stages = [{0}, {1, 2}, {3, 4}, {5, 6}, {7}]

    print("Graph edges:")
    for u in range(8):
        for v in range(8):
            if graph[u][v] != INF:
                print(f"  {u} -> {v}: {graph[u][v]}")

    cost_f, path_f = multistage_forward(graph, stages)
    cost_b, path_b = multistage_backward(graph, stages)

    print(f"\nForward DP: cost={cost_f}, path={path_f}")
    print(f"Backward DP: cost={cost_b}, path={path_b}")


def run_tests():
    print("\n" + "=" * 60)
    print("TEST CASES")
    print("=" * 60)

    # Simple 2-stage
    g1 = [[INF, 5], [INF, INF]]
    c1, p1 = multistage_forward(g1, [{0}, {1}])
    print(f"2-stage: {c1} (expected 5)")

    # 3-stage
    g2 = [[INF, 2, 3], [INF, INF, 1], [INF, INF, INF]]
    c2, p2 = multistage_forward(g2, [{0}, {1}, {2}])
    print(f"3-stage: {c2} (expected 3)")


if __name__ == "__main__":
    run_example()
    run_tests()
    print("\nLEARNING: DAG with stages, DP forward/backward O(V+E)")
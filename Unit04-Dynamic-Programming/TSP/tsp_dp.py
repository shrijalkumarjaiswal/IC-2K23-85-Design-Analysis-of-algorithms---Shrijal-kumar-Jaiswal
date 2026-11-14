"""
Traveling Salesman Problem (DP) - Unit 4: Dynamic Programming
Held-Karp algorithm: O(n^2 * 2^n) time, O(n * 2^n) space
"""

INF = float('inf')


def tsp_dp(dist):
    """Held-Karp DP for TSP. Returns (min_cost, path)"""
    n = len(dist)
    # dp[mask][i] = min cost to visit vertices in mask, ending at i
    dp = [[INF] * n for _ in range(1 << n)]
    parent = [[-1] * n for _ in range(1 << n)]

    dp[1][0] = 0  # Start at vertex 0

    for mask in range(1 << n):
        for u in range(n):
            if dp[mask][u] == INF:
                continue
            for v in range(n):
                if mask & (1 << v) == 0:  # v not visited
                    new_mask = mask | (1 << v)
                    new_cost = dp[mask][u] + dist[u][v]
                    if new_cost < dp[new_mask][v]:
                        dp[new_mask][v] = new_cost
                        parent[new_mask][v] = u

    # Find minimum cost returning to start
    full_mask = (1 << n) - 1
    min_cost = INF
    last = -1
    for u in range(1, n):
        cost = dp[full_mask][u] + dist[u][0]
        if cost < min_cost:
            min_cost = cost
            last = u

    # Reconstruct path
    if min_cost == INF:
        return INF, []

    path = [0]
    mask = full_mask
    curr = last
    while curr != 0 and curr != -1:
        path.append(curr)
        prev = parent[mask][curr]
        mask ^= (1 << curr)
        curr = prev
    path.append(0)

    return min_cost, path


def run_example():
    print("=" * 60)
    print("TSP DP (HELD-KARP) - EXAMPLE")
    print("=" * 60)

    # 4 cities
    dist = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    cost, path = tsp_dp(dist)
    print(f"Distance matrix:")
    for row in dist:
        print(f"  {row}")
    print(f"\nMin cost: {cost}")
    print(f"Path: {path}")
    print(f"Expected: 80 (0->1->3->2->0)")


def run_tests():
    print("\n" + "=" * 60)
    print("TEST CASES")
    print("=" * 60)

    # 3 cities triangle
    d1 = [[0, 1, 2], [1, 0, 3], [2, 3, 0]]
    c1, p1 = tsp_dp(d1)
    print(f"3 cities: {c1} (expected 6: 0->1->2->0)")

    # 2 cities
    d2 = [[0, 5], [5, 0]]
    c2, p2 = tsp_dp(d2)
    print(f"2 cities: {c2} (expected 10)")


def run_performance():
    print("\n" + "=" * 60)
    print("PERFORMANCE")
    print("=" * 60)

    import random, time
    random.seed(42)

    for n in [8, 10, 12]:
        dist = [[0 if i == j else random.randint(1, 100) for j in range(n)] for i in range(n)]
        start = time.perf_counter()
        tsp_dp(dist)
        elapsed = (time.perf_counter() - start) * 1000
        print(f"  n={n}: {elapsed:.2f} ms")


if __name__ == "__main__":
    run_example()
    run_tests()
    run_performance()
    print("\nLEARNING: DP[mask][i] = min cost visiting mask ending at i. Time O(n^2 2^n)")
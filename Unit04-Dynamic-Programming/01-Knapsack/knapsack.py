"""
0/1 Knapsack using Dynamic Programming - Unit 4: Dynamic Programming
Items cannot be broken. DP table: dp[i][w] = max value using first i items with weight limit w.
"""

def knapsack_01(values, weights, capacity):
    """DP solution: O(n*W) time, O(n*W) space"""
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    # Traceback to find selected items
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)
            w -= weights[i - 1]

    return dp[n][capacity], selected[::-1], dp


def knapsack_01_optimized(values, weights, capacity):
    """Space optimized: O(n*W) time, O(W) space"""
    n = len(values)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

    return dp[capacity]


def run_example():
    print("=" * 60)
    print("0/1 KNAPSACK - EXAMPLE")
    print("=" * 60)

    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50

    print(f"Items: {list(zip(values, weights))}")
    print(f"Capacity: {capacity}")

    max_val, selected, dp = knapsack_01(values, weights, capacity)
    print(f"\nMax Value: {max_val}")
    print(f"Selected items (indices): {selected}")
    print(f"Selected items: {[(values[i], weights[i]) for i in selected]}")

    # Verify with optimized version
    max_val_opt = knapsack_01_optimized(values, weights, capacity)
    print(f"Optimized version: {max_val_opt}")
    print(f"Match: {max_val == max_val_opt}")


def run_tests():
    print("\n" + "=" * 60)
    print("TEST CASES")
    print("=" * 60)

    # Test 1
    v1, w1 = [10, 40, 30, 50], [5, 4, 6, 3]
    val, sel, _ = knapsack_01(v1, w1, 10)
    print(f"Test 1: Value={val}, Expected=90, Pass={val==90}")

    # Test 2
    v2, w2 = [1, 2, 3], [4, 5, 1]
    val, sel, _ = knapsack_01(v2, w2, 4)
    print(f"Test 2: Value={val}, Expected=3, Pass={val==3}")

    # Test 3: Single item
    val, sel, _ = knapsack_01([100], [10], 5)
    print(f"Test 3: Value={val}, Expected=0, Pass={val==0}")

    # Test 4: Capacity 0
    val, sel, _ = knapsack_01([10, 20], [5, 5], 0)
    print(f"Test 4: Value={val}, Expected=0, Pass={val==0}")


def run_performance():
    print("\n" + "=" * 60)
    print("PERFORMANCE")
    print("=" * 60)

    import random, time
    random.seed(42)

    for n, W in [(50, 1000), (100, 2000), (200, 5000)]:
        values = [random.randint(1, 100) for _ in range(n)]
        weights = [random.randint(1, 50) for _ in range(n)]

        start = time.perf_counter()
        knapsack_01_optimized(values, weights, W)
        elapsed = (time.perf_counter() - start) * 1000
        print(f"  n={n}, W={W}: {elapsed:.2f} ms")


if __name__ == "__main__":
    run_example()
    run_tests()
    run_performance()
    print("\nLEARNING: DP table dp[i][w], time O(nW), space O(nW) or O(W)")
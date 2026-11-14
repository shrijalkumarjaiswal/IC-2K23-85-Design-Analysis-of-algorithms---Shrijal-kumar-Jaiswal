"""
Fibonacci with Recursion vs Memoization vs Tabulation - Unit 4: Dynamic Programming
Demonstrates exponential vs linear time complexity.
"""

import time
import sys
sys.setrecursionlimit(10000)


def fib_recursive(n):
    """Naive recursive: O(2^n) time, O(n) space"""
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_memoized(n, memo=None):
    """Top-down with memoization: O(n) time, O(n) space"""
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        result = n
    else:
        result = fib_memoized(n - 1, memo) + fib_memoized(n - 2, memo)

    memo[n] = result
    return result


def fib_tabulation(n):
    """Bottom-up tabulation: O(n) time, O(n) space"""
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def fib_optimized(n):
    """Space optimized: O(n) time, O(1) space"""
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def run_correctness_tests():
    """Verify all implementations give same results"""
    print("=" * 60)
    print("CORRECTNESS VERIFICATION")
    print("=" * 60)

    test_values = [0, 1, 2, 3, 5, 10, 15, 20, 30]
    expected = [0, 1, 1, 2, 5, 55, 610, 6765, 832040]

    print(f"{'n':>4} | {'Recursive':>12} | {'Memoized':>12} | {'Tabulation':>12} | {'Optimized':>12} | {'Expected':>12}")
    print("-" * 75)

    all_pass = True
    for n, exp in zip(test_values, expected):
        r = fib_recursive(n) if n <= 30 else "SKIP"
        m = fib_memoized(n)
        t = fib_tabulation(n)
        o = fib_optimized(n)

        if isinstance(r, int):
            pass_r = (r == exp)
        else:
            pass_r = True

        pass_m = (m == exp)
        pass_t = (t == exp)
        pass_o = (o == exp)

        all_pass = all_pass and pass_r and pass_m and pass_t and pass_o

        r_str = str(r) if isinstance(r, int) else r
        print(f"{n:>4} | {r_str:>12} | {m:>12} | {t:>12} | {o:>12} | {exp:>12}")

    print("-" * 75)
    print(f"All tests passed: {all_pass}")
    return all_pass


def run_performance_comparison():
    """Compare execution times"""
    print("\n" + "=" * 60)
    print("PERFORMANCE COMPARISON")
    print("=" * 60)

    # Test values for each method (recursive only up to ~35)
    test_sizes = {
        'recursive': [10, 20, 25, 30, 35],
        'memoized': [10, 20, 30, 40, 50, 100, 500, 1000],
        'tabulation': [10, 20, 30, 40, 50, 100, 500, 1000, 5000, 10000],
        'optimized': [10, 20, 30, 40, 50, 100, 500, 1000, 5000, 10000, 50000],
    }

    print("\nRecursive (exponential - very slow):")
    for n in test_sizes['recursive']:
        start = time.perf_counter()
        fib_recursive(n)
        elapsed = (time.perf_counter() - start) * 1000
        print(f"  n={n:>5}: {elapsed:>10.2f} ms")

    print("\nMemoized (linear with recursion overhead):")
    for n in test_sizes['memoized']:
        start = time.perf_counter()
        fib_memoized(n)
        elapsed = (time.perf_counter() - start) * 1000
        print(f"  n={n:>5}: {elapsed:>10.4f} ms")

    print("\nTabulation (bottom-up, no recursion):")
    for n in test_sizes['tabulation']:
        start = time.perf_counter()
        fib_tabulation(n)
        elapsed = (time.perf_counter() - start) * 1000
        print(f"  n={n:>5}: {elapsed:>10.4f} ms")

    print("\nOptimized O(1) space:")
    for n in test_sizes['optimized']:
        start = time.perf_counter()
        fib_optimized(n)
        elapsed = (time.perf_counter() - start) * 1000
        print(f"  n={n:>5}: {elapsed:>10.4f} ms")


def demonstrate_memoization():
    """Show how memoization works"""
    print("\n" + "=" * 60)
    print("MEMOIZATION DEMONSTRATION")
    print("=" * 60)

    # Show call count for recursive vs memoized
    call_count = [0]  # Use list for mutable closure

    def fib_count(n):
        call_count[0] += 1
        if n <= 1:
            return n
        return fib_count(n - 1) + fib_count(n - 2)

    memo = {}
    memo_calls = [0]

    def fib_memo_count(n):
        memo_calls[0] += 1
        if n in memo:
            return memo[n]
        if n <= 1:
            result = n
        else:
            result = fib_memo_count(n - 1) + fib_memo_count(n - 2)
        memo[n] = result
        return result

    n = 10

    call_count[0] = 0
    fib_count(n)
    recursive_calls = call_count[0]

    memo.clear()
    memo_calls[0] = 0
    fib_memo_count(n)
    memoized_calls = memo_calls[0]

    print(f"Computing Fib({n}):")
    print(f"  Recursive calls:     {recursive_calls}")
    print(f"  Memoized calls:      {memoized_calls}")
    print(f"  Reduction:           {recursive_calls / memoized_calls:.1f}x fewer calls")
    print(f"  Memo dictionary size: {len(memo)}")


def show_complexity_analysis():
    """Display complexity comparison"""
    print("\n" + "=" * 60)
    print("COMPLEXITY ANALYSIS")
    print("=" * 60)

    print("""
    | Method          | Time      | Space | Notes                           |
    |-----------------|-----------|-------|---------------------------------|
    | Recursive       | O(2^n)    | O(n)  | Exponential - impractical >35  |
    | Memoized (Top)  | O(n)      | O(n)  | Recursion + cache               |
    | Tabulation (Bot)| O(n)      | O(n)  | Iterative, fills array          |
    | Optimized       | O(n)      | O(1)  | Only keeps last 2 values        |

    Recurrence relation:
    T(n) = T(n-1) + T(n-2) + O(1)  ->  O(2^n) without memoization
    T(n) = T(n-1) + O(1)  ->  O(n) with memoization
    """)


if __name__ == "__main__":
    run_correctness_tests()
    run_performance_comparison()
    demonstrate_memoization()
    show_complexity_analysis()

    print("\n" + "=" * 60)
    print("LEARNING OUTCOMES")
    print("=" * 60)
    print("1. Naive recursion: exponential O(2^n) due to overlapping subproblems")
    print("2. Memoization: stores results, reduces to O(n) time")
    print("3. Tabulation: bottom-up iterative, same O(n) time")
    print("4. Space optimization: only need last 2 values -> O(1) space")
    print("5. Key DP concepts: overlapping subproblems, optimal substructure")
    print("6. Trade-offs: recursion overhead vs iterative simplicity")
    print("7. Practical limit: recursive ~35, memoized/tabulation ~10^5+")
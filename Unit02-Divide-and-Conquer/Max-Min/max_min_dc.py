"""
Maximum and Minimum using Divide and Conquer
Unit 2: Divide and Conquer
"""

import time
import random
from typing import List, Tuple


def max_min_dc(arr: List[int], left: int = 0, right: int = None) -> Tuple[int, int]:
    """
    Find Maximum and Minimum using Divide and Conquer

    Divide: Split array into two halves
    Conquer: Recursively find max/min in each half
    Combine: Compare results from both halves

    Time Complexity: O(n)
    Space Complexity: O(log n) - recursion stack

    Number of comparisons: 3n/2 - 2 (optimal for comparison-based)
    """
    if right is None:
        right = len(arr) - 1

    # Base case: single element
    if left == right:
        return arr[left], arr[left]

    # Base case: two elements
    if right == left + 1:
        if arr[left] < arr[right]:
            return arr[right], arr[left]  # max, min
        else:
            return arr[left], arr[right]  # max, min

    # Divide
    mid = left + (right - left) // 2

    # Conquer
    max_left, min_left = max_min_dc(arr, left, mid)
    max_right, min_right = max_min_dc(arr, mid + 1, right)

    # Combine
    overall_max = max(max_left, max_right)
    overall_min = min(min_left, min_right)

    return overall_max, overall_min


def max_min_linear(arr: List[int]) -> Tuple[int, int]:
    """
    Find Maximum and Minimum using Linear Scan

    Time Complexity: O(n)
    Space Complexity: O(1)

    Number of comparisons: 2n - 2 (or 2n - 3 with optimization)
    """
    if not arr:
        raise ValueError("Empty array")

    max_val = min_val = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
        elif arr[i] < min_val:
            min_val = arr[i]

    return max_val, min_val


def max_min_pairwise(arr: List[int]) -> Tuple[int, int]:
    """
    Find Maximum and Minimum using Pairwise Comparison (Optimal)

    Time Complexity: O(n)
    Space Complexity: O(1)

    Number of comparisons: 3n/2 - 2 (optimal)
    """
    if not arr:
        raise ValueError("Empty array")

    n = len(arr)

    # Initialize based on odd/even length
    if n % 2 == 0:
        if arr[0] > arr[1]:
            max_val, min_val = arr[0], arr[1]
        else:
            max_val, min_val = arr[1], arr[0]
        start = 2
    else:
        max_val = min_val = arr[0]
        start = 1

    # Process pairs
    for i in range(start, n, 2):
        if arr[i] > arr[i + 1]:
            local_max, local_min = arr[i], arr[i + 1]
        else:
            local_max, local_min = arr[i + 1], arr[i]

        if local_max > max_val:
            max_val = local_max
        if local_min < min_val:
            min_val = local_min

    return max_val, min_val


def count_comparisons_dc(arr: List[int], left: int = 0, right: int = None) -> Tuple[int, int, int]:
    """Count comparisons in divide and conquer approach"""
    if right is None:
        right = len(arr) - 1

    comparisons = 0

    def helper(l, r):
        nonlocal comparisons
        if l == r:
            return arr[l], arr[l]

        if r == l + 1:
            comparisons += 1
            if arr[l] < arr[r]:
                return arr[r], arr[l]
            else:
                return arr[l], arr[r]

        mid = l + (r - l) // 2
        max_l, min_l = helper(l, mid)
        max_r, min_r = helper(mid + 1, r)

        comparisons += 2  # Two comparisons for combine
        return max(max_l, max_r), min(min_l, min_r)

    max_val, min_val = helper(left, right)
    return max_val, min_val, comparisons


def count_comparisons_linear(arr: List[int]) -> Tuple[int, int, int]:
    """Count comparisons in linear approach"""
    if not arr:
        raise ValueError("Empty array")

    max_val = min_val = arr[0]
    comparisons = 0

    for i in range(1, len(arr)):
        comparisons += 1
        if arr[i] > max_val:
            max_val = arr[i]
        else:
            comparisons += 1
            if arr[i] < min_val:
                min_val = arr[i]

    return max_val, min_val, comparisons


def count_comparisons_pairwise(arr: List[int]) -> Tuple[int, int, int]:
    """Count comparisons in pairwise approach"""
    if not arr:
        raise ValueError("Empty array")

    n = len(arr)
    comparisons = 0

    if n % 2 == 0:
        comparisons += 1
        if arr[0] > arr[1]:
            max_val, min_val = arr[0], arr[1]
        else:
            max_val, min_val = arr[1], arr[0]
        start = 2
    else:
        max_val = min_val = arr[0]
        start = 1

    for i in range(start, n, 2):
        comparisons += 1
        if arr[i] > arr[i + 1]:
            local_max, local_min = arr[i], arr[i + 1]
        else:
            local_max, local_min = arr[i + 1], arr[i]

        comparisons += 1
        if local_max > max_val:
            max_val = local_max

        comparisons += 1
        if local_min < min_val:
            min_val = local_min

    return max_val, min_val, comparisons


def measure_time(func, *args, iterations: int = 1000) -> float:
    """Measure average execution time"""
    func(*args)  # Warm up
    start = time.perf_counter()
    for _ in range(iterations):
        func(*args)
    end = time.perf_counter()
    return (end - start) / iterations * 1_000_000  # microseconds


def run_performance_analysis():
    """Run performance analysis for different input sizes"""
    print("=" * 70)
    print("MAX-MIN FINDING - PERFORMANCE ANALYSIS")
    print("=" * 70)
    print(f"{'Size':>8} | {'DC (μs)':>12} | {'Linear (μs)':>12} | {'Pairwise (μs)':>14}")
    print("-" * 70)

    sizes = [100, 500, 1000, 5000, 10000, 50000, 100000]

    for size in sizes:
        arr = random.sample(range(size * 10), size)

        t_dc = measure_time(max_min_dc, arr, iterations=200)
        t_linear = measure_time(max_min_linear, arr, iterations=500)
        t_pairwise = measure_time(max_min_pairwise, arr, iterations=500)

        print(f"{size:>8} | {t_dc:>12.3f} | {t_linear:>12.3f} | {t_pairwise:>14.3f}")


def verify_correctness():
    """Verify correctness of all implementations"""
    print("\n" + "=" * 70)
    print("CORRECTNESS VERIFICATION")
    print("=" * 70)

    test_cases = [
        [5],
        [3, 7],
        [10, 5, 8, 3, 12, 7, 1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [42, 42, 42, 42],
        [-5, -10, -3, -1, -7],
        [100, -50, 0, 75, -25, 50],
    ]

    all_passed = True
    for arr in test_cases:
        expected_max = max(arr)
        expected_min = min(arr)

        dc_max, dc_min = max_min_dc(arr)
        lin_max, lin_min = max_min_linear(arr)
        pw_max, pw_min = max_min_pairwise(arr)

        dc_ok = (dc_max == expected_max and dc_min == expected_min)
        lin_ok = (lin_max == expected_max and lin_min == expected_min)
        pw_ok = (pw_max == expected_max and pw_min == expected_min)

        status = "✓" if (dc_ok and lin_ok and pw_ok) else "✗"
        if not (dc_ok and lin_ok and pw_ok):
            all_passed = False

        print(f"{status} Array: {arr}")
        print(f"   Expected: max={expected_max}, min={expected_min}")
        print(f"   DC: max={dc_max}, min={dc_min} | Linear: max={lin_max}, min={lin_min} | Pairwise: max={pw_max}, min={pw_min}")

    print(f"\nAll tests passed: {all_passed}")
    return all_passed


def compare_comparisons():
    """Compare number of comparisons"""
    print("\n" + "=" * 70)
    print("COMPARISON COUNT ANALYSIS")
    print("=" * 70)
    print(f"{'Size':>6} | {'DC':>6} | {'Linear':>8} | {'Pairwise':>8} | {'3n/2-2':>8}")
    print("-" * 70)

    for size in [2, 3, 4, 5, 6, 7, 8, 10, 16, 32, 100, 1000]:
        arr = list(range(size))
        random.shuffle(arr)

        _, _, dc_comp = count_comparisons_dc(arr)
        _, _, lin_comp = count_comparisons_linear(arr)
        _, _, pw_comp = count_comparisons_pairwise(arr)

        theoretical = 3 * size // 2 - 2 if size > 1 else 0

        print(f"{size:>6} | {dc_comp:>6} | {lin_comp:>8} | {pw_comp:>8} | {theoretical:>8}")


def print_complexity_analysis():
    """Print complexity analysis"""
    print("\n" + "=" * 70)
    print("COMPLEXITY ANALYSIS - MAX-MIN DIVIDE AND CONQUER")
    print("=" * 70)
    print("""
MAX-MIN PROBLEM using Divide and Conquer:

RECURRENCE RELATION:
    T(n) = 2T(n/2) + 2
    T(1) = 0 (no comparisons for single element)
    T(2) = 1 (one comparison for two elements)

MASTER THEOREM:
    a = 2 (two subproblems)
    b = 2 (size divided by 2)
    f(n) = 2 = O(1) = O(n^0)

    log_b(a) = log_2(2) = 1
    f(n) = O(n^0) = O(n^(log_b a - 1)) = O(n^0)

    Case 1: f(n) = O(n^(log_b a - ε)) for ε = 1
    T(n) = Θ(n^(log_b a)) = Θ(n)

COMPARISON COUNT:
    C(n) = 2C(n/2) + 2
    C(1) = 0
    C(2) = 1

    Solution: C(n) = 3n/2 - 2 (for n power of 2)
    This is OPTIMAL for comparison-based max-min finding!

COMPLEXITY SUMMARY:
    Time:  O(n) - All three approaches
    Space: O(log n) - Divide and Conquer (recursion stack)
           O(1)     - Linear and Pairwise

COMPARISON OPTIMALITY:
    Information theory lower bound: ⌈3n/2⌉ - 2 comparisons
    - Linear:     2n - 2 comparisons (not optimal)
    - Pairwise:   3n/2 - 2 comparisons (OPTIMAL)
    - Divide & Conquer: 3n/2 - 2 comparisons (OPTIMAL)
""")


def demonstrate_dc():
    """Demonstrate divide and conquer execution"""
    print("\n" + "=" * 70)
    print("DIVIDE AND CONQUER EXECUTION TRACE")
    print("=" * 70)

    arr = [12, 5, 18, 3, 9, 15, 7, 20]
    print(f"Array: {arr}")
    print()

    def trace_max_min(arr, left, right, depth=0):
        indent = "  " * depth
        if left == right:
            print(f"{indent}Base case (1 element): max={arr[left]}, min={arr[left]}")
            return arr[left], arr[left]

        if right == left + 1:
            if arr[left] < arr[right]:
                print(f"{indent}Base case (2 elements): max={arr[right]}, min={arr[left]}")
                return arr[right], arr[left]
            else:
                print(f"{indent}Base case (2 elements): max={arr[left]}, min={arr[right]}")
                return arr[left], arr[right]

        mid = left + (right - left) // 2
        print(f"{indent}Divide: [{left}:{mid}] and [{mid+1}:{right}]")

        max_l, min_l = trace_max_min(arr, left, mid, depth + 1)
        max_r, min_r = trace_max_min(arr, mid + 1, right, depth + 1)

        overall_max = max(max_l, max_r)
        overall_min = min(min_l, min_r)
        print(f"{indent}Combine: max({max_l}, {max_r}) = {overall_max}, min({min_l}, {min_r}) = {overall_min}")

        return overall_max, overall_min

    max_val, min_val = trace_max_min(arr, 0, len(arr) - 1)
    print(f"\nFinal Result: max={max_val}, min={min_val}")


if __name__ == "__main__":
    verify_correctness()
    print_complexity_analysis()
    compare_comparisons()
    demonstrate_dc()
    run_performance_analysis()
    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETE")
    print("=" * 70)
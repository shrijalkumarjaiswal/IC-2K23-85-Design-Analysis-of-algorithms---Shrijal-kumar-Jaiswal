"""
Binary Search using Divide and Conquer
Unit 2: Divide and Conquer
"""

import time
import random
from typing import List, Optional


def binary_search_dc(arr: List[int], target: int, left: int = 0, right: int = None) -> Optional[int]:
    """
    Binary Search using Divide and Conquer (Recursive)

    Divide: Split array into two halves
    Conquer: Recursively search in appropriate half
    Combine: Return the result (trivial for search)

    Time Complexity: O(log n)
    Space Complexity: O(log n) - recursion stack
    """
    if right is None:
        right = len(arr) - 1

    # Base case: empty subarray
    if left > right:
        return None

    # Divide
    mid = left + (right - left) // 2

    # Conquer
    if arr[mid] == target:
        return mid  # Found - base case
    elif arr[mid] < target:
        # Search right half
        return binary_search_dc(arr, target, mid + 1, right)
    else:
        # Search left half
        return binary_search_dc(arr, target, left, mid - 1)


def binary_search_dc_iterative(arr: List[int], target: int) -> Optional[int]:
    """
    Binary Search using Divide and Conquer (Iterative)

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        # Divide
        mid = left + (right - left) // 2

        # Conquer
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return None


def verify_sorted(arr: List[int]) -> bool:
    """Verify array is sorted"""
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))


def measure_time(func, *args, iterations: int = 1000) -> float:
    """Measure average execution time"""
    # Warm up
    func(*args)

    start = time.perf_counter()
    for _ in range(iterations):
        func(*args)
    end = time.perf_counter()
    return (end - start) / iterations * 1_000_000  # microseconds


def run_performance_analysis():
    """Run performance analysis for different input sizes"""
    print("=" * 70)
    print("BINARY SEARCH (Divide & Conquer) - PERFORMANCE ANALYSIS")
    print("=" * 70)
    print(f"{'Size':>8} | {'Recursive (μs)':>15} | {'Iterative (μs)':>15} | {'Speedup':>10}")
    print("-" * 70)

    sizes = [100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
    results = []

    for size in sizes:
        arr = sorted(random.sample(range(size * 10), size))
        target = arr[size // 2]  # Average case: middle element

        # Verify array is sorted
        assert verify_sorted(arr), "Array not sorted!"

        # Measure times
        rec_time = measure_time(binary_search_dc, arr, target, iterations=500)
        iter_time = measure_time(binary_search_dc_iterative, arr, target, iterations=500)

        speedup = rec_time / iter_time if iter_time > 0 else 0

        print(f"{size:>8} | {rec_time:>15.3f} | {iter_time:>15.3f} | {speedup:>10.2f}x")

        results.append({
            'size': size,
            'recursive': rec_time,
            'iterative': iter_time,
            'speedup': speedup
        })

    return results


def verify_correctness():
    """Verify correctness of both implementations"""
    print("\n" + "=" * 70)
    print("CORRECTNESS VERIFICATION")
    print("=" * 70)

    test_cases = [
        ([1, 3, 5, 7, 9, 11, 13], 7, 3),
        ([2, 4, 6, 8, 10], 10, 4),
        ([1, 2, 3, 4, 5], 1, 0),
        ([1, 2, 3, 4, 5], 5, 4),
        ([1, 2, 3, 4, 5], 6, None),
        ([], 1, None),
        ([42], 42, 0),
        ([42], 21, None),
        (list(range(0, 1000, 2)), 500, 250),
        (list(range(100)), 99, 99),
    ]

    all_passed = True
    for arr, target, expected in test_cases:
        rec_result = binary_search_dc(arr, target)
        iter_result = binary_search_dc_iterative(arr, target)

        rec_pass = rec_result == expected
        iter_pass = iter_result == expected

        status = "✓" if rec_pass and iter_pass else "✗"
        if not (rec_pass and iter_pass):
            all_passed = False

        print(f"{status} Array size: {len(arr):>4}, Target: {target:>4}")
        print(f"   Expected: {expected}, Recursive: {rec_result}, Iterative: {iter_result}")

    print(f"\nAll tests passed: {all_passed}")
    return all_passed


def print_complexity_analysis():
    """Print complexity analysis"""
    print("\n" + "=" * 70)
    print("COMPLEXITY ANALYSIS - DIVIDE AND CONQUER")
    print("=" * 70)
    print("""
BINARY SEARCH using Divide and Conquer:

RECURRENCE RELATION:
    T(n) = T(n/2) + O(1)
    T(1) = O(1)

MASTER THEOREM:
    a = 1 (one subproblem)
    b = 2 (size divided by 2)
    f(n) = O(1) = O(n^0)

    log_b(a) = log_2(1) = 0
    f(n) = O(n^0) = O(n^(log_b a))

    Case 2: f(n) = Θ(n^(log_b a) log^k n) with k=0
    T(n) = Θ(n^(log_b a) log^(k+1) n) = Θ(log n)

COMPLEXITY:
    Time:  O(log n) - Best, Average, Worst all same
    Space: O(log n) - Recursive (call stack)
           O(1)     - Iterative

DIVIDE AND CONQUER STRUCTURE:
    1. DIVIDE:   Split problem into subproblems (find mid)
    2. CONQUER:  Solve subproblems recursively (search half)
    3. COMBINE:  Trivial for search (just return result)

    This is a "decrease and conquer" variant - only one subproblem
    is solved at each step, not multiple.
""")


def demonstrate_divide_conquer():
    """Demonstrate the divide and conquer steps"""
    print("\n" + "=" * 70)
    print("DIVIDE AND CONQUER EXECUTION TRACE")
    print("=" * 70)

    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 11

    print(f"Array: {arr}")
    print(f"Target: {target}")
    print(f"Length: {len(arr)}")
    print()

    def trace_binary_search(arr, target, left, right, depth=0):
        indent = "  " * depth
        if left > right:
            print(f"{indent}Base case: left({left}) > right({right}) -> NOT FOUND")
            return None

        mid = left + (right - left) // 2
        print(f"{indent}Divide: left={left}, right={right}, mid={mid}, arr[mid]={arr[mid]}")

        if arr[mid] == target:
            print(f"{indent}Conquer: FOUND at index {mid}")
            return mid
        elif arr[mid] < target:
            print(f"{indent}Conquer: {arr[mid]} < {target}, search RIGHT half")
            return trace_binary_search(arr, target, mid + 1, right, depth + 1)
        else:
            print(f"{indent}Conquer: {arr[mid]} > {target}, search LEFT half")
            return trace_binary_search(arr, target, left, mid - 1, depth + 1)

    result = trace_binary_search(arr, target, 0, len(arr) - 1)
    print(f"\nResult: Found at index {result}")


if __name__ == "__main__":
    verify_correctness()
    print_complexity_analysis()
    demonstrate_divide_conquer()
    run_performance_analysis()
    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETE")
    print("=" * 70)
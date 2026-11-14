"""
Binary Search Implementation - Iterative and Recursive
Unit 1: Introduction to Algorithms & Performance Analysis
"""

import time
import random
from typing import List, Optional


def binary_search_iterative(arr: List[int], target: int) -> Optional[int]:
    """
    Iterative Binary Search Algorithm

    Args:
        arr: Sorted list of integers
        target: Value to search for

    Returns:
        Index of target if found, None otherwise

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Prevents overflow

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None


def binary_search_recursive(arr: List[int], target: int, left: int = 0, right: int = None) -> Optional[int]:
    """
    Recursive Binary Search Algorithm

    Args:
        arr: Sorted list of integers
        target: Value to search for
        left: Left boundary (default 0)
        right: Right boundary (default len(arr) - 1)

    Returns:
        Index of target if found, None otherwise

    Time Complexity: O(log n)
    Space Complexity: O(log n) - due to recursion stack
    """
    if right is None:
        right = len(arr) - 1

    if left > right:
        return None

    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def linear_search(arr: List[int], target: int) -> Optional[int]:
    """
    Linear Search for comparison

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for i, val in enumerate(arr):
        if val == target:
            return i
    return None


def measure_execution_time(search_func, arr: List[int], target: int, iterations: int = 1000) -> float:
    """Measure average execution time over multiple iterations"""
    start = time.perf_counter()
    for _ in range(iterations):
        search_func(arr, target)
    end = time.perf_counter()
    return (end - start) / iterations


def generate_test_data(size: int) -> List[int]:
    """Generate sorted array of given size"""
    return sorted(random.sample(range(size * 10), size))


def run_performance_analysis():
    """Run performance analysis for different input sizes"""
    print("=" * 60)
    print("BINARY SEARCH PERFORMANCE ANALYSIS")
    print("=" * 60)
    print(f"{'Size':>8} | {'Iterative (μs)':>15} | {'Recursive (μs)':>15} | {'Linear (μs)':>12}")
    print("-" * 60)

    sizes = [100, 500, 1000, 5000, 10000, 50000, 100000]
    results = []

    for size in sizes:
        arr = generate_test_data(size)
        target = arr[size // 2]  # Search for middle element (average case)

        # Measure times
        iter_time = measure_execution_time(binary_search_iterative, arr, target) * 1_000_000
        rec_time = measure_execution_time(binary_search_recursive, arr, target) * 1_000_000
        linear_time = measure_execution_time(linear_search, arr, target) * 1_000_000

        print(f"{size:>8} | {iter_time:>15.3f} | {rec_time:>15.3f} | {linear_time:>12.3f}")

        results.append({
            'size': size,
            'iterative': iter_time,
            'recursive': rec_time,
            'linear': linear_time
        })

    return results


def verify_correctness():
    """Verify correctness of both implementations"""
    print("\n" + "=" * 60)
    print("CORRECTNESS VERIFICATION")
    print("=" * 60)

    test_cases = [
        ([1, 3, 5, 7, 9, 11, 13], 7, 3),
        ([2, 4, 6, 8, 10], 10, 4),
        ([1, 2, 3, 4, 5], 1, 0),
        ([1, 2, 3, 4, 5], 5, 4),
        ([1, 2, 3, 4, 5], 6, None),
        ([], 1, None),
        ([42], 42, 0),
        ([42], 21, None),
    ]

    all_passed = True
    for arr, target, expected in test_cases:
        iter_result = binary_search_iterative(arr, target)
        rec_result = binary_search_recursive(arr, target)

        iter_pass = iter_result == expected
        rec_pass = rec_result == expected

        status = "✓" if iter_pass and rec_pass else "✗"
        if not (iter_pass and rec_pass):
            all_passed = False

        print(f"{status} Array: {arr}, Target: {target}")
        print(f"   Expected: {expected}, Iterative: {iter_result}, Recursive: {rec_result}")

    print(f"\nAll tests passed: {all_passed}")
    return all_passed


def analyze_complexity():
    """Print complexity analysis"""
    print("\n" + "=" * 60)
    print("COMPLEXITY ANALYSIS")
    print("=" * 60)
    print("""
BINARY SEARCH (Iterative):
  Best Case:    O(1)     - Target found at middle element
  Average Case: O(log n) - Target found after log n comparisons
  Worst Case:   O(log n) - Target not in array or at boundaries
  Space:        O(1)     - Constant extra space

BINARY SEARCH (Recursive):
  Best Case:    O(1)     - Target found at middle element
  Average Case: O(log n) - Target found after log n comparisons
  Worst Case:   O(log n) - Target not in array or at boundaries
  Space:        O(log n) - Recursion stack depth

LINEAR SEARCH (for comparison):
  Best Case:    O(1)     - Target at first position
  Average Case: O(n)     - Target at middle position
  Worst Case:   O(n)     - Target not in array or at last position
  Space:        O(1)     - Constant extra space
""")


if __name__ == "__main__":
    # Run verification
    verify_correctness()

    # Print complexity analysis
    analyze_complexity()

    # Run performance analysis
    results = run_performance_analysis()

    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)
"""
Merge Sort Implementation with Performance Analysis
Unit 2: Divide and Conquer
"""

import time
import random
from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    """
    Merge Sort using Divide and Conquer

    Divide: Split array into two halves
    Conquer: Recursively sort each half
    Combine: Merge two sorted halves

    Time Complexity: O(n log n) - Best, Average, Worst
    Space Complexity: O(n) - auxiliary array for merging
    """
    if len(arr) <= 1:
        return arr

    # Divide
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Conquer
    left = merge_sort(left)
    right = merge_sort(right)

    # Combine
    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    """Merge two sorted arrays"""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort_inplace(arr: List[int], left: int = 0, right: int = None) -> None:
    """
    In-place Merge Sort (uses O(n) auxiliary space but modifies original array)
    """
    if right is None:
        right = len(arr) - 1

    if left >= right:
        return

    mid = left + (right - left) // 2

    merge_sort_inplace(arr, left, mid)
    merge_sort_inplace(arr, mid + 1, right)

    merge_inplace(arr, left, mid, right)


def merge_inplace(arr: List[int], left: int, mid: int, right: int) -> None:
    """Merge two sorted subarrays in-place using auxiliary array"""
    # Create copies of subarrays
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1


def is_sorted(arr: List[int]) -> bool:
    """Verify array is sorted"""
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))


def measure_time(func, *args, iterations: int = 100) -> float:
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
    print("MERGE SORT - PERFORMANCE ANALYSIS")
    print("=" * 70)
    print(f"{'Size':>8} | {'Functional (μs)':>16} | {'In-Place (μs)':>15} | {'Verified':>8}")
    print("-" * 70)

    sizes = [100, 500, 1000, 2000, 5000, 10000, 20000]

    for size in sizes:
        arr = random.sample(range(size * 10), size)

        # Functional version
        t_func = measure_time(merge_sort, arr, iterations=50)
        result = merge_sort(arr)
        verified = "✓" if is_sorted(result) else "✗"

        # In-place version
        arr_copy = arr.copy()
        t_inplace = measure_time(merge_sort_inplace, arr_copy, iterations=50)
        verified2 = "✓" if is_sorted(arr_copy) else "✗"

        print(f"{size:>8} | {t_func:>16.3f} | {t_inplace:>15.3f} | {verified}{verified2:>6}")


def verify_correctness():
    """Verify correctness of implementations"""
    print("\n" + "=" * 70)
    print("CORRECTNESS VERIFICATION")
    print("=" * 70)

    test_cases = [
        [],
        [1],
        [2, 1],
        [3, 1, 2],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [3, 1, 4, 1, 5, 9, 2, 6],
        [42, 42, 42],
        [-5, -10, -3, -1, -7],
        [100, -50, 0, 75, -25, 50],
    ]

    all_passed = True
    for arr in test_cases:
        # Functional
        result = merge_sort(arr)
        expected = sorted(arr)
        func_ok = result == expected

        # In-place
        arr_copy = arr.copy()
        merge_sort_inplace(arr_copy)
        inplace_ok = arr_copy == expected

        status = "✓" if func_ok and inplace_ok else "✗"
        if not (func_ok and inplace_ok):
            all_passed = False

        print(f"{status} Input: {arr}")
        print(f"   Expected: {expected}")
        print(f"   Functional: {result}")
        print(f"   In-place: {arr_copy}")

    print(f"\nAll tests passed: {all_passed}")
    return all_passed


def print_complexity_analysis():
    """Print complexity analysis"""
    print("\n" + "=" * 70)
    print("COMPLEXITY ANALYSIS - MERGE SORT")
    print("=" * 70)
    print("""
MERGE SORT using Divide and Conquer:

RECURRENCE RELATION:
    T(n) = 2T(n/2) + n
    T(1) = O(1)

    Divide:    O(1) - finding midpoint
    Conquer:   2T(n/2) - two recursive calls
    Combine:   O(n)  - merging two sorted arrays

MASTER THEOREM:
    a = 2 (two subproblems)
    b = 2 (size halved)
    f(n) = n = O(n^1)

    log_b(a) = log_2(2) = 1
    f(n) = O(n^1) = O(n^(log_b a))

    Case 2: f(n) = Θ(n^(log_b a) log^k n) with k=0
    T(n) = Θ(n^(log_b a) log^(k+1) n) = Θ(n log n)

COMPLEXITY:
    Time:  O(n log n) - Best, Average, Worst (always same)
    Space: O(n) - auxiliary array for merging
           O(log n) - recursion stack

STABILITY: Stable (maintains relative order of equal elements)

NOTES:
    - Not adaptive (always does same work regardless of input order)
    - Not in-place (requires O(n) extra space)
    - Excellent for linked lists (O(1) merge space)
    - Predictable performance makes it good for real-time systems
""")


def demonstrate_merge_sort():
    """Demonstrate merge sort execution"""
    print("\n" + "=" * 70)
    print("MERGE SORT EXECUTION TRACE")
    print("=" * 70)

    arr = [38, 27, 43, 3, 9, 82, 10]
    print(f"Original: {arr}")
    print()

    def trace_merge_sort(arr, depth=0):
        indent = "  " * depth
        if len(arr) <= 1:
            print(f"{indent}Base case: {arr}")
            return arr

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        print(f"{indent}Divide: {left} | {right}")

        left = trace_merge_sort(left, depth + 1)
        right = trace_merge_sort(right, depth + 1)

        result = merge(left, right)
        print(f"{indent}Combine: {left} + {right} = {result}")

        return result

    sorted_arr = trace_merge_sort(arr)
    print(f"\nSorted: {sorted_arr}")


def compare_with_other_sorts():
    """Compare merge sort with other sorting algorithms"""
    print("\n" + "=" * 70)
    print("COMPARISON WITH OTHER SORTS (n=5000)")
    print("=" * 70)

    # We'll just show theoretical comparison
    print("""
Theoretical Comparison for n=5000:

Algorithm          | Time Complexity | Space  | Stable | Notes
-------------------|-----------------|--------|--------|--------------------------
Merge Sort         | O(n log n)      | O(n)   | Yes    | Consistent performance
Quick Sort         | O(n log n) avg  | O(log n)| No    | Fast in practice
Heap Sort          | O(n log n)      | O(1)   | No     | Guaranteed O(n log n)
Bubble Sort        | O(n²)           | O(1)   | Yes    | Educational only
Insertion Sort     | O(n²)           | O(1)   | Yes    | Good for small n

For n=5000:
- Merge Sort:    ~5000 * 12.3 = 61,500 operations
- Quick Sort:    ~5000 * 12.3 = 61,500 operations (avg)
- Heap Sort:     ~5000 * 12.3 = 61,500 operations
- Bubble Sort:   ~5000² / 2 = 12,500,000 operations
- Insertion Sort:~5000² / 4 = 6,250,000 operations (avg)

Merge Sort is ~100-200x faster than O(n²) sorts for n=5000!
""")


if __name__ == "__main__":
    verify_correctness()
    print_complexity_analysis()
    demonstrate_merge_sort()
    compare_with_other_sorts()
    run_performance_analysis()
    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETE")
    print("=" * 70)
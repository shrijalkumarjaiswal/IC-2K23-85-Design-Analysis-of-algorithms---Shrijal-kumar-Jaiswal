"""
Quick Sort Implementation with Performance Analysis
Unit 2: Divide and Conquer
"""

import time
import random
from typing import List


def quick_sort(arr: List[int]) -> List[int]:
    """
    Quick Sort using Divide and Conquer (Functional Version)

    Divide: Partition array around pivot
    Conquer: Recursively sort subarrays
    Combine: Trivial (concatenation)

    Time Complexity:
        Best: O(n log n) - balanced partitions
        Average: O(n log n)
        Worst: O(n²) - already sorted/reverse sorted with poor pivot
    Space Complexity: O(log n) average, O(n) worst (recursion stack)
    """
    if len(arr) <= 1:
        return arr

    # Choose pivot (median-of-three for better average case)
    pivot = median_of_three(arr)

    # Divide: Partition
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Conquer
    left = quick_sort(left)
    right = quick_sort(right)

    # Combine
    return left + middle + right


def median_of_three(arr: List[int]) -> int:
    """Choose pivot using median of first, middle, last elements"""
    if len(arr) <= 2:
        return arr[0]
    first = arr[0]
    middle = arr[len(arr) // 2]
    last = arr[-1]
    return sorted([first, middle, last])[1]


def quick_sort_inplace(arr: List[int], low: int = 0, high: int = None) -> None:
    """
    In-place Quick Sort (Lomuto Partition Scheme)

    Space Complexity: O(log n) average (recursion stack)
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        # Partition
        pi = partition(arr, low, high)

        # Recursively sort partitions
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)


def partition(arr: List[int], low: int, high: int) -> int:
    """
    Lomuto Partition Scheme
    Returns final position of pivot
    """
    # Choose pivot (median of three)
    mid = (low + high) // 2
    # Sort low, mid, high
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]

    # Move pivot to end
    arr[mid], arr[high] = arr[high], arr[mid]
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_hoare(arr: List[int], low: int = 0, high: int = None) -> None:
    """
    In-place Quick Sort (Hoare Partition Scheme)
    More efficient than Lomuto
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        pi = hoare_partition(arr, low, high)
        quick_sort_hoare(arr, low, pi)
        quick_sort_hoare(arr, pi + 1, high)


def hoare_partition(arr: List[int], low: int, high: int) -> int:
    """Hoare Partition Scheme"""
    pivot = arr[(low + high) // 2]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


def is_sorted(arr: List[int]) -> bool:
    """Verify array is sorted"""
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))


def measure_time(func, *args, iterations: int = 100) -> float:
    """Measure average execution time"""
    func(*args)  # Warm up
    start = time.perf_counter()
    for _ in range(iterations):
        func(*args)
    end = time.perf_counter()
    return (end - start) / iterations * 1_000_000  # microseconds


def run_performance_analysis():
    """Run performance analysis for different input sizes and cases"""
    print("=" * 80)
    print("QUICK SORT - PERFORMANCE ANALYSIS")
    print("=" * 80)

    sizes = [100, 500, 1000, 2000, 5000, 10000, 20000]

    print("\n1. AVERAGE CASE (Random Data)")
    print("-" * 80)
    print(f"{'Size':>8} | {'Functional (μs)':>16} | {'Lomuto (μs)':>14} | {'Hoare (μs)':>12} | {'Verified':>8}")
    print("-" * 80)

    for size in sizes:
        arr = random.sample(range(size * 10), size)

        t_func = measure_time(quick_sort, arr, iterations=50)
        result = quick_sort(arr)
        v1 = "✓" if is_sorted(result) else "✗"

        arr_copy = arr.copy()
        t_lomuto = measure_time(quick_sort_inplace, arr_copy, iterations=50)
        v2 = "✓" if is_sorted(arr_copy) else "✗"

        arr_copy2 = arr.copy()
        t_hoare = measure_time(quick_sort_hoare, arr_copy2, iterations=50)
        v3 = "✓" if is_sorted(arr_copy2) else "✗"

        print(f"{size:>8} | {t_func:>16.3f} | {t_lomuto:>14.3f} | {t_hoare:>12.3f} | {v1}{v2}{v3:>5}")

    print("\n2. BEST CASE (Already Sorted - Median of 3 pivot handles this well)")
    print("-" * 80)
    print(f"{'Size':>8} | {'Functional (μs)':>16} | {'Lomuto (μs)':>14} | {'Hoare (μs)':>12}")
    print("-" * 80)

    for size in sizes:
        arr = list(range(size))

        t_func = measure_time(quick_sort, arr, iterations=50)
        t_lomuto = measure_time(quick_sort_inplace, arr.copy(), iterations=50)
        t_hoare = measure_time(quick_sort_hoare, arr.copy(), iterations=50)

        print(f"{size:>8} | {t_func:>16.3f} | {t_lomuto:>14.3f} | {t_hoare:>12.3f}")

    print("\n3. WORST CASE SIMULATION (Adversarial input for basic pivot)")
    print("-" * 80)
    print("Using first-element pivot on sorted array:")
    print("-" * 80)

    def quick_sort_first_pivot(arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
        pivot = arr[0]  # BAD: always picks first
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort_first_pivot(left) + middle + quick_sort_first_pivot(right)

    small_sizes = [100, 200, 500, 1000, 2000]
    print(f"{'Size':>8} | {'Median-of-3 (μs)':>16} | {'First Pivot (μs)':>16} | {'Ratio':>8}")
    print("-" * 80)

    for size in small_sizes:
        arr = list(range(size))

        t_good = measure_time(quick_sort, arr, iterations=20)
        t_bad = measure_time(quick_sort_first_pivot, arr, iterations=5)
        ratio = t_bad / t_good if t_good > 0 else 0

        print(f"{size:>8} | {t_good:>16.3f} | {t_bad:>16.3f} | {ratio:>8.1f}x")


def verify_correctness():
    """Verify correctness of all implementations"""
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
        [1, 1, 1, 1, 1],  # All duplicates
    ]

    all_passed = True
    for arr in test_cases:
        expected = sorted(arr)

        # Functional
        result = quick_sort(arr)
        func_ok = result == expected

        # Lomuto
        arr_copy = arr.copy()
        quick_sort_inplace(arr_copy)
        lomuto_ok = arr_copy == expected

        # Hoare
        arr_copy2 = arr.copy()
        quick_sort_hoare(arr_copy2)
        hoare_ok = arr_copy2 == expected

        status = "✓" if func_ok and lomuto_ok and hoare_ok else "✗"
        if not (func_ok and lomuto_ok and hoare_ok):
            all_passed = False

        print(f"{status} Input: {arr}")
        print(f"   Expected: {expected}")
        print(f"   Functional: {result}")
        print(f"   Lomuto: {arr_copy}")
        print(f"   Hoare: {arr_copy2}")

    print(f"\nAll tests passed: {all_passed}")
    return all_passed


def print_complexity_analysis():
    """Print complexity analysis"""
    print("\n" + "=" * 70)
    print("COMPLEXITY ANALYSIS - QUICK SORT")
    print("=" * 70)
    print("""
QUICK SORT using Divide and Conquer:

RECURRENCE RELATIONS:

Best/Average Case (balanced partitions):
    T(n) = 2T(n/2) + n
    T(1) = O(1)

    Master Theorem: a=2, b=2, f(n)=n
    log_b(a) = 1, f(n) = Θ(n)
    Case 2: T(n) = Θ(n log n)

Worst Case (unbalanced partitions):
    T(n) = T(n-1) + n
    T(1) = O(1)

    Solution: T(n) = n + (n-1) + ... + 1 = n(n+1)/2 = Θ(n²)

PIVOT SELECTION STRATEGIES:
    1. First/Last Element: Simple, but O(n²) on sorted data
    2. Random Element: Expected O(n log n), prevents worst case
    3. Median of Three: Good practical choice, handles sorted data
    4. Median of Medians: Guaranteed O(n log n) worst case, but high constant

PARTITION SCHEMES:
    Lomuto: Simple, single scan, more swaps
    Hoare:  Fewer swaps, better cache performance, slightly more complex

COMPLEXITY SUMMARY:
    Time:  Best O(n log n), Average O(n log n), Worst O(n²)
    Space: O(log n) average (stack), O(n) worst (stack)

PROPERTIES:
    - In-place: Yes (O(log n) extra space)
    - Stable: No
    - Adaptive: No (but can be with 3-way partition)
    - Online: No

OPTIMIZATIONS:
    1. Median-of-three pivot
    2. Insertion sort for small subarrays (< 10)
    3. Tail recursion elimination
    4. 3-way partition for duplicate keys
    5. Randomized pivot for adversarial inputs
""")


def demonstrate_quick_sort():
    """Demonstrate quick sort execution"""
    print("\n" + "=" * 70)
    print("QUICK SORT EXECUTION TRACE (Lomuto)")
    print("=" * 70)

    arr = [38, 27, 43, 3, 9, 82, 10]
    print(f"Original: {arr}")
    print()

    def trace_partition(arr, low, high, depth=0):
        indent = "  " * depth
        if low >= high:
            return

        mid = (low + high) // 2
        # Median of three
        if arr[low] > arr[mid]:
            arr[low], arr[mid] = arr[mid], arr[low]
        if arr[low] > arr[high]:
            arr[low], arr[high] = arr[high], arr[low]
        if arr[mid] > arr[high]:
            arr[mid], arr[high] = arr[high], arr[mid]

        arr[mid], arr[high] = arr[high], arr[mid]
        pivot = arr[high]

        print(f"{indent}Partition: {arr[low:high+1]}, pivot={pivot}")

        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pi = i + 1

        print(f"{indent}After partition: {arr[low:high+1]}, pivot index={pi}")

        trace_partition(arr, low, pi - 1, depth + 1)
        trace_partition(arr, pi + 1, high, depth + 1)

    trace_partition(arr, 0, len(arr) - 1)
    print(f"\nSorted: {arr}")


if __name__ == "__main__":
    verify_correctness()
    print_complexity_analysis()
    demonstrate_quick_sort()
    run_performance_analysis()
    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETE")
    print("=" * 70)
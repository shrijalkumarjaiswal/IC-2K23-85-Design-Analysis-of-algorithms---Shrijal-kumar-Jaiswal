"""
Heap Sort Implementation with Performance Analysis
Unit 2: Divide and Conquer
"""

import time
import random
from typing import List


def heap_sort(arr: List[int]) -> List[int]:
    """
    Heap Sort using Binary Heap

    Build max heap, then repeatedly extract maximum

    Time Complexity: O(n log n) - Best, Average, Worst
    Space Complexity: O(1) - In-place
    """
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move current root (max) to end
        arr[0], arr[i] = arr[i], arr[0]

        # Heapify reduced heap
        heapify(arr, i, 0)

    return arr


def heapify(arr: List[int], n: int, i: int) -> None:
    """
    Heapify subtree rooted at index i
    n is the size of heap
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # If left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child is larger than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort_descending(arr: List[int]) -> List[int]:
    """Heap sort for descending order (min heap)"""
    n = len(arr)

    # Build min heap
    for i in range(n // 2 - 1, -1, -1):
        min_heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        min_heapify(arr, i, 0)

    return arr


def min_heapify(arr: List[int], n: int, i: int) -> None:
    """Heapify for min heap"""
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, n, smallest)


def is_sorted(arr: List[int]) -> bool:
    """Verify array is sorted"""
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))


def is_sorted_descending(arr: List[int]) -> bool:
    """Verify array is sorted descending"""
    return all(arr[i] >= arr[i+1] for i in range(len(arr)-1))


def measure_time(func, *args, iterations: int = 100) -> float:
    """Measure average execution time"""
    func(*args)  # Warm up
    start = time.perf_counter()
    for _ in range(iterations):
        func(*args)
    end = time.perf_counter()
    return (end - start) / iterations * 1_000_000  # microseconds


def build_heap_trace(arr: List[int]) -> List[str]:
    """Trace heap building process"""
    trace = []
    n = len(arr)
    trace.append(f"Initial array: {arr}")

    for i in range(n // 2 - 1, -1, -1):
        trace.append(f"\nHeapify at index {i} (value {arr[i]}):")
        trace.append(f"  Before: {arr}")
        heapify(arr, n, i)
        trace.append(f"  After:  {arr}")

    trace.append(f"\nMax Heap built: {arr}")
    return trace


def extract_max_trace(arr: List[int]) -> List[str]:
    """Trace max extraction process"""
    trace = []
    n = len(arr)

    for i in range(n - 1, 0, -1):
        trace.append(f"\nExtract max: swap arr[0]={arr[0]} with arr[{i}]={arr[i]}")
        arr[0], arr[i] = arr[i], arr[0]
        trace.append(f"  After swap: {arr}")
        trace.append(f"  Heapify reduced heap (size {i}):")
        heapify(arr, i, 0)
        trace.append(f"  After heapify: {arr}")

    trace.append(f"\nFinal sorted: {arr}")
    return trace


def run_performance_analysis():
    """Run performance analysis for different input sizes"""
    print("=" * 70)
    print("HEAP SORT - PERFORMANCE ANALYSIS")
    print("=" * 70)
    print(f"{'Size':>8} | {'Ascending (μs)':>15} | {'Descending (μs)':>16} | {'Verified':>8}")
    print("-" * 70)

    sizes = [100, 500, 1000, 2000, 5000, 10000, 20000, 50000]

    for size in sizes:
        arr = random.sample(range(size * 10), size)

        # Ascending
        t_asc = measure_time(heap_sort, arr.copy(), iterations=50)
        result = heap_sort(arr.copy())
        v1 = "✓" if is_sorted(result) else "✗"

        # Descending
        t_desc = measure_time(heap_sort_descending, arr.copy(), iterations=50)
        result2 = heap_sort_descending(arr.copy())
        v2 = "✓" if is_sorted_descending(result2) else "✗"

        print(f"{size:>8} | {t_asc:>15.3f} | {t_desc:>16.3f} | {v1}{v2:>6}")


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
        expected = sorted(arr)

        # Ascending
        result = heap_sort(arr.copy())
        asc_ok = result == expected

        # Descending
        expected_desc = sorted(arr, reverse=True)
        result_desc = heap_sort_descending(arr.copy())
        desc_ok = result_desc == expected_desc

        status = "✓" if asc_ok and desc_ok else "✗"
        if not (asc_ok and desc_ok):
            all_passed = False

        print(f"{status} Input: {arr}")
        print(f"   Expected: {expected}")
        print(f"   Ascending: {result}")
        print(f"   Descending: {result_desc}")

    print(f"\nAll tests passed: {all_passed}")
    return all_passed


def print_complexity_analysis():
    """Print complexity analysis"""
    print("\n" + "=" * 70)
    print("COMPLEXITY ANALYSIS - HEAP SORT")
    print("=" * 70)
    print("""
HEAP SORT using Binary Heap:

ALGORITHM PHASES:
    1. BUILD HEAP: Convert array into max heap
       - Start from last non-leaf node (n/2 - 1) down to root
       - Heapify each node

    2. EXTRACT MAX: Repeatedly remove maximum
       - Swap root with last element
       - Reduce heap size
       - Heapify root

HEAPIFY OPERATION:
    HEAPIFY(arr, n, i):
        largest ← i
        left ← 2i + 1
        right ← 2i + 2

        if left < n and arr[left] > arr[largest]:
            largest ← left
        if right < n and arr[right] > arr[largest]:
            largest ← right

        if largest ≠ i:
            swap arr[i] and arr[largest]
            HEAPIFY(arr, n, largest)

COMPLEXITY ANALYSIS:

BUILD HEAP:
    Not O(n log n) as naive analysis suggests!
    Actual: O(n)

    Proof: Height of node i is ⌊log(n/i)⌋
    Number of nodes at height h: ≤ n/2^(h+1)
    Work at height h: O(h)

    Total work = Σ (h=0 to log n) (n/2^(h+1)) * O(h) = O(n)

EXTRACT MAX (n-1 times):
    Each extraction: O(log n) - height of heap
    Total: (n-1) * O(log n) = O(n log n)

OVERALL:
    Time:  Build O(n) + Extract O(n log n) = O(n log n)
           Best, Average, Worst all O(n log n)
    Space: O(1) - In-place, only recursion stack O(log n)

RECURRENCE:
    T(n) = T(n-1) + O(log n)
    T(1) = O(1)

    Solution: O(n log n)

PROPERTIES:
    - In-place: Yes (O(1) extra space)
    - Stable: No (swapping can change relative order)
    - Adaptive: No
    - Guaranteed O(n log n) worst case

COMPARISON WITH OTHER O(n log n) SORTS:
    Merge Sort: O(n) space, Stable, Not in-place
    Quick Sort: O(log n) avg space, Unstable, O(n²) worst
    Heap Sort: O(1) space, Unstable, Guaranteed O(n log n)

    Heap Sort is the ONLY comparison sort with:
    O(1) space + O(n log n) worst case!
""")


def demonstrate_heap_sort():
    """Demonstrate heap sort execution"""
    print("\n" + "=" * 70)
    print("HEAP SORT EXECUTION TRACE")
    print("=" * 70)

    arr = [12, 11, 13, 5, 6, 7]
    print(f"Original: {arr}")
    print()

    print("PHASE 1: BUILD MAX HEAP")
    print("-" * 40)
    trace = build_heap_trace(arr.copy())
    for line in trace:
        print(line)

    print("\n\nPHASE 2: EXTRACT MAX REPEATEDLY")
    print("-" * 40)
    # Rebuild heap for extraction trace
    heap_arr = arr.copy()
    n = len(heap_arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(heap_arr, n, i)

    trace = extract_max_trace(heap_arr)
    for line in trace:
        print(line)


def compare_with_other_sorts():
    """Compare heap sort with other sorts"""
    print("\n" + "=" * 70)
    print("THEORETICAL COMPARISON")
    print("=" * 70)
    print("""
For n = 10,000:

Algorithm          | Operations (approx) | Space    | Worst Case
-------------------|---------------------|----------|-------------
Merge Sort         | 10000 * 13.3 = 133K | O(n)     | O(n log n)
Quick Sort (avg)   | 10000 * 13.3 = 133K | O(log n) | O(n²)
Quick Sort (worst) | 10000²/2 = 50M      | O(n)     | O(n²)
Heap Sort          | 10000 * 13.3 = 133K | O(1)     | O(n log n)
Bubble Sort        | 10000²/2 = 50M      | O(1)     | O(n²)
Insertion Sort     | 10000²/4 = 25M      | O(1)     | O(n²)

Key Advantages of Heap Sort:
1. Guaranteed O(n log n) worst case
2. O(1) extra space (in-place)
3. No recursion limit issues (can be implemented iteratively)

Key Disadvantages:
1. Not stable
2. Poor cache performance (non-local memory access)
3. Slower than Quick Sort in practice due to constant factors
4. Not adaptive (doesn't benefit from partially sorted input)
""")


if __name__ == "__main__":
    verify_correctness()
    print_complexity_analysis()
    demonstrate_heap_sort()
    compare_with_other_sorts()
    run_performance_analysis()
    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETE")
    print("=" * 70)
"""
Basic Array Operations Implementation
Unit 1: Introduction to Algorithms & Performance Analysis
"""

import time
import random
from typing import List, Any, Optional


class ArrayOperations:
    """Class demonstrating basic array operations with complexity analysis"""

    def __init__(self):
        self.array: List[Any] = []

    # ==================== INSERTION OPERATIONS ====================

    def insert_at_end(self, value: Any) -> None:
        """Insert element at the end - O(1) amortized"""
        self.array.append(value)

    def insert_at_beginning(self, value: Any) -> None:
        """Insert element at beginning - O(n)"""
        self.array.insert(0, value)

    def insert_at_position(self, index: int, value: Any) -> bool:
        """Insert element at specific position - O(n)"""
        if 0 <= index <= len(self.array):
            self.array.insert(index, value)
            return True
        return False

    # ==================== DELETION OPERATIONS ====================

    def delete_from_end(self) -> Optional[Any]:
        """Delete element from end - O(1)"""
        if self.array:
            return self.array.pop()
        return None

    def delete_from_beginning(self) -> Optional[Any]:
        """Delete element from beginning - O(n)"""
        if self.array:
            return self.array.pop(0)
        return None

    def delete_from_position(self, index: int) -> Optional[Any]:
        """Delete element from specific position - O(n)"""
        if 0 <= index < len(self.array):
            return self.array.pop(index)
        return None

    def delete_by_value(self, value: Any) -> bool:
        """Delete first occurrence of value - O(n)"""
        try:
            self.array.remove(value)
            return True
        except ValueError:
            return False

    # ==================== SEARCH OPERATIONS ====================

    def linear_search(self, target: Any) -> Optional[int]:
        """Linear search - O(n)"""
        for i, val in enumerate(self.array):
            if val == target:
                return i
        return None

    def binary_search(self, target: Any) -> Optional[int]:
        """Binary search (requires sorted array) - O(log n)"""
        left, right = 0, len(self.array) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if self.array[mid] == target:
                return mid
            elif self.array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return None

    # ==================== SORTING OPERATIONS ====================

    def bubble_sort(self) -> None:
        """Bubble sort - O(n²)"""
        n = len(self.array)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    swapped = True
            if not swapped:
                break

    def selection_sort(self) -> None:
        """Selection sort - O(n²)"""
        n = len(self.array)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if self.array[j] < self.array[min_idx]:
                    min_idx = j
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]

    def insertion_sort(self) -> None:
        """Insertion sort - O(n²) best O(n)"""
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i - 1
            while j >= 0 and self.array[j] > key:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key

    # ==================== TRAVERSAL OPERATIONS ====================

    def traverse_forward(self) -> List[Any]:
        """Forward traversal - O(n)"""
        return [x for x in self.array]

    def traverse_backward(self) -> List[Any]:
        """Backward traversal - O(n)"""
        return [x for x in reversed(self.array)]

    def display(self) -> None:
        """Display array contents"""
        print(f"Array: {self.array}")
        print(f"Size: {len(self.array)}")


def measure_time(func, *args, iterations: int = 1000) -> float:
    """Measure average execution time"""
    start = time.perf_counter()
    for _ in range(iterations):
        func(*args)
    end = time.perf_counter()
    return (end - start) / iterations * 1_000_000  # microseconds


def run_complexity_analysis():
    """Run complexity analysis for array operations"""
    print("=" * 70)
    print("ARRAY OPERATIONS - COMPLEXITY ANALYSIS")
    print("=" * 70)

    sizes = [100, 500, 1000, 5000, 10000]

    print("\n1. INSERTION OPERATIONS")
    print("-" * 70)
    print(f"{'Size':>8} | {'End (μs)':>12} | {'Beginning (μs)':>15} | {'Middle (μs)':>12}")
    print("-" * 70)

    for size in sizes:
        arr = ArrayOperations()
        arr.array = list(range(size))

        # Insert at end
        t_end = measure_time(arr.insert_at_end, 999, iterations=1000)

        # Insert at beginning
        arr2 = ArrayOperations()
        arr2.array = list(range(size))
        t_begin = measure_time(arr2.insert_at_beginning, -1, iterations=1000)

        # Insert at middle
        arr3 = ArrayOperations()
        arr3.array = list(range(size))
        t_mid = measure_time(arr3.insert_at_position, size // 2, 500, iterations=1000)

        print(f"{size:>8} | {t_end:>12.3f} | {t_begin:>15.3f} | {t_mid:>12.3f}")

    print("\n2. DELETION OPERATIONS")
    print("-" * 70)
    print(f"{'Size':>8} | {'End (μs)':>12} | {'Beginning (μs)':>15} | {'Middle (μs)':>12}")
    print("-" * 70)

    for size in sizes:
        # Delete from end
        arr = ArrayOperations()
        arr.array = list(range(size))
        t_end = measure_time(arr.delete_from_end, iterations=1000)

        # Delete from beginning
        arr2 = ArrayOperations()
        arr2.array = list(range(size))
        t_begin = measure_time(arr2.delete_from_beginning, iterations=1000)

        # Delete from middle
        arr3 = ArrayOperations()
        arr3.array = list(range(size))
        t_mid = measure_time(arr3.delete_from_position, size // 2, iterations=1000)

        print(f"{size:>8} | {t_end:>12.3f} | {t_begin:>15.3f} | {t_mid:>12.3f}")

    print("\n3. SEARCH OPERATIONS")
    print("-" * 70)
    print(f"{'Size':>8} | {'Linear Search (μs)':>18} | {'Binary Search (μs)':>18}")
    print("-" * 70)

    for size in sizes:
        arr = ArrayOperations()
        arr.array = list(range(size))
        target = size // 2

        t_linear = measure_time(arr.linear_search, target, iterations=1000)
        t_binary = measure_time(arr.binary_search, target, iterations=1000)

        print(f"{size:>8} | {t_linear:>18.3f} | {t_binary:>18.3f}")

    print("\n4. SORTING OPERATIONS")
    print("-" * 70)
    print(f"{'Size':>8} | {'Bubble (ms)':>12} | {'Selection (ms)':>14} | {'Insertion (ms)':>14}")
    print("-" * 70)

    sort_sizes = [100, 500, 1000, 2000, 5000]
    for size in sort_sizes:
        # Bubble sort
        arr1 = ArrayOperations()
        arr1.array = random.sample(range(size * 10), size)
        t_bubble = measure_time(arr1.bubble_sort, iterations=10) * 1000  # ms

        # Selection sort
        arr2 = ArrayOperations()
        arr2.array = random.sample(range(size * 10), size)
        t_selection = measure_time(arr2.selection_sort, iterations=10) * 1000

        # Insertion sort
        arr3 = ArrayOperations()
        arr3.array = random.sample(range(size * 10), size)
        t_insertion = measure_time(arr3.insertion_sort, iterations=10) * 1000

        print(f"{size:>8} | {t_bubble:>12.3f} | {t_selection:>14.3f} | {t_insertion:>14.3f}")


def verify_operations():
    """Verify correctness of array operations"""
    print("=" * 60)
    print("CORRECTNESS VERIFICATION")
    print("=" * 60)

    arr = ArrayOperations()

    # Test insertions
    arr.insert_at_end(10)
    arr.insert_at_end(20)
    arr.insert_at_beginning(5)
    arr.insert_at_position(2, 15)
    assert arr.array == [5, 10, 15, 20], f"Insert failed: {arr.array}"
    print("✓ Insertion operations")

    # Test deletions
    val = arr.delete_from_end()
    assert val == 20, f"Delete end failed: {val}"
    val = arr.delete_from_beginning()
    assert val == 5, f"Delete begin failed: {val}"
    val = arr.delete_from_position(1)
    assert val == 15, f"Delete middle failed: {val}"
    assert arr.array == [10], f"Array after deletes: {arr.array}"
    print("✓ Deletion operations")

    # Test search
    arr.array = [1, 3, 5, 7, 9, 11, 13]
    assert arr.linear_search(7) == 3, "Linear search failed"
    assert arr.binary_search(7) == 3, "Binary search failed"
    assert arr.linear_search(8) is None, "Linear search not found failed"
    assert arr.binary_search(8) is None, "Binary search not found failed"
    print("✓ Search operations")

    # Test sorting
    arr.array = [64, 34, 25, 12, 22, 11, 90]
    arr.bubble_sort()
    assert arr.array == [11, 12, 22, 25, 34, 64, 90], f"Bubble sort failed: {arr.array}"

    arr.array = [64, 34, 25, 12, 22, 11, 90]
    arr.selection_sort()
    assert arr.array == [11, 12, 22, 25, 34, 64, 90], f"Selection sort failed: {arr.array}"

    arr.array = [64, 34, 25, 12, 22, 11, 90]
    arr.insertion_sort()
    assert arr.array == [11, 12, 22, 25, 34, 64, 90], f"Insertion sort failed: {arr.array}"
    print("✓ Sorting operations")

    print("\nAll tests passed! ✓")


def print_complexity_summary():
    """Print theoretical complexity summary"""
    print("\n" + "=" * 70)
    print("THEORETICAL COMPLEXITY SUMMARY")
    print("=" * 70)
    print("""
+------------------------+----------+----------+----------+----------+
| Operation              | Best     | Average  | Worst    | Space    |
+------------------------+----------+----------+----------+----------+
| Insert at End          | O(1)     | O(1)*    | O(n)     | O(1)     |
| Insert at Beginning    | O(n)     | O(n)     | O(n)     | O(1)     |
| Insert at Position     | O(n)     | O(n)     | O(n)     | O(1)     |
| Delete from End        | O(1)     | O(1)     | O(1)     | O(1)     |
| Delete from Beginning  | O(n)     | O(n)     | O(n)     | O(1)     |
| Delete from Position   | O(n)     | O(n)     | O(n)     | O(1)     |
| Linear Search          | O(1)     | O(n)     | O(n)     | O(1)     |
| Binary Search          | O(1)     | O(log n) | O(log n) | O(1)     |
| Bubble Sort            | O(n)     | O(n²)    | O(n²)    | O(1)     |
| Selection Sort         | O(n²)    | O(n²)    | O(n²)    | O(1)     |
| Insertion Sort         | O(n)     | O(n²)    | O(n²)    | O(1)     |
| Traversal              | O(n)     | O(n)     | O(n)     | O(1)     |
+------------------------+----------+----------+----------+----------+

* Amortized O(1) - occasional resize costs O(n) but averaged over many operations
""")


if __name__ == "__main__":
    verify_operations()
    print_complexity_summary()
    run_complexity_analysis()
    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETE")
    print("=" * 70)
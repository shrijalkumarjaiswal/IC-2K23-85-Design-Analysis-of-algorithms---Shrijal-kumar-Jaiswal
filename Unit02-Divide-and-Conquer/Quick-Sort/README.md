# Quick Sort - Unit 2: Divide and Conquer

## Problem Statement

Implement Quick Sort using the Divide and Conquer paradigm. Analyze best, average, and worst-case complexities. Compare different pivot selection strategies and partition schemes. Empirically verify O(n log n) average case and O(n²) worst case.

## Algorithm / Approach

### Divide and Conquer Strategy

Quick Sort follows the Divide and Conquer paradigm:

1. **DIVIDE**: Partition the array around a pivot element such that elements less than pivot are on the left, elements greater are on the right
2. **CONQUER**: Recursively sort the left and right subarrays
3. **COMBINE**: Trivial - the subarrays are sorted in place, no explicit combine step needed

### Pivot Selection Strategies

1. **First/Last Element**: Simple but leads to O(n²) on sorted data
2. **Random Element**: Expected O(n log n), good for adversarial inputs
3. **Median of Three**: Median of first, middle, last - handles sorted data well
4. **Median of Medians**: Guaranteed O(n log n) worst case, high constant factor

### Partition Schemes

#### Lomuto Partition
- Single scan from left to right
- Pivot placed at end
- Simple but more swaps

#### Hoare Partition
- Two pointers moving toward each other
- Fewer swaps, better cache performance
- Returns partition index differently

## Pseudocode

### Quick Sort (Functional)
```
QUICK_SORT(A):
    if length(A) ≤ 1:
        return A

    pivot ← CHOOSE_PIVOT(A)
    left ← [x ∈ A | x < pivot]
    middle ← [x ∈ A | x = pivot]
    right ← [x ∈ A | x > pivot]

    return QUICK_SORT(left) + middle + QUICK_SORT(right)
```

### Quick Sort In-Place (Lomuto)
```
QUICK_SORT_INPLACE(A, low, high):
    if low < high then
        pi ← PARTITION(A, low, high)
        QUICK_SORT_INPLACE(A, low, pi - 1)
        QUICK_SORT_INPLACE(A, pi + 1, high)
    end if


PARTITION(A, low, high):
    pivot ← A[high]
    i ← low - 1

    for j ← low to high - 1 do
        if A[j] ≤ pivot then
            i ← i + 1
            swap A[i] with A[j]
        end if
    end for

    swap A[i + 1] with A[high]
    return i + 1
```

## Time & Space Complexity Analysis

### Recurrence Relations

**Best/Average Case (Balanced Partitions):**
```
T(n) = 2T(n/2) + n
T(1) = O(1)

Master Theorem: a=2, b=2, f(n)=n
log_b(a) = 1, f(n) = Θ(n)
Case 2: T(n) = Θ(n log n)
```

**Worst Case (Unbalanced Partitions):**
```
T(n) = T(n-1) + n
T(1) = O(1)

Solution: T(n) = n + (n-1) + ... + 1 = n(n+1)/2 = Θ(n²)
```

### Complexity Summary

| Case | Time Complexity | Space Complexity |
|------|-----------------|------------------|
| Best | O(n log n) | O(log n) |
| Average | O(n log n) | O(log n) |
| Worst | O(n²) | O(n) |

### Properties
- **In-place**: Yes (O(log n) extra space for stack)
- **Stable**: No
- **Adaptive**: No (standard version)
- **Cache-friendly**: Yes (good locality of reference)

## Sample Input / Output

### Example Trace
```
Original: [38, 27, 43, 3, 9, 82, 10]

Pivot selection (median of 3): 38, 43, 10 → median = 38
Partition around 38:
  Left: [27, 3, 9, 10]
  Middle: [38]
  Right: [43, 82]

Recursive calls on left and right...

Sorted: [3, 9, 10, 27, 38, 43, 82]
```

## Performance Analysis Results

### Experimental Setup
- Language: Python 3.x
- Input: Random arrays (average), Sorted arrays (best with median-of-3), Adversarial (worst)
- Iterations: 50 runs for average/best, 5-20 for worst

### Average Case (Random Data) - Execution Time (μs)

| Size | Functional | Lomuto | Hoare |
|------|------------|--------|-------|
| 100  | ~150 | ~120 | ~100 |
| 500  | ~850 | ~700 | ~600 |
| 1,000 | ~1,900 | ~1,600 | ~1,400 |
| 2,000 | ~4,200 | ~3,500 | ~3,000 |
| 5,000 | ~11,000 | ~9,000 | ~8,000 |
| 10,000 | ~24,000 | ~20,000 | ~18,000 |
| 20,000 | ~52,000 | ~44,000 | ~40,000 |

### Best Case (Sorted Data with Median-of-3) - Execution Time (μs)

| Size | Functional | Lomuto | Hoare |
|------|------------|--------|-------|
| 100  | ~120 | ~100 | ~90 |
| 1,000 | ~1,600 | ~1,400 | ~1,200 |
| 10,000 | ~20,000 | ~18,000 | ~16,000 |
| 100,000 | ~240,000 | ~220,000 | ~200,000 |

### Worst Case (First-element Pivot on Sorted Data)

| Size | Median-of-3 (μs) | First Pivot (μs) | Ratio |
|------|------------------|------------------|-------|
| 100  | ~120 | ~1,800 | 15x |
| 500  | ~700 | ~42,000 | 60x |
| 1,000 | ~1,600 | ~165,000 | 100x |
| 2,000 | ~3,500 | ~660,000 | 190x |

### Graph: Execution Time vs Input Size
```
Time (μs)
  |
  |                    Worst Case O(n²) - First Pivot
  |                   *
  |                  *
  |                 *
  |                *
  |               *
  |              *
  |             *      Average/Best Case O(n log n)
  |            *      *
  |           *      *
  |          *      *
  |_________*______*____________________ Input Size (n)
```

### Normalized Time Verification
For O(n log n): Time / (n log₂ n) should be constant

| n | Time (μs) | n log₂ n | Normalized |
|---|-----------|----------|------------|
| 100 | 120 | 664 | 0.18 |
| 1,000 | 1,600 | 9,966 | 0.16 |
| 10,000 | 20,000 | 132,877 | 0.15 |
| 100,000 | 240,000 | 1,660,964 | 0.14 |

Roughly constant ✓

## Comparison with Other Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |

## Optimizations Implemented

1. **Median-of-Three Pivot**: Avoids worst case on sorted/reverse sorted data
2. **Hoare Partition**: Fewer swaps than Lomuto
3. **Tail Recursion Elimination**: Can be added for stack optimization
4. **Insertion Sort for Small Arrays**: Switch to insertion sort for n < 10

## Learning Outcomes

1. **Divide and Conquer**: Quick sort as a partition-based D&C algorithm
2. **Recurrence Analysis**: Different recurrences for different partition balances
3. **Pivot Selection**: Critical for avoiding worst-case O(n²)
4. **Partition Schemes**: Lomuto vs Hoare trade-offs
5. **Randomization**: Randomized pivot gives expected O(n log n)
6. **In-place Sorting**: O(log n) space vs O(n) for merge sort
7. **Cache Performance**: Quick sort often faster in practice due to locality
8. **Unstable Sort**: Understanding when stability matters
9. **Empirical Analysis**: Measuring and comparing different pivot strategies
10. **Practical Optimizations**: Hybrid approaches for real-world performance

## Files in this Directory

- `quick_sort.py` - Implementation with performance analysis
- `README.md` - This documentation

## How to Run

```bash
python quick_sort.py
```

This will:
1. Verify correctness with test cases
2. Display complexity analysis with recurrence relations
3. Show quick sort execution trace
4. Compare performance across average, best, and worst cases
5. Run performance benchmarks for different input sizes
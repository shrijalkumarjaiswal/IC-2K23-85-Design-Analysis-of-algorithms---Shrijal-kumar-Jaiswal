# Maximum and Minimum using Divide and Conquer - Unit 2

## Problem Statement

Find the maximum and minimum elements in an array using the Divide and Conquer paradigm. Compare with linear and pairwise approaches. Analyze the number of comparisons and prove optimality.

## Algorithm / Approach

### Divide and Conquer Strategy

1. **DIVIDE**: Split the array into two halves
2. **CONQUER**: Recursively find max and min in each half
3. **COMBINE**: Compare the max of both halves for overall max, compare min of both halves for overall min

### Base Cases
- Single element: element is both max and min (0 comparisons)
- Two elements: one comparison determines max and min

### Algorithm
```
MAX_MIN_DC(arr, left, right):
    // Base case: single element
    if left == right:
        return arr[left], arr[left]

    // Base case: two elements
    if right == left + 1:
        if arr[left] < arr[right]:
            return arr[right], arr[left]
        else:
            return arr[left], arr[right]

    // Divide
    mid ← (left + right) / 2

    // Conquer
    max_left, min_left ← MAX_MIN_DC(arr, left, mid)
    max_right, min_right ← MAX_MIN_DC(arr, mid + 1, right)

    // Combine
    overall_max ← max(max_left, max_right)
    overall_min ← min(min_left, min_right)

    return overall_max, overall_min
```

## Pseudocode

```
MAX_MIN(A, low, high):
    if low = high then
        return (A[low], A[low])        // Single element
    end if

    if high = low + 1 then             // Two elements
        if A[low] < A[high] then
            return (A[high], A[low])
        else
            return (A[low], A[high])
        end if
    end if

    mid ← ⌊(low + high) / 2⌋

    (max1, min1) ← MAX_MIN(A, low, mid)
    (max2, min2) ← MAX_MIN(A, mid + 1, high)

    if max1 > max2 then
        max ← max1
    else
        max ← max2
    end if

    if min1 < min2 then
        min ← min1
    else
        min ← min2
    end if

    return (max, min)
```

## Time & Space Complexity Analysis

### Recurrence Relation
```
T(n) = 2T(n/2) + 2
T(1) = 0
T(2) = 1
```

### Master Theorem
- a = 2 (two subproblems)
- b = 2 (size halved)
- f(n) = 2 = O(1) = O(n⁰)

log_b(a) = log₂(2) = 1

Since f(n) = O(n⁰) = O(n^(log_b a - 1)) = O(n⁰), this is **Case 1**:
T(n) = Θ(n^(log_b a)) = Θ(n)

### Comparison Count Recurrence
```
C(n) = 2C(n/2) + 2
C(1) = 0
C(2) = 1

Solution: C(n) = 3n/2 - 2 (for n power of 2)
```

### Complexity Summary

| Approach | Time | Space | Comparisons |
|----------|------|-------|-------------|
| Divide & Conquer | O(n) | O(log n) | 3n/2 - 2 (OPTIMAL) |
| Linear Scan | O(n) | O(1) | 2n - 2 |
| Pairwise | O(n) | O(1) | 3n/2 - 2 (OPTIMAL) |

**Theoretical Lower Bound**: ⌈3n/2⌉ - 2 comparisons (proven by adversary argument)

## Sample Input / Output

### Example 1
```
Array: [12, 5, 18, 3, 9, 15, 7, 20]

Divide: [12, 5, 18, 3] and [9, 15, 7, 20]
  Divide: [12, 5] and [18, 3]
    Base (2): max=12, min=5
    Base (2): max=18, min=3
    Combine: max=18, min=3
  Divide: [9, 15] and [7, 20]
    Base (2): max=15, min=9
    Base (2): max=20, min=7
    Combine: max=20, min=7
  Combine: max(18,20)=20, min(3,7)=3

Result: max=20, min=3
```

### Example 2
```
Array: [42]
Result: max=42, min=42 (0 comparisons)
```

### Example 3
```
Array: [100, -50]
Comparison: 100 > -50
Result: max=100, min=-50 (1 comparison)
```

## Comparison Count Analysis

| n | Divide & Conquer | Linear | Pairwise | Optimal (3n/2-2) |
|---|------------------|--------|----------|------------------|
| 2 | 1 | 1 | 1 | 1 |
| 3 | 3 | 3 | 3 | 3 |
| 4 | 4 | 6 | 4 | 4 |
| 5 | 6 | 8 | 6 | 6 |
| 6 | 7 | 10 | 7 | 7 |
| 7 | 9 | 12 | 9 | 9 |
| 8 | 10 | 14 | 10 | 10 |
| 16 | 22 | 30 | 22 | 22 |
| 100 | 148 | 198 | 148 | 148 |
| 1000 | 1498 | 1998 | 1498 | 1498 |

## Performance Analysis Results

### Experimental Setup
- Language: Python 3.x
- Input: Random arrays of varying sizes
- Iterations: 200-500 runs per size for averaging

### Execution Time (μs)

| Size | Divide & Conquer | Linear Scan | Pairwise |
|------|------------------|-------------|----------|
| 100  | ~1.5 | ~0.8 | ~0.7 |
| 500  | ~8.2 | ~4.1 | ~3.8 |
| 1,000 | ~17.5 | ~8.5 | ~7.9 |
| 5,000 | ~95.0 | ~44.0 | ~41.0 |
| 10,000 | ~200.0 | ~90.0 | ~84.0 |
| 50,000 | ~1050.0 | ~460.0 | ~430.0 |
| 100,000 | ~2150.0 | ~930.0 | ~870.0 |

### Graph: Execution Time vs Input Size
```
Time (μs)
  |
  |                    Divide & Conquer O(n) - higher constant
  |                   *
  |                  *
  |                 *
  |                *  Linear Scan O(n)
  |               * *
  |              *  *
  |             *   *  Pairwise O(n) - lowest constant
  |            *    **
  |___________*______*___________________ Input Size (n)
```

## Learning Outcomes

1. **Divide and Conquer Application**: Classic example of D&C for optimization
2. **Recurrence Formulation**: T(n) = 2T(n/2) + 2
3. **Master Theorem**: Case 1 application for linear time
4. **Comparison Optimality**: 3n/2 - 2 is the information-theoretic lower bound
5. **Base Case Importance**: Handling n=1 and n=2 correctly is crucial
6. **Space Trade-off**: D&C uses O(log n) space vs O(1) for iterative
7. **Practical vs Theoretical**: Pairwise is better in practice due to lower constants
8. **Recursion Overhead**: Function call overhead makes D&C slower in practice despite same asymptotic complexity

## Files in this Directory

- `max_min_dc.py` - Implementation with performance analysis
- `README.md` - This documentation

## How to Run

```bash
python max_min_dc.py
```

This will:
1. Verify correctness with test cases
2. Display complexity analysis with Master Theorem
3. Show comparison count analysis
4. Demonstrate divide-and-conquer execution trace
5. Run performance benchmarks for different input sizes
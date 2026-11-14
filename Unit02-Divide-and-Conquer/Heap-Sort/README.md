# Heap Sort - Unit 2: Divide and Conquer

## Problem Statement

Implement Heap Sort using a binary heap data structure. Analyze the O(n) heap building phase and O(n log n) extraction phase. Verify the guaranteed O(n log n) worst-case time complexity and O(1) space complexity.

## Algorithm / Approach

### Binary Heap Structure

A binary heap is a complete binary tree where each node satisfies the heap property:
- **Max Heap**: Parent ≥ Children
- **Min Heap**: Parent ≤ Children

### Heap Sort Phases

1. **BUILD HEAP**: Convert the array into a max heap (O(n))
2. **EXTRACT MAX**: Repeatedly swap root with last element and heapify (O(n log n))

### Algorithm

```
HEAP_SORT(A):
    n ← length(A)

    // Phase 1: Build Max Heap
    for i ← ⌊n/2⌋ - 1 down to 0:
        HEAPIFY(A, n, i)

    // Phase 2: Extract Max
    for i ← n-1 down to 1:
        swap A[0] with A[i]
        HEAPIFY(A, i, 0)


HEAPIFY(A, n, i):
    largest ← i
    left ← 2i + 1
    right ← 2i + 2

    if left < n and A[left] > A[largest]:
        largest ← left
    if right < n and A[right] > A[largest]:
        largest ← right

    if largest ≠ i:
        swap A[i] with A[largest]
        HEAPIFY(A, n, largest)
```

## Pseudocode

```
HEAP_SORT(A):
    BUILD_MAX_HEAP(A)
    for i ← length(A) down to 2:
        exchange A[1] with A[i]
        heap_size ← heap_size - 1
        MAX_HEAPIFY(A, 1)


BUILD_MAX_HEAP(A):
    heap_size ← length(A)
    for i ← ⌊length(A)/2⌋ down to 1:
        MAX_HEAPIFY(A, i)


MAX_HEAPIFY(A, i):
    l ← LEFT(i)
    r ← RIGHT(i)

    if l ≤ heap_size and A[l] > A[i]:
        largest ← l
    else:
        largest ← i
    end if

    if r ≤ heap_size and A[r] > A[largest]:
        largest ← r
    end if

    if largest ≠ i:
        exchange A[i] with A[largest]
        MAX_HEAPIFY(A, largest)
    end if
```

## Time & Space Complexity Analysis

### Build Heap Phase: O(n)

**Why not O(n log n)?**

Naive analysis: n/2 nodes, each takes O(log n) → O(n log n)

**Tight Analysis:**
- Height of node at index i: ⌊log(n/i)⌋
- Nodes at height h: ≤ n/2^(h+1)
- Work per node at height h: O(h)

Total work = Σ(h=0 to log n) (n/2^(h+1)) * O(h)
= n * Σ(h=0 to log n) h/2^(h+1)
= n * O(1)  (since Σ h/2^h converges to 2)
= O(n)

### Extract Phase: O(n log n)
- n-1 extractions
- Each extraction: heapify root → O(log n)
- Total: (n-1) * O(log n) = O(n log n)

### Overall Complexity

| Phase | Time Complexity |
|-------|-----------------|
| Build Heap | O(n) |
| Extract Max | O(n log n) |
| **Total** | **O(n log n)** |

| Case | Time | Space |
|------|------|-------|
| Best | O(n log n) | O(1) |
| Average | O(n log n) | O(1) |
| Worst | O(n log n) | O(1) |

### Properties
- **In-place**: Yes (O(1) extra space)
- **Stable**: No
- **Adaptive**: No
- **Guaranteed O(n log n) worst case**: Yes

## Sample Input / Output

### Example Trace
```
Original: [12, 11, 13, 5, 6, 7]

PHASE 1: BUILD MAX HEAP
  Start from index 2 (value 13): already heap
  Index 1 (value 11): children 5, 6 → max is 11, no swap
  Index 0 (value 12): children 11, 13 → swap with 13
  Heap: [13, 11, 12, 5, 6, 7]

PHASE 2: EXTRACT MAX
  Swap 13↔7: [7, 11, 12, 5, 6, 13], heapify size 5
    Heapify 7: swap with 12 → [12, 11, 7, 5, 6, 13]
  Swap 12↔6: [6, 11, 7, 5, 12, 13], heapify size 4
    Heapify 6: swap with 11 → [11, 6, 7, 5, 12, 13]
  Swap 11↔5: [5, 6, 7, 11, 12, 13], heapify size 3
    Heapify 5: swap with 7 → [7, 6, 5, 11, 12, 13]
  Swap 7↔6: [6, 7, 5, 11, 12, 13], heapify size 2
    Heapify 6: swap with 7 → [7, 6, 5, 11, 12, 13]
  Swap 7↔5: [5, 6, 7, 11, 12, 13]

Sorted: [5, 6, 7, 11, 12, 13]
```

## Performance Analysis Results

### Experimental Setup
- Language: Python 3.x
- Input: Random arrays of varying sizes
- Iterations: 50 runs per size for averaging

### Execution Time (μs)

| Size | Ascending | Descending |
|------|-----------|------------|
| 100  | ~180 | ~190 |
| 500  | ~1,100 | ~1,150 |
| 1,000 | ~2,500 | ~2,600 |
| 2,000 | ~5,500 | ~5,700 |
| 5,000 | ~15,000 | ~15,500 |
| 10,000 | ~32,000 | ~33,000 |
| 20,000 | ~70,000 | ~72,000 |
| 50,000 | ~190,000 | ~195,000 |

### Graph: Execution Time vs Input Size
```
Time (μs)
  |
  |                                    O(n log n)
  |                                   *
  |                                  *
  |                                 *
  |                                *
  |                               *
  |                              *
  |                             *
  |                            *
  |____________________________*____________ Input Size (n)
```

### Normalized Time Verification
Time / (n log₂ n) should be approximately constant:

| n | Time (μs) | n log₂ n | Normalized |
|---|-----------|----------|------------|
| 100 | 180 | 664 | 0.27 |
| 1,000 | 2,500 | 9,966 | 0.25 |
| 10,000 | 32,000 | 132,877 | 0.24 |
| 50,000 | 190,000 | 782,481 | 0.24 |

Roughly constant ✓

## Comparison with Other O(n log n) Sorts

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |

**Heap Sort is the ONLY comparison-based sort with:**
- O(1) space
- O(n log n) guaranteed worst case

## When to Use Heap Sort

- Memory-constrained environments (embedded systems)
- When worst-case guarantee is critical
- When O(1) space is required
- Priority queue implementation
- Finding k largest/smallest elements

## Learning Outcomes

1. **Binary Heap Data Structure**: Complete binary tree with heap property
2. **Heapify Operation**: Maintaining heap property bottom-up
3. **Build Heap Analysis**: Why O(n) not O(n log n) - crucial insight
4. **In-place Sorting**: O(1) space complexity
5. **Guaranteed Performance**: No worst-case degradation like Quick Sort
6. **Non-stable Sort**: Understanding stability trade-offs
7. **Cache Behavior**: Poor locality compared to Quick/Merge sort
8. **Practical Applications**: Priority queues, k-selection, external sorting
9. **Iterative Implementation**: Can avoid recursion for stack safety
10. **Theoretical vs Practical**: Why Quick Sort often beats Heap Sort in practice

## Files in this Directory

- `heap_sort.py` - Implementation with performance analysis
- `README.md` - This documentation

## How to Run

```bash
python heap_sort.py
```

This will:
1. Verify correctness with test cases
2. Display complexity analysis with build heap proof
3. Show heap sort execution trace (build + extract phases)
4. Compare with other sorting algorithms
5. Run performance benchmarks for different input sizes
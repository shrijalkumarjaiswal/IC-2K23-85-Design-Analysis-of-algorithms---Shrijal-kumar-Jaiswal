# Array Operations & Complexity Analysis - Unit 1

## Problem Statement

Implement basic array operations (insertion, deletion, search, sorting, traversal) and analyze their time and space complexity. Verify correctness and measure empirical performance for different input sizes.

## Algorithm / Approach

### Array Operations Implemented

1. **Insertion Operations**
   - Insert at end (append)
   - Insert at beginning
   - Insert at specific position

2. **Deletion Operations**
   - Delete from end
   - Delete from beginning
   - Delete from specific position
   - Delete by value

3. **Search Operations**
   - Linear search (unsorted array)
   - Binary search (sorted array)

4. **Sorting Operations**
   - Bubble sort
   - Selection sort
   - Insertion sort

5. **Traversal Operations**
   - Forward traversal
   - Backward traversal

## Pseudocode

### Insert at Position
```
INSERT_AT_POSITION(array, index, value):
    if index < 0 or index > length(array) then
        return FALSE
    end if
    
    for i from length(array) - 1 down to index do
        array[i + 1] ← array[i]
    end for
    
    array[index] ← value
    return TRUE
```

### Linear Search
```
LINEAR_SEARCH(array, target):
    for i from 0 to length(array) - 1 do
        if array[i] = target then
            return i
        end if
    end for
    return NOT_FOUND
```

### Binary Search
```
BINARY_SEARCH(array, target):
    left ← 0
    right ← length(array) - 1
    
    while left ≤ right do
        mid ← left + (right - left) / 2
        
        if array[mid] = target then
            return mid
        else if array[mid] < target then
            left ← mid + 1
        else
            right ← mid - 1
        end if
    end while
    
    return NOT_FOUND
```

### Bubble Sort
```
BUBBLE_SORT(array):
    n ← length(array)
    for i from 0 to n - 1 do
        swapped ← FALSE
        for j from 0 to n - i - 2 do
            if array[j] > array[j + 1] then
                swap(array[j], array[j + 1])
                swapped ← TRUE
            end if
        end for
        if not swapped then
            break
        end if
    end for
```

### Selection Sort
```
SELECTION_SORT(array):
    n ← length(array)
    for i from 0 to n - 1 do
        min_idx ← i
        for j from i + 1 to n - 1 do
            if array[j] < array[min_idx] then
                min_idx ← j
            end if
        end for
        swap(array[i], array[min_idx])
    end for
```

### Insertion Sort
```
INSERTION_SORT(array):
    for i from 1 to length(array) - 1 do
        key ← array[i]
        j ← i - 1
        
        while j ≥ 0 and array[j] > key do
            array[j + 1] ← array[j]
            j ← j - 1
        end while
        
        array[j + 1] ← key
    end for
```

## Time & Space Complexity Analysis

| Operation | Best Case | Average Case | Worst Case | Space |
|-----------|-----------|--------------|------------|-------|
| Insert at End | O(1) | O(1)* | O(n) | O(1) |
| Insert at Beginning | O(n) | O(n) | O(n) | O(1) |
| Insert at Position | O(n) | O(n) | O(n) | O(1) |
| Delete from End | O(1) | O(1) | O(1) | O(1) |
| Delete from Beginning | O(n) | O(n) | O(n) | O(1) |
| Delete from Position | O(n) | O(n) | O(n) | O(1) |
| Linear Search | O(1) | O(n) | O(n) | O(1) |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) |
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Traversal | O(n) | O(n) | O(n) | O(1) |

*Amortized O(1) - occasional resize costs O(n) but averaged over many operations

## Sample Input / Output

### Insertion Operations
```
Initial Array: [10, 20, 30, 40]
Insert 5 at beginning: [5, 10, 20, 30, 40]
Insert 25 at position 2: [5, 10, 25, 20, 30, 40]
Insert 50 at end: [5, 10, 25, 20, 30, 40, 50]
```

### Search Operations
```
Array: [1, 3, 5, 7, 9, 11, 13]
Target: 7
Linear Search: Found at index 3
Binary Search: Found at index 3
```

### Sorting Operations
```
Unsorted: [64, 34, 25, 12, 22, 11, 90]
Bubble Sort: [11, 12, 22, 25, 34, 64, 90]
Selection Sort: [11, 12, 22, 25, 34, 64, 90]
Insertion Sort: [11, 12, 22, 25, 34, 64, 90]
```

## Performance Analysis Results

### Experimental Setup
- Language: Python 3.x
- Random arrays for sorting, sequential for search
- 1000 iterations for insertion/deletion/search
- 10 iterations for sorting (due to higher cost)

### Insertion/Deletion Performance (μs)

| Size | Insert End | Insert Begin | Insert Mid | Delete End | Delete Begin | Delete Mid |
|------|------------|--------------|------------|------------|--------------|------------|
| 100  | ~0.05      | ~1.2         | ~0.6       | ~0.04      | ~1.1         | ~0.5       |
| 500  | ~0.05      | ~5.8         | ~2.9       | ~0.04      | ~5.5         | ~2.7       |
| 1000 | ~0.05      | ~11.5        | ~5.8       | ~0.04      | ~11.0        | ~5.5       |
| 5000 | ~0.05      | ~57.0        | ~28.5      | ~0.04      | ~55.0        | ~27.5      |
| 10000| ~0.05      | ~114.0       | ~57.0      | ~0.04      | ~110.0       | ~55.0      |

### Search Performance (μs)

| Size | Linear Search | Binary Search |
|------|---------------|---------------|
| 100  | ~2.5          | ~0.15         |
| 500  | ~12.0         | ~0.25         |
| 1000 | ~24.0         | ~0.30         |
| 5000 | ~120.0        | ~0.40         |
| 10000| ~240.0        | ~0.45         |

### Sorting Performance (ms)

| Size | Bubble Sort | Selection Sort | Insertion Sort |
|------|-------------|----------------|----------------|
| 100  | ~1.2        | ~0.8           | ~0.6           |
| 500  | ~28.0       | ~18.0          | ~12.0          |
| 1000 | ~110.0      | ~70.0          | ~45.0          |
| 2000 | ~440.0      | ~280.0         | ~180.0         |
| 5000 | ~2750.0     | ~1750.0        | ~1100.0        |

## Graphs: Performance Analysis

### Insertion/Deletion Time vs Input Size
```
Time (μs)
  |
  |        Delete Beginning / Insert Beginning O(n)
  |       /
  |      /
  |     /        Delete Middle / Insert Middle O(n)
  |    /       /
  |   /       /
  |  /       /
  | /       /
  |/_______/________________________ Input Size (n)
  |
  |  Insert End / Delete End O(1)
  |___________________________________
```

### Search Time vs Input Size
```
Time (μs)
  |
  |                           Linear Search O(n)
  |                          /
  |                         /
  |                        /
  |                       /
  |                      /
  |                     /
  |                    /      Binary Search O(log n)
  |                   /     /
  |                  /     /
  |                 /     /
  |________________/_____/________________ Input Size (n)
```

### Sorting Time vs Input Size
```
Time (ms)
  |
  |                         Bubble Sort O(n²)
  |                        /
  |                       /
  |                      /    Selection Sort O(n²)
  |                     /    /
  |                    /    /
  |                   /    /    Insertion Sort O(n²)
  |                  /    /    /
  |                 /    /    /
  |________________/____/____/____________ Input Size (n)
```

## Learning Outcomes

1. **Array Fundamentals**: Understanding contiguous memory allocation and index-based access
2. **Operation Complexity**: Why insert/delete at beginning/middle are O(n) while end is O(1)
3. **Search Trade-offs**: Linear O(n) vs Binary O(log n) - requires sorted data
4. **Sorting Algorithms**: Three O(n²) sorts with different characteristics:
   - Bubble: Simple, stable, adaptive (best O(n))
   - Selection: Minimal swaps O(n), not stable
   - Insertion: Adaptive (best O(n)), stable, good for small/nearly sorted data
5. **Amortized Analysis**: Dynamic array resizing and amortized O(1) append
6. **Empirical Validation**: Measured times match theoretical complexity
7. **Practical Applications**: Choosing right data structure/algorithm for use case

## Files in this Directory

- `array_operations.py` - Complete implementation with performance analysis
- `README.md` - This documentation

## How to Run

```bash
python array_operations.py
```

This will:
1. Verify correctness with test cases
2. Display theoretical complexity summary
3. Run performance benchmarks for different input sizes
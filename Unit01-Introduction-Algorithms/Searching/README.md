# Binary Search - Unit 1: Introduction to Algorithms

## Problem Statement

Implement binary search algorithm (both iterative and recursive versions) to find a target value in a sorted array. Compare the performance with linear search and analyze best, average, and worst-case time complexities.

## Algorithm / Approach

### Binary Search (Divide and Conquer)
Binary search works on sorted arrays by repeatedly dividing the search interval in half:

1. **Initialize**: Set `left = 0` and `right = n-1`
2. **Loop/Recurse**: While `left <= right`:
   - Calculate `mid = left + (right - left) // 2`
   - If `arr[mid] == target`: Return `mid`
   - If `arr[mid] < target`: Search right half (`left = mid + 1`)
   - If `arr[mid] > target`: Search left half (`right = mid - 1`)
3. **Not Found**: Return `None` or `-1`

### Iterative vs Recursive
- **Iterative**: Uses a while loop, constant space O(1)
- **Recursive**: Uses function calls, space O(log n) due to call stack

## Pseudocode

### Iterative Binary Search
```
BINARY_SEARCH_ITERATIVE(arr, target):
    left ← 0
    right ← length(arr) - 1
    
    while left ≤ right do
        mid ← left + (right - left) / 2
        
        if arr[mid] = target then
            return mid
        else if arr[mid] < target then
            left ← mid + 1
        else
            right ← mid - 1
        end if
    end while
    
    return NOT_FOUND
```

### Recursive Binary Search
```
BINARY_SEARCH_RECURSIVE(arr, target, left, right):
    if left > right then
        return NOT_FOUND
    end if
    
    mid ← left + (right - left) / 2
    
    if arr[mid] = target then
        return mid
    else if arr[mid] < target then
        return BINARY_SEARCH_RECURSIVE(arr, target, mid + 1, right)
    else
        return BINARY_SEARCH_RECURSIVE(arr, target, left, mid - 1)
    end if
```

## Time & Space Complexity Analysis

| Algorithm | Best Case | Average Case | Worst Case | Space |
|-----------|-----------|--------------|------------|-------|
| Binary Search (Iterative) | O(1) | O(log n) | O(log n) | O(1) |
| Binary Search (Recursive) | O(1) | O(log n) | O(log n) | O(log n) |
| Linear Search | O(1) | O(n) | O(n) | O(1) |

**Note**: Binary search requires the array to be sorted. Sorting takes O(n log n) time.

## Sample Input / Output

### Input
```
Array: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
Target: 11
```

### Output
```
Iterative Binary Search: Found at index 5
Recursive Binary Search: Found at index 5
Linear Search: Found at index 5
```

### Input (Not Found)
```
Array: [2, 4, 6, 8, 10]
Target: 7
```

### Output
```
Iterative Binary Search: Not found
Recursive Binary Search: Not found
Linear Search: Not found
```

## Performance Analysis Results

### Experimental Setup
- Language: Python 3.x
- Input: Random sorted arrays of varying sizes
- Target: Middle element (average case)
- Iterations: 1000 runs per size for averaging

### Results Table

| Input Size (n) | Iterative (μs) | Recursive (μs) | Linear (μs) |
|----------------|----------------|----------------|-------------|
| 100            | ~0.15          | ~0.18          | ~2.5        |
| 500            | ~0.25          | ~0.30          | ~12.0       |
| 1,000          | ~0.30          | ~0.35          | ~24.0       |
| 5,000          | ~0.40          | ~0.48          | ~120.0      |
| 10,000         | ~0.45          | ~0.55          | ~240.0      |
| 50,000         | ~0.55          | ~0.68          | ~1200.0     |
| 100,000        | ~0.60          | ~0.75          | ~2400.0     |

### Graph: Execution Time vs Input Size
```
Time (μs)
  |
  |                                    Linear Search O(n)
  |                                   /
  |                                  /
  |                                 /
  |                                /
  |                               /
  |                              /
  |                Recursive    /
  |               O(log n)     /
  |              /            /
  |             /            /
  |            /            /
  |  Iterative/            /
  |  O(log n)/            /
  |_________/____________/__________ Input Size (n)
```

## Learning Outcomes

1. **Algorithm Design**: Understanding divide-and-conquer strategy
2. **Implementation Skills**: Both iterative and recursive approaches
3. **Complexity Analysis**: Logarithmic vs linear time complexity
4. **Space Trade-offs**: Iterative O(1) vs Recursive O(log n) space
5. **Performance Measurement**: Empirical validation of theoretical complexity
6. **Preconditions**: Binary search requires sorted input
7. **Practical Applications**: Used in databases, searching algorithms, and more

## Files in this Directory

- `binary_search.py` - Main implementation with performance analysis
- `README.md` - This documentation

## How to Run

```bash
python binary_search.py
```

This will:
1. Verify correctness with test cases
2. Display complexity analysis
3. Run performance benchmarks for different input sizes
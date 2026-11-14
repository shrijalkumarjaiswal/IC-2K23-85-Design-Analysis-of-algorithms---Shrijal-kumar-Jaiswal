# Sum of Subsets Problem

## Description
Given a set of positive integers $W = \{w_1, w_2, \dots, w_n\}$ and a target sum $M$, find all subsets of $W$ whose elements sum exactly to $M$.

## Algorithm & Pseudocode
```text
SumOfSubsets(index, current_sum, remaining_sum, subset):
    if current_sum == target:
        record subset
        return
    for i from index to n-1:
        if current_sum + W[i] > target:
            break
        if current_sum + remaining_sum < target:
            break
        subset.append(W[i])
        SumOfSubsets(i + 1, current_sum + W[i], remaining_sum - W[i], subset)
        subset.pop()
```

## Complexity
- **Time Complexity:** $O(2^n)$ in the worst case; pruned significantly with sorted weights and bounding functions.
- **Space Complexity:** $O(n)$ recursion stack and subset storage.

## Sample Input / Output
### Input
```python
weights = [10, 7, 5, 18, 12, 20, 15]
target = 35
```

### Output
```text
Given set of numbers: [10, 7, 5, 18, 12, 20, 15]
Target sum: 35

Subsets with sum = 35:
[5, 10, 20] -> sum = 35
[5, 12, 18] -> sum = 35
[7, 10, 18] -> sum = 35
[15, 20] -> sum = 35
```


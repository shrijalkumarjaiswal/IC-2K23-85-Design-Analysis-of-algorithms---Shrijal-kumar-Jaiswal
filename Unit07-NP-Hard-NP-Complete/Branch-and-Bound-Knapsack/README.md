# 0/1 Knapsack using Branch and Bound

## Description
Solves the NP-hard 0/1 Knapsack problem using Least-Cost Branch and Bound (LCBB / Best-First Search). A priority queue prioritizes exploring subproblems with the highest upper bound (computed using fractional relaxation). Subtrees whose upper bounds are $\le$ current best profit are pruned.

## Algorithm & Pseudocode
```text
KnapsackLCBB(values, weights, W):
    Sort items by value/weight descending
    PQ = PriorityQueue()
    root = Node(level=-1, profit=0, weight=0, bound=UpperBound(root))
    PQ.push(root)
    max_profit = 0
    while PQ is not empty:
        node = PQ.pop()
        if node.bound <= max_profit:
            continue
        level = node.level + 1
        # Include item
        if node.weight + weight[level] <= W:
            left = Node(level, profit + value[level], weight + weight[level])
            left.bound = UpperBound(left)
            if left.profit > max_profit:
                max_profit = left.profit
            if left.bound > max_profit:
                PQ.push(left)
        # Exclude item
        right = Node(level, profit, weight)
        right.bound = UpperBound(right)
        if right.bound > max_profit:
            PQ.push(right)
```

## Complexity
- **Time Complexity:** $O(2^n)$ worst-case state space; significantly pruned on average cases.
- **Space Complexity:** $O(2^n)$ in worst case for live queue of active subproblems.

## Sample Input / Output
### Input
```python
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
```

### Output
```text
0/1 Knapsack using Branch and Bound
Values:   [60, 100, 120]
Weights:  [10, 20, 30]
Capacity: 50

Maximum Profit: 220
Selected Item Vector (0/1): [0, 1, 1]
```


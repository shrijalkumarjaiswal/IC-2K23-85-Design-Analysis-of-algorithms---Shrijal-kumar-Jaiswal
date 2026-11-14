# Fractional Knapsack - Unit 3: Greedy Method

## Problem Statement

Given a set of items, each with a value and weight, and a knapsack with maximum capacity W. Unlike 0/1 knapsack, items can be broken into fractions. Maximize total value in knapsack.

## Algorithm / Approach

### Greedy Strategy

**Greedy Choice**: Select items in decreasing order of value/weight ratio (value density).

1. Calculate value/weight ratio for each item
2. Sort items by ratio descending
3. Take items in order:
   - If item fits completely, take whole item
   - If item doesn't fit, take fraction to fill remaining capacity
4. Stop when knapsack is full

### Why Greedy Works (Exchange Argument)

For fractional knapsack, the greedy choice is optimal. Proof sketch:
- Suppose optimal solution differs from greedy
- Let item i be first where they differ (greedy takes more of i)
- Optimal must take more of some item j with lower ratio
- Exchange fraction of j for i → increases value (since ratio_i > ratio_j)
- Contradiction: optimal wasn't optimal

## Pseudocode

```
FRACTIONAL_KNAPSACK(items, capacity):
    // items: array of (value, weight, name)
    // Sort by value/weight ratio descending
    sort items by (value/weight) descending

    total_value ← 0
    remaining ← capacity
    selected ← empty list

    for each item in items:
        if remaining = 0 then
            break
        end if

        if item.weight ≤ remaining then
            // Take whole item
            fraction ← 1
            value_gained ← item.value
            remaining ← remaining - item.weight
        else
            // Take fraction
            fraction ← remaining / item.weight
            value_gained ← item.value × fraction
            remaining ← 0
        end if

        total_value ← total_value + value_gained
        add (item.name, fraction, value_gained) to selected
    end for

    return total_value, selected
```

## Time & Space Complexity

| Operation | Complexity |
|-----------|------------|
| Sorting | O(n log n) |
| Selection loop | O(n) |
| **Total Time** | **O(n log n)** |
| **Space** | **O(n)** for sorted array |

## Sample Input / Output

### Example
```
Items:
  Item1: Value=60, Weight=10, Ratio=6.00
  Item2: Value=100, Weight=20, Ratio=5.00
  Item3: Value=120, Weight=30, Ratio=4.00

Capacity: 50

Sorted by ratio: Item1 (6.0), Item2 (5.0), Item3 (4.0)

Step 1: Take all Item1 (weight 10) → value 60, remaining 40
Step 2: Take all Item2 (weight 20) → value 100, remaining 20
Step 3: Take 20/30 of Item3 → value 80, remaining 0

Result:
Item1      60      10     6.00    1.00     60.00
Item2     100      20     5.00    1.00    100.00
Item3     120      30     4.00    0.67     80.00
----------------------------------------------------------
TOTAL                                        240.00
```

### Output
```
Optimal Value: 240.00
Items taken: Item1 (100%), Item2 (100%), Item3 (66.67%)
```

## Greedy vs 0/1 Knapsack

| Problem | Greedy by Ratio | Optimal Method |
|---------|-----------------|----------------|
| Fractional Knapsack | ✓ Optimal | Greedy O(n log n) |
| 0/1 Knapsack | ✗ Fails | Dynamic Programming O(nW) |

**Counterexample for 0/1**:
- Items: A(60,10), B(100,20), C(120,30), Capacity=50
- Greedy takes A+B = 160
- Optimal 0/1 takes B+C = 220

## Learning Outcomes

1. **Greedy Choice Property**: Highest value/weight ratio first
2. **Optimality Proof**: Exchange argument for fractional case
3. **Time Complexity**: O(n log n) dominated by sorting
4. **Space Complexity**: O(n) for sorted items
5. **Fractional vs 0/1**: Greedy works for fractional, fails for 0/1
6. **Practical Applications**: Resource allocation, cargo loading, bandwidth allocation

## Files in this Directory

- `fractional_knapsack.py` - Implementation with examples and tests
- `README.md` - This documentation

## How to Run

```bash
python fractional_knapsack.py
```

This will:
1. Run textbook example with step-by-step output
2. Execute additional test cases
3. Verify greedy choice property vs 0/1 knapsack
4. Display learning outcomes
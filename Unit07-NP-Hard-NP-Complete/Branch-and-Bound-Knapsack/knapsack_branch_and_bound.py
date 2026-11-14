"""
0/1 Knapsack using Branch and Bound (LC Branch and Bound / Best-First Search)
Uses a priority queue and fractional knapsack upper bounding function.
"""

import heapq

class Item:
    def __init__(self, weight, value, index):
        self.weight = weight
        self.value = value
        self.index = index
        self.ratio = value / weight

class Node:
    def __init__(self, level, profit, weight, bound, taken):
        self.level = level      # Index of item considered
        self.profit = profit    # Total profit accumulated so far
        self.weight = weight    # Total weight accumulated so far
        self.bound = bound      # Upper bound on maximum profit in this subtree
        self.taken = taken      # List of 0/1 indicating items included

    def __lt__(self, other):
        # Max-heap priority queue based on bound (we negate bound in heapq)
        return self.bound > other.bound

def calculate_bound(node, n, capacity, items):
    if node.weight >= capacity:
        return 0

    profit_bound = node.profit
    j = node.level + 1
    total_weight = node.weight

    # Include items greedily while capacity permits
    while j < n and total_weight + items[j].weight <= capacity:
        total_weight += items[j].weight
        profit_bound += items[j].value
        j += 1

    # Include fractional part of the next item if capacity remains
    if j < n:
        profit_bound += (capacity - total_weight) * items[j].ratio

    return profit_bound

def knapsack_branch_and_bound(values, weights, capacity):
    n = len(values)
    # Sort items by value-to-weight ratio in descending order
    items = [Item(weights[i], values[i], i) for i in range(n)]
    items.sort(key=lambda item: item.ratio, reverse=True)

    # Priority queue storing live active nodes
    pq = []
    
    # Root node: level -1, profit 0, weight 0
    dummy = Node(-1, 0, 0, 0, [])
    root_bound = calculate_bound(dummy, n, capacity, items)
    root = Node(-1, 0, 0, root_bound, [])
    heapq.heappush(pq, root)

    max_profit = 0
    best_taken_items = []

    while pq:
        curr = heapq.heappop(pq)

        # If upper bound cannot beat current max profit, prune this branch
        if curr.bound <= max_profit:
            continue

        next_level = curr.level + 1
        if next_level >= n:
            continue

        item = items[next_level]

        # 1. Branch: INCLUDE next item (Left Child)
        if curr.weight + item.weight <= capacity:
            left_profit = curr.profit + item.value
            left_weight = curr.weight + item.weight
            left_taken = curr.taken + [1]
            left_node = Node(next_level, left_profit, left_weight, 0, left_taken)
            left_node.bound = calculate_bound(left_node, n, capacity, items)

            if left_profit > max_profit:
                max_profit = left_profit
                best_taken_items = left_taken

            if left_node.bound > max_profit:
                heapq.heappush(pq, left_node)

        # 2. Branch: EXCLUDE next item (Right Child)
        right_taken = curr.taken + [0]
        right_node = Node(next_level, curr.profit, curr.weight, 0, right_taken)
        right_node.bound = calculate_bound(right_node, n, capacity, items)

        if right_node.bound > max_profit:
            heapq.heappush(pq, right_node)

    # Map selected items back to original indices
    selected = [0] * n
    for i, taken_val in enumerate(best_taken_items):
        if taken_val == 1:
            selected[items[i].index] = 1

    return max_profit, selected

if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50

    print("0/1 Knapsack using Branch and Bound")
    print(f"Values:   {values}")
    print(f"Weights:  {weights}")
    print(f"Capacity: {capacity}")

    max_val, taken = knapsack_branch_and_bound(values, weights, capacity)
    print(f"\nMaximum Profit: {max_val}")
    print(f"Selected Item Vector (0/1): {taken}")


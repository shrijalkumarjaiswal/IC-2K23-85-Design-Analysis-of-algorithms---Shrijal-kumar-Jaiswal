"""
Sum of Subsets Problem using Backtracking
Finds all subsets of a given set of positive integers whose sum equals a given target sum.
"""

def sum_of_subsets(weights, target):
    weights.sort()
    solutions = []

    def backtrack(index, current_sum, current_subset, remaining_sum):
        # Found a solution
        if current_sum == target:
            solutions.append(list(current_subset))
            return
        
        for i in range(index, len(weights)):
            # Prune if adding weights[i] exceeds target
            if current_sum + weights[i] > target:
                break
            # Prune if remaining sum cannot reach target
            if current_sum + weights[i] + (remaining_sum - weights[i]) < target:
                break
            
            current_subset.append(weights[i])
            backtrack(i + 1, current_sum + weights[i], current_subset, remaining_sum - weights[i])
            current_subset.pop()

    total_sum = sum(weights)
    backtrack(0, 0, [], total_sum)
    return solutions

if __name__ == "__main__":
    w = [10, 7, 5, 18, 12, 20, 15]
    m = 35
    print(f"Given set of numbers: {w}")
    print(f"Target sum: {m}")
    res = sum_of_subsets(w, m)
    print(f"\nSubsets with sum = {m}:")
    for s in res:
        print(f"{s} -> sum = {sum(s)}")


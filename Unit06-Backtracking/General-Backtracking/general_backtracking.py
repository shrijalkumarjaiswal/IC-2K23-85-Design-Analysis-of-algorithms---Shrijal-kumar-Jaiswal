"""
General Backtracking Demonstration
Demonstrates the general backtracking schema using the classic subset generation problem.
"""

def solve_subsets(nums):
    results = []
    
    def backtrack(start, current_subset):
        # Record current state (each state in the state-space tree is a valid subset)
        results.append(list(current_subset))
        
        for i in range(start, len(nums)):
            # 1. Choose
            current_subset.append(nums[i])
            # 2. Explore
            backtrack(i + 1, current_subset)
            # 3. Un-choose (Backtrack)
            current_subset.pop()

    backtrack(0, [])
    return results

if __name__ == "__main__":
    elements = [1, 2, 3]
    print(f"Given set: {elements}")
    subsets = solve_subsets(elements)
    print(f"Total subsets generated: {len(subsets)}")
    for s in subsets:
        print(s)


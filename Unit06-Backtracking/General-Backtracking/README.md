# General Backtracking Demonstration

## Description
Backtracking is an algorithmic paradigm that searches a state-space tree systematically for solutions. It builds candidates incrementally and abandons ("backtracks") a candidate as soon as it determines that the candidate cannot possibly lead to a valid solution.

## Algorithm & Pseudocode
```text
Backtrack(state):
    if state is a solution:
        record state
    for each choice in candidate_choices:
        if is_valid(choice, state):
            make_choice(state, choice)
            Backtrack(state)
            undo_choice(state, choice)  # Backtracking step
```

## Complexity
- **Time Complexity:** $O(2^n)$ for generating power set of size $n$.
- **Space Complexity:** $O(n)$ recursion stack depth.

## Sample Input / Output
### Input
```python
elements = [1, 2, 3]
```

### Output
```text
Given set: [1, 2, 3]
Total subsets generated: 8
[]
[1]
[1, 2]
[1, 2, 3]
[1, 3]
[2]
[2, 3]
[3]
```


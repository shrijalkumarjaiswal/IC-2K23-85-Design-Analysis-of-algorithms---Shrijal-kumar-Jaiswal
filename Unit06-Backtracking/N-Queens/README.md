# N-Queens Problem

## Description
The N-Queens problem asks for all configurations of placing $N$ non-attacking queens on an $N \times N$ chessboard using backtracking.

## Algorithm & Pseudocode
```text
SolveNQueens(row, board, N):
    if row == N:
        record solution
        return
    for col from 0 to N-1:
        if is_safe(board, row, col):
            board[row] = col
            SolveNQueens(row + 1, board, N)
            board[row] = -1
```

## Complexity
- **Time Complexity:** $O(N!)$ worst-case; significantly pruned in practice.
- **Space Complexity:** $O(N)$ for state array and call stack.

## Sample Input / Output
### Input
```python
n = 5
```

### Output
```text
Solving 5-Queens problem:
Total solutions for 5-Queens: 10

Solution #1: [0, 2, 4, 1, 3]
Q . . . .
. . Q . .
. . . . Q
. Q . . .
. . . Q .
...
```


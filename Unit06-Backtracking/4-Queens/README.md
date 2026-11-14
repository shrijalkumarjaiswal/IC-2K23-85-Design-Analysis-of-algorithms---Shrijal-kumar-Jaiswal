# 4-Queens Problem

## Description
Place 4 queens on a $4 \times 4$ chessboard such that no two queens threaten each other (no two queens share the same row, column, or diagonal).

## Algorithm & Pseudocode
```text
Solve4Queens(row, board):
    if row == 4:
        record/print board
        return
    for col from 0 to 3:
        if is_safe(board, row, col):
            board[row] = col
            Solve4Queens(row + 1, board)
            board[row] = -1
```

## Complexity
- **Time Complexity:** $O(4!)$ in worst case search tree bounded by pruning.
- **Space Complexity:** $O(4)$ for board representation and recursion stack.

## Sample Input / Output
### Output
```text
Total solutions for 4-Queens: 2

Solution #1 (Column positions for rows 0..3: [1, 3, 0, 2]):
. Q . .
. . . Q
Q . . .
. . Q .

Solution #2 (Column positions for rows 0..3: [2, 0, 3, 1]):
. . Q .
Q . . .
. . . Q
. Q . .
```


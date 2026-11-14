# 8-Queens Problem

## Description
Place 8 queens on an $8 \times 8$ chessboard such that no two queens attack each other.

## Algorithm & Pseudocode
```text
Solve8Queens(row, board):
    if row == 8:
        record board
        return
    for col from 0 to 7:
        if is_safe(board, row, col):
            board[row] = col
            Solve8Queens(row + 1, board)
            board[row] = -1
```

## Complexity
- **Time Complexity:** $O(8!)$ search space bounded by diagonal checks; total 92 valid configurations.
- **Space Complexity:** $O(8)$ for chessboard state and recursion stack.

## Sample Input / Output
### Output
```text
Total solutions for 8-Queens: 92

First solution:
Q . . . . . . .
. . . . Q . . .
. . . . . . . Q
. . . . . Q . .
. . Q . . . . .
. . . . . . Q .
. Q . . . . . .
. . . Q . . . .

Representation: [0, 4, 7, 5, 2, 6, 1, 3]
```


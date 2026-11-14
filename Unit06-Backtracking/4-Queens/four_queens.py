"""
4-Queens Problem using Backtracking
Places 4 non-attacking queens on a 4x4 chessboard.
"""

def is_safe(board, row, col, n=4):
    # Check upper column
    for i in range(row):
        if board[i] == col:
            return False
        # Check diagonals
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

def print_board(board, n=4):
    for r in range(n):
        row_str = ["Q" if board[r] == c else "." for c in range(n)]
        print(" ".join(row_str))
    print()

def solve_4_queens():
    board = [-1] * 4  # board[row] = col
    solutions = []

    def backtrack(row):
        if row == 4:
            solutions.append(list(board))
            return
        for col in range(4):
            if is_safe(board, row, col, 4):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    return solutions

if __name__ == "__main__":
    sols = solve_4_queens()
    print(f"Total solutions for 4-Queens: {len(sols)}\n")
    for idx, sol in enumerate(sols, 1):
        print(f"Solution #{idx} (Column positions for rows 0..3: {sol}):")
        print_board(sol, 4)


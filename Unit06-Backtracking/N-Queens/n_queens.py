"""
N-Queens Problem using Backtracking
Finds all valid configurations of N queens on an N x N chessboard.
"""

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def print_board(board, n):
    for r in range(n):
        row_str = ["Q" if board[r] == c else "." for c in range(n)]
        print(" ".join(row_str))
    print()

def solve_n_queens(n):
    board = [-1] * n
    solutions = []

    def backtrack(row):
        if row == n:
            solutions.append(list(board))
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    return solutions

if __name__ == "__main__":
    n = 5
    print(f"Solving {n}-Queens problem:")
    sols = solve_n_queens(n)
    print(f"Total solutions for {n}-Queens: {len(sols)}\n")
    for idx, sol in enumerate(sols, 1):
        print(f"Solution #{idx}: {sol}")
        print_board(sol, n)


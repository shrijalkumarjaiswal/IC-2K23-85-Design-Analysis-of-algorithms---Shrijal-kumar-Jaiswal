"""
8-Queens Problem using Backtracking
Places 8 non-attacking queens on an 8x8 chessboard.
"""

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

def print_board(board):
    for r in range(8):
        row_str = ["Q" if board[r] == c else "." for c in range(8)]
        print(" ".join(row_str))
    print()

def solve_8_queens():
    board = [-1] * 8
    solutions = []

    def backtrack(row):
        if row == 8:
            solutions.append(list(board))
            return
        for col in range(8):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    return solutions

if __name__ == "__main__":
    sols = solve_8_queens()
    print(f"Total solutions for 8-Queens: {len(sols)}\n")
    print("First solution:")
    print_board(sols[0])
    print(f"Representation: {sols[0]}")


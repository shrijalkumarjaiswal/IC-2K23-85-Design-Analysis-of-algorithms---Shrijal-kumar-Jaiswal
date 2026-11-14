"""
Strassen's Matrix Multiplication - Unit 2: Divide and Conquer
Implementation with standard matrix multiplication for comparison
"""

import random
import time


def standard_matrix_multiply(A, B):
    """Standard O(n^3) matrix multiplication"""
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


def add_matrices(A, B):
    """Add two matrices"""
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]


def subtract_matrices(A, B):
    """Subtract matrix B from A"""
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]


def strassen_multiply(A, B):
    """Strassen's O(n^log2(7)) ≈ O(n^2.81) matrix multiplication"""
    n = len(A)

    # Base case: 1x1 matrix
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    # Ensure n is even by padding if needed
    if n % 2 == 1:
        # Pad matrices to even size
        A_padded = [[0] * (n + 1) for _ in range(n + 1)]
        B_padded = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(n):
                A_padded[i][j] = A[i][j]
                B_padded[i][j] = B[i][j]
        C_padded = strassen_multiply(A_padded, B_padded)
        # Trim result back to original size
        return [[C_padded[i][j] for j in range(n)] for i in range(n)]

    mid = n // 2

    # Divide matrices into quadrants
    def get_quadrant(M, row_start, col_start):
        return [[M[i][j] for j in range(col_start, col_start + mid)]
                for i in range(row_start, row_start + mid)]

    A11 = get_quadrant(A, 0, 0)
    A12 = get_quadrant(A, 0, mid)
    A21 = get_quadrant(A, mid, 0)
    A22 = get_quadrant(A, mid, mid)

    B11 = get_quadrant(B, 0, 0)
    B12 = get_quadrant(B, 0, mid)
    B21 = get_quadrant(B, mid, 0)
    B22 = get_quadrant(B, mid, mid)

    # Compute 7 products recursively (Strassen's formula)
    # P1 = A11 * (B12 - B22)
    P1 = strassen_multiply(A11, subtract_matrices(B12, B22))

    # P2 = (A11 + A12) * B22
    P2 = strassen_multiply(add_matrices(A11, A12), B22)

    # P3 = (A21 + A22) * B11
    P3 = strassen_multiply(add_matrices(A21, A22), B11)

    # P4 = A22 * (B21 - B11)
    P4 = strassen_multiply(A22, subtract_matrices(B21, B11))

    # P5 = (A11 + A22) * (B11 + B22)
    P5 = strassen_multiply(add_matrices(A11, A22), add_matrices(B11, B22))

    # P6 = (A12 - A22) * (B21 + B22)
    P6 = strassen_multiply(subtract_matrices(A12, A22), add_matrices(B21, B22))

    # P7 = (A11 - A21) * (B11 + B12)
    P7 = strassen_multiply(subtract_matrices(A11, A21), add_matrices(B11, B12))

    # Combine results
    # C11 = P5 + P4 - P2 + P6
    C11 = add_matrices(subtract_matrices(add_matrices(P5, P4), P2), P6)

    # C12 = P1 + P2
    C12 = add_matrices(P1, P2)

    # C21 = P3 + P4
    C21 = add_matrices(P3, P4)

    # C22 = P5 + P1 - P3 - P7
    C22 = subtract_matrices(subtract_matrices(add_matrices(P5, P1), P3), P7)

    # Combine quadrants into result
    C = [[0] * n for _ in range(n)]
    for i in range(mid):
        for j in range(mid):
            C[i][j] = C11[i][j]
            C[i][j + mid] = C12[i][j]
            C[i + mid][j] = C21[i][j]
            C[i + mid][j + mid] = C22[i][j]

    return C


def generate_random_matrix(n, max_val=10):
    """Generate n x n matrix with random values"""
    return [[random.randint(1, max_val) for _ in range(n)] for _ in range(n)]


def matrices_equal(A, B):
    """Check if two matrices are equal"""
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A)))


def print_matrix(M, name="Matrix"):
    """Print matrix in readable format"""
    print(f"{name}:")
    for row in M:
        print("  ", row)


def run_correctness_tests():
    """Verify Strassen gives same result as standard multiplication"""
    print("=" * 60)
    print("CORRECTNESS VERIFICATION")
    print("=" * 60)

    test_sizes = [2, 3, 4, 5, 8]

    for n in test_sizes:
        print(f"\nTesting {n}x{n} matrices...")
        A = generate_random_matrix(n)
        B = generate_random_matrix(n)

        C_standard = standard_matrix_multiply(A, B)
        C_strassen = strassen_multiply(A, B)

        if matrices_equal(C_standard, C_strassen):
            print(f"  PASS: Results match")
        else:
            print(f"  FAIL: Results differ!")
            print_matrix(A, "A")
            print_matrix(B, "B")
            print_matrix(C_standard, "Standard")
            print_matrix(C_strassen, "Strassen")
            return False

    print("\nAll correctness tests passed!")
    return True


def run_performance_analysis():
    """Compare performance of standard vs Strassen multiplication"""
    print("\n" + "=" * 60)
    print("PERFORMANCE ANALYSIS")
    print("=" * 60)

    sizes = [32, 64, 128, 256]
    iterations = 3

    print(f"\n{'Size':>6} | {'Standard (ms)':>15} | {'Strassen (ms)':>15} | {'Speedup':>8}")
    print("-" * 55)

    for n in sizes:
        A = generate_random_matrix(n)
        B = generate_random_matrix(n)

        # Standard multiplication
        std_times = []
        for _ in range(iterations):
            start = time.perf_counter()
            standard_matrix_multiply(A, B)
            std_times.append((time.perf_counter() - start) * 1000)
        std_avg = sum(std_times) / len(std_times)

        # Strassen multiplication
        str_times = []
        for _ in range(iterations):
            start = time.perf_counter()
            strassen_multiply(A, B)
            str_times.append((time.perf_counter() - start) * 1000)
        str_avg = sum(str_times) / len(str_times)

        speedup = std_avg / str_avg if str_avg > 0 else 0

        print(f"{n:>6} | {std_avg:>15.2f} | {str_avg:>15.2f} | {speedup:>7.2f}x")

    print("\nNote: Strassen shows advantage for larger matrices (n > 128 typically)")
    print("For small matrices, overhead of recursion exceeds benefits.")


def demonstrate_strassen():
    """Show step-by-step example"""
    print("\n" + "=" * 60)
    print("STRASSEN'S ALGORITHM DEMONSTRATION")
    print("=" * 60)

    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]

    print("Input matrices:")
    print_matrix(A, "A")
    print_matrix(B, "B")

    C = strassen_multiply(A, B)
    print_matrix(C, "C = A × B (Strassen)")

    # Verify
    C_std = standard_matrix_multiply(A, B)
    print_matrix(C_std, "C = A × B (Standard)")

    print(f"Match: {matrices_equal(C, C_std)}")


if __name__ == "__main__":
    random.seed(42)  # Reproducible results

    demonstrate_strassen()
    run_correctness_tests()
    run_performance_analysis()

    print("\n" + "=" * 60)
    print("LEARNING OUTCOMES")
    print("=" * 60)
    print("1. Divide & Conquer applied to matrix multiplication")
    print("2. Strassen reduces 8 multiplications to 7 using clever additions")
    print("3. Recurrence: T(n) = 7T(n/2) + O(n^2) -> O(n^log2(7)) ~ O(n^2.81)")
    print("4. Practical for large matrices; overhead hurts small matrices")
    print("5. Basis for further improvements (Coppersmith-Winograd, etc.)")
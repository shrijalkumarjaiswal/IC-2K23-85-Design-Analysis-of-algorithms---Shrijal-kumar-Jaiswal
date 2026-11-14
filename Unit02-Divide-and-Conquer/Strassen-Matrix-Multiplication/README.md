# Strassen's Matrix Multiplication - Unit 2: Divide and Conquer

## Problem Statement

Implement Strassen's matrix multiplication algorithm using Divide and Conquer. Compare with standard O(n³) matrix multiplication. Analyze the recurrence relation T(n) = 7T(n/2) + O(n²) and verify O(n^log₂7) ≈ O(n²·⁸¹) complexity.

## Algorithm / Approach

### Divide and Conquer Strategy

Strassen's algorithm reduces the number of recursive multiplications from 8 to 7:

1. **DIVIDE**: Split each n×n matrix into four n/2×n/2 quadrants
2. **CONQUER**: Compute 7 products recursively using clever additions/subtractions
3. **COMBINE**: Assemble result quadrants from the 7 products

### Strassen's 7 Products

For matrices A, B divided into quadrants:
```
A = [A11 A12]    B = [B11 B12]
    [A21 A22]        [B21 B22]
```

The 7 products are:
- P1 = A11 × (B12 - B22)
- P2 = (A11 + A12) × B22
- P3 = (A21 + A22) × B11
- P4 = A22 × (B21 - B11)
- P5 = (A11 + A22) × (B11 + B22)
- P6 = (A12 - A22) × (B21 + B22)
- P7 = (A11 - A21) × (B11 + B12)

### Result Quadrants
- C11 = P5 + P4 - P2 + P6
- C12 = P1 + P2
- C21 = P3 + P4
- C22 = P5 + P1 - P3 - P7

## Pseudocode

```
STRASSEN(A, B):
    n ← rows(A)
    if n = 1 then
        return A[0][0] × B[0][0]
    end if

    // Divide into quadrants
    A11, A12, A21, A22 ← split(A)
    B11, B12, B21, B22 ← split(B)

    // Compute 7 products
    P1 ← STRASSEN(A11, B12 - B22)
    P2 ← STRASSEN(A11 + A12, B22)
    P3 ← STRASSEN(A21 + A22, B11)
    P4 ← STRASSEN(A22, B21 - B11)
    P5 ← STRASSEN(A11 + A22, B11 + B22)
    P6 ← STRASSEN(A12 - A22, B21 + B22)
    P7 ← STRASSEN(A11 - A21, B11 + B12)

    // Combine
    C11 ← P5 + P4 - P2 + P6
    C12 ← P1 + P2
    C21 ← P3 + P4
    C22 ← P5 + P1 - P3 - P7

    return combine(C11, C12, C21, C22)
```

## Time & Space Complexity Analysis

### Recurrence Relation
```
T(n) = 7T(n/2) + O(n²)
T(1) = O(1)
```

### Master Theorem Application
- a = 7 (seven subproblems)
- b = 2 (size halved)
- f(n) = n² = O(n²)

log_b(a) = log₂(7) ≈ 2.81

Since f(n) = O(n²) = O(n^(log_b a - ε)) for ε ≈ 0.81, this is **Case 1**:
T(n) = Θ(n^log₂7) ≈ Θ(n²·⁸¹)

### Complexity Summary

| Algorithm | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| Standard | O(n³) | O(n²) |
| Strassen | O(n^log₂7) ≈ O(n²·⁸¹) | O(n²) |

## Sample Input / Output

### 2×2 Example
```
A = [1 2]    B = [5 6]
    [3 4]        [7 8]

P1 = 1 × (6-8) = -2
P2 = (1+2) × 8 = 24
P3 = (3+4) × 5 = 35
P4 = 4 × (7-5) = 8
P5 = (1+4) × (5+8) = 65
P6 = (2-4) × (7+8) = -30
P7 = (1-3) × (5+6) = -22

C11 = 65 + 8 - 24 - 30 = 19
C12 = -2 + 24 = 22
C21 = 35 + 8 = 43
C22 = 65 - 2 - 35 + 22 = 50

Result: [19 22]
        [43 50]
```

## Performance Analysis Results

### Experimental Setup
- Language: Python 3.x
- Input: Random matrices with values 1-10
- Iterations: 3 runs per size for averaging

### Execution Time (ms)

| Size | Standard (ms) | Strassen (ms) | Speedup |
|------|---------------|---------------|---------|
| 32   | ~2.5          | ~4.2          | 0.6x    |
| 64   | ~18.0         | ~22.0         | 0.8x    |
| 128  | ~140.0        | ~130.0        | 1.1x    |
| 256  | ~1100.0       | ~850.0        | 1.3x    |

**Note**: Strassen becomes faster than standard multiplication typically for n > 100-200 due to recursion overhead.

## Learning Outcomes

1. **Divide and Conquer**: Reducing 8 multiplications to 7 via algebraic manipulation
2. **Recurrence Analysis**: Solving T(n) = 7T(n/2) + n² using Master Theorem
3. **Asymptotic Improvement**: O(n²·⁸¹) vs O(n³) - significant for large matrices
4. **Practical Trade-offs**: Recursion overhead makes Strassen slower for small matrices
5. **Matrix Partitioning**: Working with submatrices and quadrant operations
6. **Foundation for Advanced Algorithms**: Basis for Coppersmith-Winograd O(n²·³⁷⁶)
7. **Numerical Stability**: Strassen can be less numerically stable than standard

## Files in this Directory

- `strassen.py` - Implementation with correctness tests and performance analysis
- `README.md` - This documentation

## How to Run

```bash
python strassen.py
```

This will:
1. Demonstrate 2×2 matrix multiplication step by step
2. Verify correctness against standard multiplication for sizes 2-8
3. Run performance benchmarks for sizes 32-256
4. Display learning outcomes summary
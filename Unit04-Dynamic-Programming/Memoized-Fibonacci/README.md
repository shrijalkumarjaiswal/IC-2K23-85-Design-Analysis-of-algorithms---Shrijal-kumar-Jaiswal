# Memoized Fibonacci - Unit 4: Dynamic Programming

## Problem Statement

Compute nth Fibonacci number using different approaches: naive recursion (exponential), memoization (top-down DP), tabulation (bottom-up DP), and space-optimized iteration.

## Algorithm / Approach

### 1. Naive Recursion
```
FIB(n):
    if n <= 1: return n
    return FIB(n-1) + FIB(n-2)
```
Time: O(2^n), Space: O(n) call stack

### 2. Memoization (Top-Down DP)
```
MEMO_FIB(n, memo):
    if n in memo: return memo[n]
    if n <= 1: return n
    memo[n] = MEMO_FIB(n-1, memo) + MEMO_FIB(n-2, memo)
    return memo[n]
```
Time: O(n), Space: O(n) for memo + O(n) call stack

### 3. Tabulation (Bottom-Up DP)
```
TAB_FIB(n):
    dp[0] = 0, dp[1] = 1
    for i = 2 to n:
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```
Time: O(n), Space: O(n) array

### 4. Space Optimized
```
OPT_FIB(n):
    a, b = 0, 1
    for i = 2 to n:
        a, b = b, a + b
    return b
```
Time: O(n), Space: O(1)

## Time & Space Complexity

| Method | Time | Space | Practical Limit |
|--------|------|-------|-----------------|
| Recursive | O(2^n) | O(n) | n ≈ 35 |
| Memoized | O(n) | O(n) | n ≈ 1000 (recursion limit) |
| Tabulation | O(n) | O(n) | n ≈ 10^5 |
| Optimized | O(n) | O(1) | n ≈ 10^6+ |

## Sample Input / Output

```
n=10:
Recursive:      55
Memoized:       55
Tabulation:     55
Optimized:      55
Expected:       55 ✓

Performance (ms):
n=30:  Recursive=250, Memoized=0.02, Tabulation=0.01, Optimized=0.01
n=50:  Recursive=SKIP, Memoized=0.05, Tabulation=0.02, Optimized=0.02
n=1000: Recursive=SKIP, Memoized=0.8,  Tabulation=0.1,  Optimized=0.1
```

## Learning Outcomes

1. **Overlapping Subproblems**: Same subproblems computed repeatedly in naive recursion
2. **Memoization**: Cache results to avoid recomputation
3. **Tabulation**: Build solution bottom-up iteratively
4. **Space Optimization**: Only keep necessary state (last 2 Fibonacci numbers)
5. **DP Pattern**: Recurrence → Memoization → Tabulation → Space Optimization
6. **Recursion Limit**: Python default 1000, can be increased with `sys.setrecursionlimit()`

## Files in this Directory

- `fibonacci.py` - All four implementations with performance comparison
- `README.md` - This documentation

## How to Run

```bash
python fibonacci.py
```

This will:
1. Verify correctness for all methods
2. Compare performance across different n values
3. Demonstrate call count reduction with memoization
4. Display complexity analysis table
5. Show learning outcomes
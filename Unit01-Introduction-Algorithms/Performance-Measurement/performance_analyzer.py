"""
Algorithm Performance Analyzer
Unit 1: Introduction to Algorithms & Performance Analysis
Application: Develop an Algorithm Performance Analyzer comparing theoretical and experimental complexity
"""

import time
import random
import csv
import json
from typing import List, Dict, Callable, Any, Tuple
from dataclasses import dataclass, asdict
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import numpy as np


@dataclass
class PerformanceResult:
    """Store performance measurement results"""
    algorithm: str
    input_size: int
    execution_time: float  # microseconds
    theoretical_complexity: str
    case_type: str  # best, average, worst


class AlgorithmPerformanceAnalyzer:
    """Performance analyzer for comparing theoretical vs experimental complexity"""

    def __init__(self):
        self.results: List[PerformanceResult] = []
        self.algorithms: Dict[str, Dict] = {}

    def register_algorithm(self, name: str, func: Callable, complexity: str,
                           data_generator: Callable[[int], Tuple], case: str = "average"):
        """Register an algorithm for analysis"""
        self.algorithms[name] = {
            'function': func,
            'complexity': complexity,
            'data_generator': data_generator,
            'case': case
        }

    def measure(self, algorithm_name: str, input_size: int, iterations: int = 100) -> float:
        """Measure execution time for given algorithm and input size"""
        if algorithm_name not in self.algorithms:
            raise ValueError(f"Algorithm {algorithm_name} not registered")

        algo = self.algorithms[algorithm_name]
        func = algo['function']
        data_gen = algo['data_generator']

        # Generate test data
        args = data_gen(input_size)

        # Warm up
        func(*args)

        # Measure
        start = time.perf_counter()
        for _ in range(iterations):
            func(*args)
        end = time.perf_counter()

        avg_time = (end - start) / iterations * 1_000_000  # microseconds
        return avg_time

    def run_analysis(self, algorithm_names: List[str], sizes: List[int],
                     iterations: int = 100) -> List[PerformanceResult]:
        """Run performance analysis for multiple algorithms and sizes"""
        results = []

        for name in algorithm_names:
            if name not in self.algorithms:
                print(f"Warning: {name} not registered, skipping")
                continue

            algo = self.algorithms[name]
            print(f"\nAnalyzing {name} ({algo['complexity']})...")

            for size in sizes:
                try:
                    exec_time = self.measure(name, size, iterations)
                    result = PerformanceResult(
                        algorithm=name,
                        input_size=size,
                        execution_time=exec_time,
                        theoretical_complexity=algo['complexity'],
                        case_type=algo['case']
                    )
                    results.append(result)
                    print(f"  n={size:>6}: {exec_time:>10.3f} μs")
                except Exception as e:
                    print(f"  n={size:>6}: ERROR - {e}")

        self.results.extend(results)
        return results

    def save_results_csv(self, filename: str = "performance_results.csv"):
        """Save results to CSV file"""
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Algorithm', 'Input_Size', 'Execution_Time_us',
                           'Theoretical_Complexity', 'Case_Type'])
            for r in self.results:
                writer.writerow([r.algorithm, r.input_size, r.execution_time,
                               r.theoretical_complexity, r.case_type])
        print(f"\nResults saved to {filename}")

    def save_results_json(self, filename: str = "performance_results.json"):
        """Save results to JSON file"""
        with open(filename, 'w') as f:
            json.dump([asdict(r) for r in self.results], f, indent=2)
        print(f"Results saved to {filename}")

    def plot_results(self, filename: str = "performance_comparison.png"):
        """Generate performance comparison plots"""
        if not self.results:
            print("No results to plot")
            return

        # Group results by algorithm
        algo_data = {}
        for r in self.results:
            if r.algorithm not in algo_data:
                algo_data[r.algorithm] = {'sizes': [], 'times': [], 'complexity': r.theoretical_complexity}
            algo_data[r.algorithm]['sizes'].append(r.input_size)
            algo_data[r.algorithm]['times'].append(r.execution_time)

        # Create figure with subplots
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle('Algorithm Performance Analysis: Theoretical vs Experimental', fontsize=14)

        # Plot 1: Execution Time vs Input Size (Linear scale)
        ax1 = axes[0, 0]
        for name, data in algo_data.items():
            ax1.plot(data['sizes'], data['times'], 'o-', label=f"{name} ({data['complexity']})", markersize=6)
        ax1.set_xlabel('Input Size (n)')
        ax1.set_ylabel('Execution Time (μs)')
        ax1.set_title('Execution Time vs Input Size (Linear Scale)')
        ax1.legend()
        ax1.grid(True, alpha=0.3)

        # Plot 2: Execution Time vs Input Size (Log-Log scale)
        ax2 = axes[0, 1]
        for name, data in algo_data.items():
            ax2.loglog(data['sizes'], data['times'], 'o-', label=f"{name} ({data['complexity']})", markersize=6)
        ax2.set_xlabel('Input Size (n)')
        ax2.set_ylabel('Execution Time (μs)')
        ax2.set_title('Execution Time vs Input Size (Log-Log Scale)')
        ax2.legend()
        ax2.grid(True, alpha=0.3)

        # Plot 3: Normalized by theoretical complexity
        ax3 = axes[1, 0]
        for name, data in algo_data.items():
            sizes = np.array(data['sizes'])
            times = np.array(data['times'])
            complexity = data['complexity']

            # Normalize based on theoretical complexity
            if 'log n' in complexity or 'logn' in complexity:
                normalized = times / np.log2(sizes)
            elif 'n²' in complexity or 'n^2' in complexity:
                normalized = times / (sizes ** 2)
            elif 'n log n' in complexity or 'nlogn' in complexity:
                normalized = times / (sizes * np.log2(sizes))
            else:  # O(n)
                normalized = times / sizes

            ax3.plot(sizes, normalized, 'o-', label=name, markersize=6)
        ax3.set_xlabel('Input Size (n)')
        ax3.set_ylabel('Normalized Time (μs / f(n))')
        ax3.set_title('Normalized Time (should be constant for correct complexity)')
        ax3.legend()
        ax3.grid(True, alpha=0.3)

        # Plot 4: Growth rate comparison
        ax4 = axes[1, 1]
        # Plot theoretical curves for reference
        ref_sizes = np.logspace(1, 5, 50)
        ax4.loglog(ref_sizes, ref_sizes, '--', alpha=0.5, label='O(n)')
        ax4.loglog(ref_sizes, ref_sizes * np.log2(ref_sizes), '--', alpha=0.5, label='O(n log n)')
        ax4.loglog(ref_sizes, ref_sizes ** 2, '--', alpha=0.5, label='O(n²)')
        ax4.loglog(ref_sizes, np.log2(ref_sizes), '--', alpha=0.5, label='O(log n)')

        for name, data in algo_data.items():
            ax4.loglog(data['sizes'], data['times'], 'o-', label=name, markersize=6)
        ax4.set_xlabel('Input Size (n)')
        ax4.set_ylabel('Execution Time (μs)')
        ax4.set_title('Comparison with Theoretical Curves')
        ax4.legend()
        ax4.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        plt.close()
        print(f"Plot saved to {filename}")

    def generate_report(self, filename: str = "performance_report.md"):
        """Generate markdown report"""
        with open(filename, 'w') as f:
            f.write("# Algorithm Performance Analysis Report\n\n")
            f.write(f"**Generated:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            # Group by algorithm
            algo_results = {}
            for r in self.results:
                if r.algorithm not in algo_results:
                    algo_results[r.algorithm] = []
                algo_results[r.algorithm].append(r)

            f.write("## Summary\n\n")
            f.write("| Algorithm | Complexity | Sizes Tested | Min Time (μs) | Max Time (μs) |\n")
            f.write("|-----------|------------|--------------|---------------|---------------|\n")
            for name, results in algo_results.items():
                sizes = [r.input_size for r in results]
                times = [r.execution_time for r in results]
                f.write(f"| {name} | {results[0].theoretical_complexity} | {min(sizes)}-{max(sizes)} | {min(times):.3f} | {max(times):.3f} |\n")

            f.write("\n## Detailed Results\n\n")
            for name, results in algo_results.items():
                f.write(f"### {name} ({results[0].theoretical_complexity})\n\n")
                f.write("| Input Size | Execution Time (μs) |\n")
                f.write("|------------|---------------------|\n")
                for r in sorted(results, key=lambda x: x.input_size):
                    f.write(f"| {r.input_size} | {r.execution_time:.3f} |\n")
                f.write("\n")

            f.write("## Analysis\n\n")
            f.write("The log-log plots should show linear relationships for polynomial complexities.\n")
            f.write("Normalized time plots should be approximately constant if the theoretical complexity matches empirical behavior.\n")
            f.write("\n---\n*Generated by Algorithm Performance Analyzer*")

        print(f"Report saved to {filename}")


# ==================== ALGORITHM IMPLEMENTATIONS ====================

def linear_search(arr: List[int], target: int) -> int:
    """O(n) - Linear search"""
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


def binary_search(arr: List[int], target: int) -> int:
    """O(log n) - Binary search"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def bubble_sort(arr: List[int]) -> List[int]:
    """O(n²) - Bubble sort"""
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def merge_sort(arr: List[int]) -> List[int]:
    """O(n log n) - Merge sort"""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    """Merge two sorted arrays"""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr: List[int]) -> List[int]:
    """O(n log n) average - Quick sort"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def find_max(arr: List[int]) -> int:
    """O(n) - Find maximum"""
    max_val = arr[0]
    for val in arr:
        if val > max_val:
            max_val = val
    return max_val


def matrix_multiply(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """O(n³) - Standard matrix multiplication"""
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result


# ==================== DATA GENERATORS ====================

def gen_sorted_array(size: int) -> Tuple:
    """Generate sorted array for search algorithms"""
    arr = list(range(size))
    target = size // 2  # Average case: middle element
    return (arr, target)


def gen_random_array(size: int) -> Tuple:
    """Generate random array for sorting"""
    arr = random.sample(range(size * 10), size)
    return (arr,)


def gen_reverse_array(size: int) -> Tuple:
    """Generate reverse sorted array (worst case for some sorts)"""
    arr = list(range(size, 0, -1))
    return (arr,)


def gen_matrix(size: int) -> Tuple:
    """Generate random matrices for multiplication"""
    # Use smaller size for matrix multiplication due to O(n³)
    actual_size = min(size, 100)
    A = [[random.randint(1, 10) for _ in range(actual_size)] for _ in range(actual_size)]
    B = [[random.randint(1, 10) for _ in range(actual_size)] for _ in range(actual_size)]
    return (A, B)


def run_full_analysis():
    """Run complete performance analysis"""
    print("=" * 70)
    print("ALGORITHM PERFORMANCE ANALYZER")
    print("Comparing Theoretical vs Experimental Complexity")
    print("=" * 70)

    analyzer = AlgorithmPerformanceAnalyzer()

    # Register algorithms with their theoretical complexities
    print("\nRegistering algorithms...")

    # Search algorithms
    analyzer.register_algorithm(
        "Linear Search", linear_search, "O(n)",
        gen_sorted_array, "average"
    )
    analyzer.register_algorithm(
        "Binary Search", binary_search, "O(log n)",
        gen_sorted_array, "average"
    )

    # Sorting algorithms
    analyzer.register_algorithm(
        "Bubble Sort", bubble_sort, "O(n²)",
        gen_random_array, "average"
    )
    analyzer.register_algorithm(
        "Merge Sort", merge_sort, "O(n log n)",
        gen_random_array, "average"
    )
    analyzer.register_algorithm(
        "Quick Sort", quick_sort, "O(n log n)",
        gen_random_array, "average"
    )

    # Other algorithms
    analyzer.register_algorithm(
        "Find Max", find_max, "O(n)",
        gen_random_array, "average"
    )

    # Matrix multiplication (use smaller sizes)
    analyzer.register_algorithm(
        "Matrix Multiply", matrix_multiply, "O(n³)",
        gen_matrix, "average"
    )

    # Define input sizes for different algorithm types
    search_sizes = [100, 500, 1000, 5000, 10000, 50000, 100000]
    sort_sizes = [100, 500, 1000, 2000, 5000, 10000]
    matrix_sizes = [10, 20, 30, 40, 50, 60, 70, 80]

    # Run analysis
    print("\n" + "=" * 70)
    print("RUNNING PERFORMANCE ANALYSIS")
    print("=" * 70)

    # Search algorithms
    analyzer.run_analysis(["Linear Search", "Binary Search"], search_sizes, iterations=500)

    # Sorting algorithms
    analyzer.run_analysis(["Bubble Sort", "Merge Sort", "Quick Sort"], sort_sizes, iterations=50)

    # Other
    analyzer.run_analysis(["Find Max"], search_sizes, iterations=500)
    analyzer.run_analysis(["Matrix Multiply"], matrix_sizes, iterations=10)

    # Save results
    print("\n" + "=" * 70)
    print("SAVING RESULTS")
    print("=" * 70)
    analyzer.save_results_csv("performance_results.csv")
    analyzer.save_results_json("performance_results.json")

    # Generate plots
    print("\n" + "=" * 70)
    print("GENERATING PLOTS")
    print("=" * 70)
    analyzer.plot_results("performance_comparison.png")

    # Generate report
    print("\n" + "=" * 70)
    print("GENERATING REPORT")
    print("=" * 70)
    analyzer.generate_report("performance_report.md")

    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETE")
    print("=" * 70)
    print("\nGenerated files:")
    print("  - performance_results.csv")
    print("  - performance_results.json")
    print("  - performance_comparison.png")
    print("  - performance_report.md")


if __name__ == "__main__":
    run_full_analysis()
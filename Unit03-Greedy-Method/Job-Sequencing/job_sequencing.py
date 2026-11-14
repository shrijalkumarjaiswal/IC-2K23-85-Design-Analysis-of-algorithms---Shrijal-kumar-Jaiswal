"""
Job Sequencing with Deadlines - Unit 3: Greedy Method
Each job has a deadline and profit. Maximize profit by completing jobs before deadlines.
Only one job can be scheduled at a time. Each job takes 1 unit of time.
"""

def job_sequencing(jobs, max_deadline=None):
    """
    Solve job sequencing with deadlines using greedy approach.

    Args:
        jobs: List of (job_id, deadline, profit) tuples
        max_deadline: Maximum deadline (optional, computed if not given)

    Returns:
        sequence: List of job_ids in execution order
        total_profit: Maximum profit achieved
    """
    if not jobs:
        return [], 0

    # Sort jobs by profit descending (greedy choice)
    sorted_jobs = sorted(jobs, key=lambda x: x[2], reverse=True)

    # Find max deadline if not provided
    if max_deadline is None:
        max_deadline = max(job[1] for job in jobs)

    # Track occupied time slots (1-indexed for clarity)
    slots = [None] * (max_deadline + 1)  # slots[0] unused
    sequence = []
    total_profit = 0

    for job_id, deadline, profit in sorted_jobs:
        # Find latest available slot before deadline
        for slot in range(min(deadline, max_deadline), 0, -1):
            if slots[slot] is None:
                slots[slot] = job_id
                sequence.append((job_id, slot))
                total_profit += profit
                break

    # Sort sequence by time slot for output
    sequence.sort(key=lambda x: x[1])
    job_order = [job_id for job_id, slot in sequence]

    return job_order, total_profit


def print_solution(jobs, sequence, total_profit):
    """Print formatted solution"""
    print(f"\n{'Time Slot':<12} {'Job ID':<10} {'Deadline':<10} {'Profit':<10}")
    print("-" * 45)

    job_dict = {job_id: (deadline, profit) for job_id, deadline, profit in jobs}

    for slot, job_id in enumerate(sequence, 1):
        deadline, profit = job_dict[job_id]
        print(f"{slot:<12} {job_id:<10} {deadline:<10} {profit:<10}")

    print("-" * 45)
    print(f"{'TOTAL PROFIT':<12} {'':<10} {'':<10} {total_profit:<10}")


def run_example():
    """Run textbook example"""
    print("=" * 60)
    print("JOB SEQUENCING WITH DEADLINES - EXAMPLE")
    print("=" * 60)

    # Example: (job_id, deadline, profit)
    jobs = [
        ("J1", 2, 100),
        ("J2", 1, 19),
        ("J3", 2, 27),
        ("J4", 1, 25),
        ("J5", 3, 15),
    ]

    print("Jobs:")
    for job_id, deadline, profit in jobs:
        print(f"  {job_id}: Deadline={deadline}, Profit={profit}")

    sequence, total_profit = job_sequencing(jobs)
    print_solution(jobs, sequence, total_profit)

    # Expected: J1 (slot 1), J3 (slot 2), J5 (slot 3) = 100+27+15 = 142
    # Or: J4 (slot 1), J1 (slot 2), J5 (slot 3) = 25+100+15 = 140
    # Optimal: J4 (1), J1 (2), J5 (3) or J2(1), J1(2), J3(3)? Let's check
    # Sorted by profit: J1(100), J3(27), J4(25), J2(19), J5(15)
    # J1 -> slot 2, J3 -> slot 1, J4 -> slot 1 taken, try slot 1, full... J4 deadline 1, slot 1 taken
    # Wait: J1 deadline 2 -> slot 2; J3 deadline 2 -> slot 1; J4 deadline 1 -> slot 1 taken
    # J2 deadline 1 -> slot 1 taken; J5 deadline 3 -> slot 3
    # Sequence: J3, J1, J5 = 27+100+15 = 142

    print(f"\nExpected optimal profit: 142")
    print(f"Actual profit: {total_profit}")
    print(f"Correct: {total_profit == 142}")


def run_additional_tests():
    """Additional test cases"""
    print("\n" + "=" * 60)
    print("ADDITIONAL TEST CASES")
    print("=" * 60)

    # Test 1: All jobs fit
    jobs1 = [("A", 3, 10), ("B", 2, 20), ("C", 1, 30)]
    seq, profit = job_sequencing(jobs1)
    print(f"\nTest 1 - All fit: Profit={profit}, Expected=60, Pass={profit==60}")

    # Test 2: More jobs than slots
    jobs2 = [("A", 1, 10), ("B", 1, 20), ("C", 1, 30), ("D", 1, 40)]
    seq, profit = job_sequencing(jobs2)
    print(f"Test 2 - More jobs than slots: Profit={profit}, Expected=40, Pass={profit==40}")

    # Test 3: Single job
    jobs3 = [("Only", 5, 100)]
    seq, profit = job_sequencing(jobs3)
    print(f"Test 3 - Single job: Profit={profit}, Expected=100, Pass={profit==100}")

    # Test 4: Zero profit jobs
    jobs4 = [("A", 2, 0), ("B", 1, 10)]
    seq, profit = job_sequencing(jobs4)
    print(f"Test 4 - Zero profit: Profit={profit}, Expected=10, Pass={profit==10}")

    # Test 5: Large deadlines
    jobs5 = [("A", 10, 50), ("B", 5, 100), ("C", 3, 30)]
    seq, profit = job_sequencing(jobs5)
    print(f"Test 5 - Large deadlines: Profit={profit}, Expected=180, Pass={profit==180}")


def demonstrate_greedy_choice():
    """Show why sorting by profit works"""
    print("\n" + "=" * 60)
    print("GREEDY CHOICE EXPLANATION")
    print("=" * 60)

    print("""
Algorithm: Sort by profit descending, place each job in latest
available slot before its deadline.

Why greedy works (Exchange Argument):
1. Consider optimal schedule O and greedy schedule G
2. Let i be first job where they differ
3. G picks highest-profit available job for each slot
4. If O picks lower-profit job, we can swap with higher-profit
   job from G without violating deadlines (since G's job was
   placed in latest possible slot)
5. Swap doesn't decrease profit -> G is optimal

Time Complexity: O(n log n) for sorting + O(n * d) for placement
  where d = max deadline
Space Complexity: O(d) for slots array
    """)


def run_performance_test():
    """Quick performance test"""
    print("\n" + "=" * 60)
    print("PERFORMANCE TEST")
    print("=" * 60)

    import random
    import time

    random.seed(42)

    for n in [100, 500, 1000, 5000]:
        jobs = [(f"J{i}", random.randint(1, n), random.randint(1, 1000))
                for i in range(n)]
        max_d = n

        start = time.perf_counter()
        sequence, profit = job_sequencing(jobs, max_d)
        elapsed = (time.perf_counter() - start) * 1000

        print(f"  n={n:>5}: {elapsed:>8.2f} ms, jobs scheduled={len(sequence)}, profit={profit}")


if __name__ == "__main__":
    run_example()
    run_additional_tests()
    demonstrate_greedy_choice()
    run_performance_test()

    print("\n" + "=" * 60)
    print("LEARNING OUTCOMES")
    print("=" * 60)
    print("1. Greedy choice: highest profit first")
    print("2. Place each job in latest available slot before deadline")
    print("3. Time complexity: O(n log n) sort + O(n*d) placement")
    print("4. Space complexity: O(d) where d = max deadline")
    print("5. Optimality proof: Exchange argument")
    print("6. Applications: Task scheduling, CPU job scheduling,")
    print("   project management with deadlines")
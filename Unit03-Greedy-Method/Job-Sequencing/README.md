# Job Sequencing with Deadlines - Unit 3: Greedy Method

## Problem Statement

Given n jobs, each with a deadline and profit. Each job takes 1 unit of time to complete. Only one job can be scheduled at a time. Maximize total profit by completing jobs before their deadlines.

## Algorithm / Approach

### Greedy Strategy

**Greedy Choice**: Select jobs in decreasing order of profit. Place each job in the latest available time slot before its deadline.

1. Sort all jobs by profit descending
2. For each job (highest profit first):
   - Find latest available time slot ≤ deadline
   - If found, schedule job there
   - If no slot available, skip job
3. Sum profits of scheduled jobs

### Why Greedy Works (Exchange Argument)

- Let G be greedy schedule, O be optimal schedule
- Let i be first time slot where G and O differ
- G places highest-profit available job in slot i
- O places some lower-profit job in slot i
- The higher-profit job must appear later in O (or not at all)
- Swap them in O: deadlines still satisfied (G placed it in latest possible slot)
- Profit doesn't decrease → contradiction if O was strictly better

## Pseudocode

```
JOB_SEQUENCING(jobs, max_deadline):
    // jobs: array of (job_id, deadline, profit)
    sort jobs by profit descending

    slots[1..max_deadline] ← all NULL
    sequence ← empty list
    total_profit ← 0

    for each job in jobs:
        // Find latest available slot ≤ deadline
        for slot from min(job.deadline, max_deadline) down to 1:
            if slots[slot] = NULL then
                slots[slot] ← job.id
                add (job.id, slot) to sequence
                total_profit ← total_profit + job.profit
                break
            end if
        end for
    end for

    sort sequence by slot
    return sequence, total_profit
```

## Time & Space Complexity

| Operation | Complexity |
|-----------|------------|
| Sorting by profit | O(n log n) |
| Slot placement | O(n × d) where d = max deadline |
| **Total Time** | **O(n log n + n×d)** |
| **Space** | **O(d)** for slots array |

## Sample Input / Output

### Example
```
Jobs:
  J1: Deadline=2, Profit=100
  J2: Deadline=1, Profit=19
  J3: Deadline=2, Profit=27
  J4: Deadline=1, Profit=25
  J5: Deadline=3, Profit=15

Sorted by profit: J1(100), J3(27), J4(25), J2(19), J5(15)

Step 1: J1 (deadline 2) → place in slot 2
Step 2: J3 (deadline 2) → place in slot 1
Step 3: J4 (deadline 1) → slot 1 taken, skip
Step 4: J2 (deadline 1) → slot 1 taken, skip
Step 5: J5 (deadline 3) → place in slot 3

Result:
Time Slot    Job ID     Deadline   Profit
1            J3         2          27
2            J1         2          100
3            J5         3          15
------------------------------------------
TOTAL PROFIT                        142
```

## Learning Outcomes

1. **Greedy Choice**: Highest profit job first
2. **Slot Placement**: Latest available slot before deadline
3. **Optimality Proof**: Exchange argument
4. **Time Complexity**: O(n log n + n×d)
5. **Space Complexity**: O(d)
6. **Practical Applications**: CPU scheduling, task planning, project management

## Files in this Directory

- `job_sequencing.py` - Implementation with examples and tests
- `README.md` - This documentation

## How to Run

```bash
python job_sequencing.py
```

This will:
1. Run textbook example with step-by-step output
2. Execute additional test cases
3. Explain greedy choice property
4. Run performance benchmarks
5. Display learning outcomes
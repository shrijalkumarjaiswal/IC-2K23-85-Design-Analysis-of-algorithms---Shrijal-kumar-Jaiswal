"""
Fractional Knapsack Problem - Unit 3: Greedy Method
Items can be broken into fractions. Greedy choice: highest value/weight ratio first.
"""

def fractional_knapsack(items, capacity):
    """
    Solve fractional knapsack using greedy approach.

    Args:
        items: List of (value, weight, name) tuples
        capacity: Maximum weight capacity of knapsack

    Returns:
        total_value: Maximum achievable value
        selected_items: List of (name, fraction_taken, value_obtained)
    """
    # Sort by value/weight ratio descending
    sorted_items = sorted(items, key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0
    selected_items = []
    remaining_capacity = capacity

    for value, weight, name in sorted_items:
        if remaining_capacity == 0:
            break

        if weight <= remaining_capacity:
            # Take whole item
            fraction = 1.0
            value_obtained = value
            remaining_capacity -= weight
        else:
            # Take fraction of item
            fraction = remaining_capacity / weight
            value_obtained = value * fraction
            remaining_capacity = 0

        total_value += value_obtained
        selected_items.append((name, fraction, value_obtained))

    return total_value, selected_items


def print_solution(items, capacity, total_value, selected_items):
    """Print formatted solution"""
    print(f"\n{'Item':<12} {'Value':>8} {'Weight':>8} {'Ratio':>8} {'Taken':>8} {'Value':>8}")
    print("-" * 58)

    # Create lookup for quick ratio calculation
    item_dict = {name: (val, wt) for val, wt, name in items}

    for name, fraction, val_obtained in selected_items:
        value, weight = item_dict[name]
        ratio = value / weight
        taken_str = f"{fraction:.2f}" if fraction < 1 else "1.00"
        print(f"{name:<12} {value:>8} {weight:>8} {ratio:>8.2f} {taken_str:>8} {val_obtained:>8.2f}")

    print("-" * 58)
    print(f"{'TOTAL':<12} {'':>8} {'':>8} {'':>8} {'':>8} {total_value:>8.2f}")
    print(f"Capacity used: {capacity - sum(item_dict[n][1]*f for n,f,_ in selected_items):.2f} / {capacity}")


def run_example():
    """Run example from textbook"""
    print("=" * 60)
    print("FRACTIONAL KNAPSACK - EXAMPLE")
    print("=" * 60)

    # Example: (value, weight, name)
    items = [
        (60, 10, "Item1"),
        (100, 20, "Item2"),
        (120, 30, "Item3"),
    ]
    capacity = 50

    print(f"Knapsack Capacity: {capacity}")
    print("Items:")
    for v, w, n in items:
        print(f"  {n}: Value={v}, Weight={w}, Ratio={v/w:.2f}")

    total_value, selected = fractional_knapsack(items, capacity)
    print_solution(items, capacity, total_value, selected)

    # Expected: Take all of Item1 (60/10=6.0), all of Item2 (100/20=5.0),
    # and 20/30 of Item3 (120/30=4.0) = 60 + 100 + 80 = 240
    print(f"\nExpected optimal value: 240.00")
    print(f"Actual value: {total_value:.2f}")
    print(f"Correct: {abs(total_value - 240.0) < 0.01}")


def run_additional_tests():
    """Additional test cases"""
    print("\n" + "=" * 60)
    print("ADDITIONAL TEST CASES")
    print("=" * 60)

    # Test 1: Single item fits exactly
    items1 = [(50, 10, "Gold")]
    total, selected = fractional_knapsack(items1, 10)
    print(f"\nTest 1 - Single item: Value={total:.2f}, Expected=50.00, Pass={total==50}")

    # Test 2: Single item, take fraction
    items2 = [(100, 50, "Diamond")]
    total, selected = fractional_knapsack(items2, 25)
    print(f"Test 2 - Fraction: Value={total:.2f}, Expected=50.00, Pass={abs(total-50)<0.01}")

    # Test 3: Multiple items, exact fit
    items3 = [(10, 5, "A"), (20, 10, "B"), (30, 15, "C")]
    total, selected = fractional_knapsack(items3, 30)
    # Ratios: A=2.0, B=2.0, C=2.0 - all same, any order gives 60
    print(f"Test 3 - Equal ratios: Value={total:.2f}, Expected=60.00, Pass={abs(total-60)<0.01}")

    # Test 4: Capacity 0
    items4 = [(100, 10, "A")]
    total, selected = fractional_knapsack(items4, 0)
    print(f"Test 4 - Zero capacity: Value={total:.2f}, Expected=0.00, Pass={total==0}")

    # Test 5: Many items
    import random
    random.seed(42)
    items5 = [(random.randint(10, 100), random.randint(1, 20), f"Item{i}") for i in range(20)]
    total, selected = fractional_knapsack(items5, 50)
    print(f"Test 5 - 20 random items: Value={total:.2f}, Items taken={len(selected)}")


def verify_greedy_choice():
    """Verify greedy choice property"""
    print("\n" + "=" * 60)
    print("GREEDY CHOICE PROPERTY VERIFICATION")
    print("=" * 60)

    # Counterexample for 0/1 knapsack (where greedy fails)
    items_01 = [(60, 10, "A"), (100, 20, "B"), (120, 30, "C")]
    capacity = 50

    # Greedy by ratio: A(6.0), B(5.0), C(4.0) -> take A, B, 20/30 C = 240
    # But for 0/1 (can't take fraction): A+B = 160, A+C = 180, B+C = 220
    # Optimal 0/1 is B+C = 220, but greedy would take A+B = 160

    print("0/1 Knapsack (greedy by ratio FAILS):")
    greedy_items = sorted(items_01, key=lambda x: x[0]/x[1], reverse=True)
    val_01 = 0
    wt_01 = 0
    for v, w, n in greedy_items:
        if wt_01 + w <= capacity:
            val_01 += v
            wt_01 += w
    print(f"  Greedy (by ratio) value: {val_01}")
    print(f"  Optimal 0/1 value: 220 (items B+C)")
    print("  -> Greedy fails for 0/1 Knapsack")

    print("\nFractional Knapsack (greedy by ratio WORKS):")
    val_frac, _ = fractional_knapsack(items_01, capacity)
    print(f"  Greedy (by ratio) value: {val_frac}")
    print(f"  Optimal fractional value: 240")
    print("  -> Greedy succeeds for Fractional Knapsack")


if __name__ == "__main__":
    run_example()
    run_additional_tests()
    verify_greedy_choice()

    print("\n" + "=" * 60)
    print("LEARNING OUTCOMES")
    print("=" * 60)
    print("1. Greedy choice: highest value/weight ratio first")
    print("2. Fractional knapsack allows optimal greedy solution")
    print("3. Time complexity: O(n log n) for sorting")
    print("4. Space complexity: O(n) for sorted items")
    print("5. Greedy fails for 0/1 knapsack (requires DP)")
    print("6. Proof: Exchange argument - any optimal solution")
    print("   can be transformed to greedy without decreasing value")
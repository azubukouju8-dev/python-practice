# Exercise 8 (part 3): The entry point that ties everything together.

from helpers import biggest_expense, format_money, total_by_category, total_spent


def get_sample_expenses():
    """Return a small list of example expenses."""
    return [
        {"name": "Lunch", "category": "food", "amount": 12.50},
        {"name": "Bus fare", "category": "transport", "amount": 3.00},
        {"name": "Data bundle", "category": "data", "amount": 10.00},
        {"name": "Dinner", "category": "food", "amount": 18.75},
        {"name": "Book", "category": "other", "amount": 25.00},
        {"name": "Taxi", "category": "transport", "amount": 8.50},
    ]


def print_report(expenses):
    """Print a formatted expense report."""
    print("=== Expense Report ===")
    print(f"Total spent: {format_money(total_spent(expenses))}")

    print("\nBy category:")
    for category, amount in total_by_category(expenses).items():
        print(f"  {category}: {format_money(amount)}")

    top = biggest_expense(expenses)
    print(f"\nBiggest expense: {top['name']} ({format_money(top['amount'])})")


def main():
    expenses = get_sample_expenses()
    print_report(expenses)


if __name__ == "__main__":
    main()
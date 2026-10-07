# Exercise 8 (part 2): Reusable logic, with no printing and no sample data.

from config import CATEGORIES, CURRENCY


def total_spent(expenses):
    """Return the sum of all expense amounts."""
    return sum(item["amount"] for item in expenses)


def total_by_category(expenses):
    """Return a dictionary of totals per category. Unknown categories count as 'other'."""
    totals = {category: 0 for category in CATEGORIES}
    for item in expenses:
        category = item["category"] if item["category"] in totals else "other"
        totals[category] += item["amount"]
    return totals


def biggest_expense(expenses):
    """Return the most expensive item, or None if the list is empty."""
    if not expenses:
        return None
    return max(expenses, key=lambda item: item["amount"])


def format_money(amount):
    """Format a number as money, for example '12.50 USD'."""
    return f"{amount:.2f} {CURRENCY}"
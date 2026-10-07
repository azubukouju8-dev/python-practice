# Exercise 6: Error handling
# Uses try / except / else / finally and raises custom errors.


def safe_divide(a, b):
    """Divide a by b, returning a friendly message instead of crashing."""
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: cannot divide by zero"
    except TypeError:
        return "Error: both values must be numbers"
    else:
        return result
    finally:
        print(f"(finished dividing {a} by {b})")


def parse_age(text):
    """Convert text to a valid age, or raise a ValueError with a clear message."""
    try:
        age = int(text)
    except ValueError:
        raise ValueError(f"'{text}' is not a valid whole number")
    if age < 0 or age > 120:
        raise ValueError(f"{age} is outside the realistic range 0-120")
    return age


if __name__ == "__main__":
    print(safe_divide(10, 2))
    print(safe_divide(5, 0))
    print(safe_divide("a", 2))

    for entry in ["21", "abc", "-5", "200"]:
        try:
            print("Valid age:", parse_age(entry))
        except ValueError as error:
            print("Rejected:", error)
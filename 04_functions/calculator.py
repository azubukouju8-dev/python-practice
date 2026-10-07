# Exercise 4: Functions
# A small toolkit of reusable functions with parameters, defaults and return values.


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def divide(a, b):
    """Return a divided by b, or None if b is zero."""
    if b == 0:
        return None
    return a / b


def average(numbers):
    """Return the average of a list of numbers, or 0 for an empty list."""
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


def celsius_to_fahrenheit(celsius):
    """Convert a temperature from Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


def greet(name, greeting="Hello"):
    """Return a greeting. 'greeting' has a default value."""
    return f"{greeting}, {name}!"


if __name__ == "__main__":
    print("add(2, 3) =", add(2, 3))
    print("divide(10, 4) =", divide(10, 4))
    print("divide(5, 0) =", divide(5, 0))
    print("average([70, 80, 90]) =", average([70, 80, 90]))
    print("celsius_to_fahrenheit(100) =", celsius_to_fahrenheit(100))
    print(greet("Uju"))
    print(greet("Uju", greeting="Good morning"))
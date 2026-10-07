# Automated tests for the calculator functions in Exercise 4.

from calculator import add, average, celsius_to_fahrenheit, divide, greet


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_divide_normal():
    assert divide(10, 4) == 2.5


def test_divide_by_zero_returns_none():
    assert divide(5, 0) is None


def test_average():
    assert average([70, 80, 90]) == 80


def test_average_of_empty_list_is_zero():
    assert average([]) == 0


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(0) == 32


def test_greet_default_and_custom_greeting():
    assert greet("Uju") == "Hello, Uju!"
    assert greet("Uju", greeting="Good morning") == "Good morning, Uju!"
# Exercise 5 (part 1): A custom module of small text helpers.


def shout(text):
    """Return the text in capitals with an exclamation mark."""
    return text.upper() + "!"


def count_vowels(text):
    """Count how many vowels are in the text."""
    return sum(1 for letter in text.lower() if letter in "aeiou")


def is_palindrome(text):
    """Return True if the text reads the same forwards and backwards."""
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]
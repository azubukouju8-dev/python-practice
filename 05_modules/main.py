# Exercise 5 (part 2): Using standard library modules and a custom module.

import math
from datetime import date

import string_tools
from string_tools import is_palindrome

# Standard library: math
print("Square root of 144:", math.sqrt(144))
print("Pi rounded:", round(math.pi, 2))
print("4.2 rounded up:", math.ceil(4.2))

# Standard library: datetime
print("Date:", date(2026, 10, 6).strftime("%d %B %Y"))

# Custom module: string_tools
print(string_tools.shout("hello"))
print("Vowels in 'Automation':", string_tools.count_vowels("Automation"))
print("Is 'Racecar' a palindrome?", is_palindrome("Racecar"))
print("Is 'Python' a palindrome?", is_palindrome("Python"))
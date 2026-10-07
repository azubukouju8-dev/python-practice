# Exercise 3: Loops
# Demonstrates for loops, while loops, and a classic FizzBuzz challenge.

# 1. for loop with range(): a multiplication table
number = 7
print(f"Multiplication table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# 2. for loop over a list: adding up a running total
prices = [1500, 2300, 800, 4200]
total = 0
for price in prices:
    total += price
print(f"\nTotal of prices: {total}")

# 3. while loop: a countdown
count = 5
print("\nCountdown:")
while count > 0:
    print(count)
    count -= 1
print("Liftoff!")

# 4. FizzBuzz: loops and conditionals working together
print("\nFizzBuzz:")
for n in range(1, 16):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
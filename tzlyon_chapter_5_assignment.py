"""
Loop Mastery Assignment
Student Name: Talib Lyon
GitHub Username: TalibLyon
Date: February 18, 2026

Overview:
This program demonstrates the use of while loops, for loops,
and nested loops through four different challenges.
"""

# =====================================
# Step 1: Collatz Sequence
# =====================================

print("=== Step 1: Collatz Sequence ===")

number = int(input("Enter starting number: "))

if number <= 0:
    print("Enter a positive number.")
else:
    steps = 0
    print("Sequence:", end=" ")

    while number != 1:
        print(number, end=" ")

        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1

        steps += 1

    print(1)
    print("Steps:", steps)


# =====================================
# Step 2: Prime Checker
# =====================================

print("\n=== Step 2: Prime Checker ===")

number = int(input("Enter a number: "))

if number <= 1:
    print(f"{number} is not prime.")
else:
    is_prime = True

    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is prime.")
    else:
        print(f"{number} is not prime.")


# =====================================
# Step 3: Multiplication Table
# =====================================

print("\n=== Step 3: Multiplication Table ===")

print("    ", end="")
for col in range(1, 11):
    print(f"{col:4}", end="")
print()

for row in range(1, 11):
    print(f"{row:4}", end="")
    for col in range(1, 11):
        print(f"{row * col:4}", end="")
    print()


# =====================================
# Step 4: Statistics Dashboard
# =====================================

print("\n=== Step 4: Statistics Dashboard ===")
print("Enter positive numbers (enter -1 to finish):")

numbers = []

while True:
    value = int(input("Enter number: "))
    if value == -1:
        break
    if value > 0:
        numbers.append(value)

if len(numbers) > 0:

    total = 0
    minimum = numbers[0]
    maximum = numbers[0]

    for num in numbers:
        total += num
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    average = total / len(numbers)

    print("\n=== Statistics ===")
    print("Count:", len(numbers))
    print("Sum:", total)
    print(f"Average: {average:.2f}")
    print("Minimum:", minimum)
    print("Maximum:", maximum)

    print("\n=== Bar Chart ===")
    for num in numbers:
        print(f"{num}: ", end="")
        for _ in range(num):
            print("*", end="")
        print()

else:
    print("No numbers were entered.")

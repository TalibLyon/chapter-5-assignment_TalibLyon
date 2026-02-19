"""
COMP 163 - Introduction to Programming
Assignment: Chapter 5 - Loop Mastery
Name: Talib Lyon
GitHub Username: TalibLyon
Date: February 18, 2026
Description: This program demonstrates mastery of while loops, for loops,
nested loops, and loop selection through four programming challenges.
AI Usage: Used for clarification of loop explanations and structure guidance.
"""

# ========================================
# Step 1: Collatz Sequence Generator
# ========================================

print("=== Collatz Sequence ===")
print("=== Collatz Sequence ===")

starting_number = int(input("Enter starting number: "))

current_number = starting_number
steps = 0

print("Sequence:", end=" ")

# Use while loop because we do not know how many steps
# it will take until the number reaches 1
while current_number != 1:
    print(current_number, end=" ")

    # Check if number is even using modulo
    # Even numbers are divided by 2 in Collatz sequence
    if current_number % 2 == 0:
        current_number = current_number // 2
    else:
        # Odd numbers are multiplied by 3 and increased by 1
        current_number = current_number * 3 + 1

    steps += 1

# Print the final 1
print(1)
print("Steps:", steps)



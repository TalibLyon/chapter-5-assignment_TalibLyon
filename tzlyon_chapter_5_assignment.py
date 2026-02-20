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
#A while loop is the best choice because we do not know ahead of time how many iterations will happen. The sequence continues until the number becomes 1, and that depends entirely on the starting value. Since the stopping condition is based on a condition rather than a fixed count, a while loop makes the most sense
#The program works by taking a starting number and uses a while loop to apply the Collatz rules until the number becomes 1. Even numbers are divided by 2, and odd numbers are multiplied by 3 and increased by 1. Theres a counter that keeps track of how many steps it takes to reach 1.
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

# Step 2: Prime Checker
#A for loop is used because we know the specific range of possible to test, making the number of iterations predictable.
#The program uses a for loop to test disivibility from 2 to one less than the number. If the number divides evenly by any value, it is not prime; otherwise, it is prime. 
number = int(input("\nEnter a number: "))

if number <= 1:
    print(f"{number} is not prime.")
else:
    print(f"Testing divisors from 2 to {number - 1}...")
    
    is_prime = True
    
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"{number} is prime!")
    else:
        print(f"{number} is not prime.")


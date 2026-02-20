[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/IiqXY2S6)
# Loop Mastery Assignment

**Student Name:** [Talib Lyon]  
**GitHub Username:** [TalibLyon]  
**Date:** [February 18, 2026]

## Overview

This assignment demonstrates mastery of while loops, for loops, and nested loops through four programming challenges. Each challenge was selected to showcase the appropriate loop type for different problem scenarios.

---

## Loop Type Analysis

### Step 1: Collatz Sequence - While Loop

**Why while loop?**  
[A while loop is the best choice because we do not know ahead of time how many iterations will happen. The sequence continues until the number becomes 1, and that depends entirely on the starting value. Since the stopping condition is based on a condition rather than a fixed count, a while loop makes the most sense]

**How it works:**  
[ The program works by taking a starting number and uses a while loop to apply the Collatz rules until the number becomes 1. Even numbers are divided by 2, and odd numbers are multiplied by 3 and increased by 1. Theres a counter that keeps track of how many steps it takes to reach 1.]

**Example:**
```
Enter starting number: 13
Sequence: 13 40 20 10 5 16 8 4 2 1
Steps: 9
```

---

### Step 2: Prime Checker - For Loop

**Why for loop?**  
[A for loop is used because we know the specific range of possible to test, making the number of iterations predictable.]

**How it works:**  
[The program uses a for loop to test disivibility from 2 to one less than the number. If the number divides evenly by any value, it is not prime; otherwise, it is prime. ]

**Example:**
```
Enter a number: 17
Testing divisors from 2 to 16...
17 is prime!
```

---

### Step 3: Multiplication Table - Nested Loops

**Why nested loops?**  
[Nested loops are needed because a multiplication table has rows and columns. One loop controls the rows, and the other controls the columns.]

**Outer vs Inner:**  
[The Outer loop creates each row. The inner loop calculates and prints the values in that row.]

**How it works:**  
[The program prints numbers  1-10 across  the top.  The outer loop runs  through each  row, and the  inner loop multiplies the row number by 1-10 to create a table.]

**Example:**
```
Multiplication Table:
    1   2   3   4   5   6   7   8   9  10
 1  1   2   3   4   5   6   7   8   9  10
 2  2   4   6   8  10  12  14  16  18  20
...
```

---

### Step 4: Statistics Dashboard - All Three Loop Types

**Why all three?**  
[Explain why this problem requires all three loop types:]
- **While loop:** [While loop is used to keep asking for input until the user enters -1.]
- **For loop:** [For loop is Used to calculate tootal, minimun, maximum, as well as average.]
- **Nested loops:** [# Nested loop is used to create the bar chart with stars for each  number.]

**How it works:**  
[Provide a comprehensive explanation of your implementation:]
- The program collects positive numbers using a while loop until -1 is entered.
- A for loop calculates the statistics.
- Nested loops generate a bar chart when each number is represented by stars

**Example:**
```
=== Statistics Dashboard ===
Enter positive numbers (enter -1 to finish):
Enter number: 5
Enter number: 12
Enter number: 8
Enter number: 15
Enter number: 3
Enter number: -1

=== Statistics ===
Count: 5 numbers
Sum: 43
Average: 8.6
Minimum: 3
Maximum: 15

=== Bar Chart ===
 5: *****
12: ************
 8: ********
15: ***************
 3: ***
```

### Edge Cases Considered

[List any edge cases you thought about or tested:]
- Example: Collatz with big numbers
- Example: Trying to input -1 immediately

---

## Challenges and Solutions

### Challenge 1: [Github was not syncing my repository together]
**Solution:** [I solved it by going back and seeing what  was wrong in my folders and during this process it was revealed to me by a TA that i was doing the assignment wrong. I received help the help  needed, i fixed my code, and synced everything up.]

### Challenge 2: [Formatting Everything]
**Solution:** [I solved by trial and error and as i went  further down the  line, it started looking right. The multiplication  table was also hard but i just needed to fix the  string spacing and align the column correctly]

[Add more if needed]

---

## Key Learnings

[Reflect on what you learned from this assignment:]
- What did you learn about choosing the right loop type?
- What was the most challenging part?
- How did this assignment improve your programming skills?

---

## AI Usage

[Choose one:]


**Option B - AI Used (be specific):**
AI assistance was used for the following:

1. **[Specific concept]:**  
   - What you asked: [I asked  Ai to clarify loop concepts and explanations for their uses]
   - What you learned: [I relearned where each type of loop goes where]
   - How you used it: [I used this knowledge to place each loop where they needed to be in order for the code to be correct.]

2. **[AI Collatz]:**  
   - What you asked: [I asked what are  the rules of the collatz sequence and what it even is]
   - What you learned: [I learned what the Collatz Sequence is, the counting  iterations, and the rules.]
   - How you used it: [I applied the my own loop to collatz sequence and made it fit to my code]

**All core logic and implementation were developed independently after understanding the concepts.**


## Commit History

This assignment was developed incrementally with meaningful commits:

---

**Declaration:** I certify that this assignment is my own work and I have not copied code from other students or unauthorized sources. Any AI assistance used has been properly documented above.

**Signature:** [Talib Lyon]  
**Date:** [2/20.26]

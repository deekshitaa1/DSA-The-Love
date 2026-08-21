"""
============================================================
        SUM OF SQUARES OF FIRST N NATURAL NUMBERS
============================================================

PROBLEM STATEMENT
-----------------
Given a positive integer n, find the sum of the squares of
the first n natural numbers.


WHAT DOES THE PROBLEM MEAN?
---------------------------

Natural numbers are:

    1, 2, 3, 4, 5, 6, ...

The square of a number means multiplying the number by itself.

    1² = 1 × 1 = 1
    2² = 2 × 2 = 4
    3² = 3 × 3 = 9
    4² = 4 × 4 = 16


So, if n = 4, we need to calculate:

    1² + 2² + 3² + 4²

    = 1 + 4 + 9 + 16

    = 30


EXAMPLE
--------
Input:
    n = 5

We need:

    1² + 2² + 3² + 4² + 5²

    = 1 + 4 + 9 + 16 + 25

    = 55

Output:
    55


============================================================
APPROACH 1: ADD THE SQUARES ONE BY ONE
============================================================

IDEA
----
The simplest way is to visit every number from 1 to n.

For every number:

    1. Find its square.
    2. Add the square to the total.
    3. Move to the next number.

For example, n = 4:

    Start:
        sum = 0

    1²:
        sum = 0 + 1
        sum = 1

    2²:
        sum = 1 + 4
        sum = 5

    3²:
        sum = 5 + 9
        sum = 14

    4²:
        sum = 14 + 16
        sum = 30


LOGIC
-----
    Start with sum = 0
            ↓
    Take numbers from 1 to n
            ↓
    Find the square of current number
            ↓
    Add it to sum
            ↓
    Move to the next number
            ↓
    Repeat until n


TIME COMPLEXITY
---------------
    O(n)

WHY?
----
We visit every number from 1 to n.

If n = 10:
    10 numbers are processed.

If n = 1,000:
    1,000 numbers are processed.

If n = 1,000,000:
    1,000,000 numbers are processed.

Therefore:

    Time Complexity = O(n)


SPACE COMPLEXITY
----------------
    O(1)

WHY?
----
We only need a constant amount of extra space for variables
such as the current number and the running sum.


============================================================
APPROACH 2: MATHEMATICAL FORMULA
============================================================

OBSERVATION
-----------
Instead of calculating every square one by one, mathematics
gives us a direct formula for the sum of squares.

The formula is:

              n × (n + 1) × (2n + 1)
    Sum =     -----------------------
                         6


FORMULA
-------
    1² + 2² + 3² + ... + n²
             =
    n(n + 1)(2n + 1) / 6


EXAMPLE
-------
Find the sum of squares of the first 3 natural numbers.

We know:

    1² + 2² + 3²
    = 1 + 4 + 9
    = 14


Using the formula:

    n = 3

    Sum = n(n + 1)(2n + 1) / 6

        = 3(3 + 1)(2 × 3 + 1) / 6

        = 3 × 4 × 7 / 6

        = 84 / 6

        = 14


WHY IS THIS APPROACH BETTER?
----------------------------

The loop approach processes every number from 1 to n.

The formula directly calculates the answer.

For example:

    n = 1,000,000

Loop approach:
    Process 1,000,000 numbers
    → O(n)

Formula approach:
    Perform a fixed number of calculations
    → O(1)


TIME COMPLEXITY
---------------
    O(1)


SPACE COMPLEXITY
----------------
    O(1)


============================================================
APPROACH COMPARISON
============================================================

Approach                    Time        Space
------------------------------------------------
Add squares using loop      O(n)        O(1)
Mathematical formula        O(1)        O(1)


KEY DSA LESSON
--------------
A problem may have a straightforward solution, but we should
always ask:

    "Can I find a mathematical pattern or formula?"

Here:

    Loop
      ↓
    O(n)
      ↓
    Mathematical observation
      ↓
    Formula
      ↓
    O(1)


IMPORTANT FORMULAS TO REMEMBER
------------------------------

1. Sum of first n natural numbers:

       n(n + 1)
       --------
           2


2. Sum of squares:

       n(n + 1)(2n + 1)
       -----------------
              6


3. Sum of cubes:

       [n(n + 1) / 2]²


============================================================
NEXT STEP
============================================================

Now that we understand:

    ✓ What the problem asks
    ✓ How to solve it using a loop
    ✓ Why the loop is O(n)
    ✓ The mathematical formula
    ✓ Why the formula is O(1)

We can now implement the solutions in Python.
============================================================
"""
#APPROACH 1: ADD THE SQUARES ONE BY ONE
'''The idea for this naive approach is to run a loop from 1 to n and sum up all the squares.'''





import code


#code
def Sum_Of_Squares(n):


    return sum([i**2 for i in range(1,n+1)])
n=int(input("enter an array: "))
print(Sum_Of_Squares(n))

# 2.[Expected Approach]- Using Mathematical Formulae - O(1) Time and O(1) Space

#code
def Summation(n):
    return (n * (n+1)*(2*n+1))//6
n=int(input("enter an input: "))
print(Summation(n))
'''Avoiding the overflow:
In the above method, sometimes due to large value of n, the value of (n * (n + 1) * (2 * n + 1)) would overflow. We can avoid this overflow up to some extent using the fact that n*(n+1) must be divisible by 2 and restructuring the formula as (n * (n + 1) / 2) * (2 * n + 1) / 3;'''

#code
def summation(n):
    return (n*(n+1)//2  *(2*n+1))//3
n=int(input("enter an number: "))
print(summation(n))

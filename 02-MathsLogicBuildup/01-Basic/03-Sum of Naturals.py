"""
============================================================
              SUM OF FIRST N NATURAL NUMBERS
============================================================

Problem Statement:
------------------
Given a positive integer n, find the sum of the first n
natural numbers.

Natural numbers:

    1, 2, 3, 4, 5, 6, ...

For example, if:

    n = 5

Then we need to calculate:

    1 + 2 + 3 + 4 + 5 = 15


Example 1:
----------
Input:
    n = 3

Output:
    6

Explanation:
    1 + 2 + 3 = 6


Example 2:
----------
Input:
    n = 5

Output:
    15

Explanation:
    1 + 2 + 3 + 4 + 5 = 15


============================================================
APPROACH 1: USING A LOOP
============================================================

Idea:
-----
Start with sum = 0.

Then visit every number from 1 to n and add it to sum.

For n = 4:

    Initially:
        sum = 0

    i = 1:
        sum = 0 + 1 = 1

    i = 2:
        sum = 1 + 2 = 3

    i = 3:
        sum = 3 + 3 = 6

    i = 4:
        sum = 6 + 4 = 10

Therefore:

    Sum = 10


Algorithm:
----------
1. Initialize sum = 0.
2. Start from i = 1.
3. Add i to sum.
4. Increase i by 1.
5. Continue until i reaches n.
6. Return sum.


Time Complexity:
----------------
    O(n)

Why?
----
The loop runs n times.

Space Complexity:
-----------------
    O(1)

Why?
----
Only a constant amount of extra memory is used.


============================================================
APPROACH 2: USING RECURSION
============================================================

Idea:
-----
The sum of the first n natural numbers can be written as:

    sum(n) = n + sum(n - 1)

For example:

    sum(5)
      ↓
    5 + sum(4)
      ↓
    5 + 4 + sum(3)
      ↓
    5 + 4 + 3 + sum(2)
      ↓
    5 + 4 + 3 + 2 + sum(1)
      ↓
    5 + 4 + 3 + 2 + 1
      ↓
    15


Base Case:
----------
When n = 1:

    sum(1) = 1

This tells the recursion when to stop.


Time Complexity:
----------------
    O(n)

Space Complexity:
-----------------
    O(n)

Why O(n) Space?
---------------
Each recursive call is stored on the call stack.


============================================================
APPROACH 3: USING MATHEMATICAL FORMULA
============================================================

Observation:
------------
There is a mathematical formula for finding the sum of the
first n natural numbers:

                n × (n + 1)
    Sum =       -----------
                    2

For example, n = 5:

                5 × (5 + 1)
    Sum =       -----------
                    2

                5 × 6
          =     -----
                  2

          =     15


Python:
-------
    return n * (n + 1) // 2


Time Complexity:
----------------
    O(1)

Why?
----
There is only a fixed number of arithmetic operations,
regardless of the value of n.


Space Complexity:
-----------------
    O(1)

Why?
----
No additional memory depending on n is required.


============================================================
COMPARISON
============================================================

Approach              Time        Space
------------------------------------------------
Loop                  O(n)        O(1)
Recursion             O(n)        O(n)
Formula               O(1)        O(1)

Best Approach:
--------------
The formula-based approach is the most efficient because
it calculates the answer directly without iterating through
all numbers.

============================================================
"""


# ============================================================
# APPROACH 1: USING A LOOP
# ============================================================

def sum_using_loop(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total


# ============================================================
# APPROACH 2: USING RECURSION
# ============================================================

def sum_using_recursion(n):
    if n == 1:
        return 1

    return n + sum_using_recursion(n - 1)


# ============================================================
# APPROACH 3: USING MATHEMATICAL FORMULA
# ============================================================

def sum_using_formula(n):
    return n * (n + 1) // 2


# ============================================================
# TEST
# ============================================================

n = int(input("Enter a number: "))

print("Using Loop      :", sum_using_loop(n))
print("Using Recursion :", sum_using_recursion(n))
print("Using Formula   :", sum_using_formula(n))

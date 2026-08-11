"""
============================================================
                 MULTIPLICATION TABLE
============================================================

Problem Statement:
------------------
Given a number n, print its multiplication table from 1 to 10.


Understanding the Problem:
---------------------------
A multiplication table shows the result of multiplying a
given number by consecutive numbers starting from 1.

For example, if:

    n = 5

Then we calculate:

    5 × 1 = 5
    5 × 2 = 10
    5 × 3 = 15
    ...
    5 × 10 = 50


Example 1:
----------
Input:
    n = 5

Output:
    5 × 1 = 5
    5 × 2 = 10
    5 × 3 = 15
    5 × 4 = 20
    5 × 5 = 25
    5 × 6 = 30
    5 × 7 = 35
    5 × 8 = 40
    5 × 9 = 45
    5 × 10 = 50


Example 2:
----------
Input:
    n = 2

Output:
    2 × 1 = 2
    2 × 2 = 4
    2 × 3 = 6
    2 × 4 = 8
    2 × 5 = 10
    2 × 6 = 12
    2 × 7 = 14
    2 × 8 = 16
    2 × 9 = 18
    2 × 10 = 20


------------------------------------------------------------
Approach: Iteration
------------------------------------------------------------

We need to perform the same operation 10 times:

    n × 1
    n × 2
    n × 3
    ...
    n × 10

Instead of writing 10 separate multiplication statements,
we use a loop.

The loop variable starts at 1 and continues up to 10.

For every iteration:

    result = n × i

where `i` represents the current multiplier.


Algorithm:
----------
1. Take the number n.
2. Start a loop from 1 to 10.
3. Multiply n by the current loop value.
4. Print the result.
5. Continue until the multiplier reaches 10.


Pseudocode:
-----------
    for i from 1 to 10:
        print n × i


Time Complexity:
----------------
    O(1)

Why?
----
The loop always runs exactly 10 times,
regardless of the value of n.

Therefore:

    10 operations → O(10) → O(1)


Space Complexity:
-----------------
    O(1)

Why?
----
Only a constant amount of extra space is used.


============================================================
"""


# 1. Iterative Approach
'''The iterative approach for printing a multiplication table involves using a loop to calculate and print the product of a given number and the numbers in range from 1 to 10. In this method, you begin with the number whose table you want to print and use a loop to multiply it with increasing values.
Time Complexity - O(1)
Space Complexity - O(1)

Illustration
Step by step execution of loop for the multiplication table of n = 5.

We have n = 5, and the loop will iterate from i = 1 to i = 10.

First Iteration (i = 1):

The loop multiplies n = 5 by i = 1.
Result: 5 * 1 = 5.
Output: 5 * 1 = 5.
Second Iteration (i = 2):

The loop multiplies n = 5 by i = 2.
Result: 5 * 2 = 10.
Output: 5 * 2 = 10.
Third Iteration (i = 3):

The loop multiplies n = 5 by i = 3.
Result: 5 * 3 = 15.
Output: 5 * 3 = 15.
....
....

Tenth Iteration (i = 10):

The loop multiplies n = 5 by i = 10.
Result: 5 * 10 = 50.
Output: 5 * 10 = 50.
'''
#Code
def Print_Table(n):
    for i in range(1,11):
        # multiplies from 1 to 10
        print("%d * %d = %d" % (n, i, n*i))
n=int(input("Enter an  Number: "))
Print_Table(n)


# 2. Recursive Approach
'''In this method, we pass i as an additional parameter with initial value as 1. We print n * i and then recursively call for i+1. We stop the recursion when i becomes 11 as we need to print only 10 multiples of given number and i.'''

#Code
def printTable(n, i=1):

    if i == 11:
        return

    print(n, "*", i, "=", n * i)

    printTable(n, i + 1)


n = int(input("Enter an input: "))

printTable(n)

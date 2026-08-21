"""
============================================================
                    CHECK EVEN OR ODD
============================================================

Problem Statement:
------------------
Given a number n, check whether the number is even or odd.

Return:
    True  -> if n is even
    False -> if n is odd


What is an Even Number?
-----------------------
A number is even if it is completely divisible by 2.

Examples:
    2, 4, 6, 8, 10, 12, ...


What is an Odd Number?
----------------------
A number is odd if it is NOT completely divisible by 2.

Examples:
    1, 3, 5, 7, 9, 11, ...


Examples:
---------
Input:
    n = 15

Output:
    False

Explanation:
    15 % 2 = 1
    Since the remainder is not 0, 15 is odd.


Input:
    n = 44

Output:
    True

Explanation:
    44 % 2 = 0
    Since the remainder is 0, 44 is even.


Basic Logic:
------------
    n % 2 == 0  -> Even
    n % 2 != 0  -> Odd


Time Complexity:
----------------
    O(1)

Space Complexity:
-----------------
    O(1)

============================================================
"""

# 1. [Naive Approach] By Finding the Remainder - O(1) Time and O(1) Space
'''We can check the remainder when divided by 2. If the remainder is 0, the number is even, otherwise it is odd. For example, when we divide 13 by 2, we get remainder as 1 and when we divide 14 by 2, we get remainder as 0.'''

#code

def isEven(n):

    if n%2==0:
        return True
    else:
        return False
n=int(input("enter an input: "))
if isEven(n):
    print(f"The {n} is even.")
else:
    print(f"The {n} is odd.")
# 2. [Efficient Approach] Using Bitwise AND Operator - O(1) Time and O(1) Space

'''The last bit of all odd numbers is always 1, while for even numbers it’s 0. So, when performing bitwise AND operation with 1, odd numbers give 1, and even numbers give 0.

Note: Bitwise operators are extremely fast and efficient because they operate directly at the binary level, making them significantly faster than arithmetic or logical operations.

Examples:

15  ->               1 1 1 1
                    &  0 0 0 1
                       -------
                       0 0 0 1 , so this we can say it is an odd number.

44 ->        1 0 1 1 0 0
            &  0 0 0 0 0 1
                 ----------
                0 0 0 0 0 0 , so this we can say it is an even number.'''

#code
def isOdd(n):
    if (n & 1)!=0:
        return False
    else:
        return True
n=int(input("enter an number: "))
if isOdd(n):
    print(f" {n} is even number.")
else:
    print(f" {n} is odd number.")

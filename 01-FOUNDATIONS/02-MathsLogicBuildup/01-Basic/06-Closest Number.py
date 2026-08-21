"""
============================================================
          CLOSEST NUMBER TO N AND DIVISIBLE BY M
============================================================

PROBLEM STATEMENT
-----------------

Given two integers `n` and `m`, where:

    m != 0

find the number that:

    1. Is divisible by m
    2. Is closest to n

If two numbers are equally close to n, return the number
with the greater absolute value.


============================================================
FIRST: WHAT DOES "DIVISIBLE" MEAN?
============================================================

A number is divisible by another number if the division
leaves no remainder.

For example:

    12 ÷ 4 = 3
    remainder = 0

Therefore:

    12 is divisible by 4


But:

    13 ÷ 4 = 3 remainder 1

Therefore:

    13 is NOT divisible by 4


Multiples of 4 are:

    ..., -12, -8, -4, 0, 4, 8, 12, 16, 20, ...


============================================================
SECOND: WHAT DOES "CLOSEST" MEAN?
============================================================

We need to find the divisible number with the smallest
distance from n.

The distance between two numbers is:

    |n - candidate|

The `| |` represents absolute value.

Absolute value means the distance from zero.

Examples:

    |5|  = 5
    |-5| = 5
    |0|  = 0


For example:

    n = 13
    m = 4

Multiples of 4 around 13 are:

    8, 12, 16, 20

Distances from 13:

    |13 - 8|  = 5
    |13 - 12| = 1
    |13 - 16| = 3
    |13 - 20| = 7

The smallest distance is:

    1

Therefore:

    Answer = 12


============================================================
EXAMPLE 1
============================================================

Input:

    n = 13
    m = 4


Multiples of 4 near 13:

    12
    16

Distance from 13:

    |13 - 12| = 1
    |13 - 16| = 3

Since 12 has the smaller distance:

    Answer = 12


============================================================
THE IMPORTANT CASE: WHEN TWO NUMBERS ARE EQUALLY CLOSE
============================================================

Consider:

    n = 15
    m = 6


Multiples of 6 around 15 are:

    12
    18


Distance from 15:

    |15 - 12| = 3
    |15 - 18| = 3


Both are equally close.

Now the problem gives us an additional rule:

    If there is a tie, choose the number
    having the maximum absolute value.


Compare:

    |12| = 12
    |18| = 18

Since:

    18 > 12

the answer is:

    18


============================================================
NEGATIVE NUMBERS
============================================================

Negative values make this problem more interesting.

Consider:

    n = -15
    m = 6


Multiples of 6 around -15 are:

    -12
    -18


Distance from -15:

    |-15 - (-12)| = 3
    |-15 - (-18)| = 3


Again, both are equally close.

Now apply the tie-breaking rule:

    |-12| = 12
    |-18| = 18

Since:

    18 > 12

the answer is:

    -18


IMPORTANT:

The answer is NOT chosen because it is numerically larger.

It is chosen because it has the larger ABSOLUTE VALUE.


============================================================
APPROACH 1: CHECK NEARBY NUMBERS
============================================================

The first idea that may come to mind is:

    "Let's check numbers around n."

For example:

    n = 13
    m = 4

We can inspect numbers around 13 and ask:

    "Is this number divisible by 4?"

For every candidate:

    1. Check whether it is divisible by m.
    2. If it is divisible, calculate its distance from n.
    3. Keep track of the closest valid number.
    4. If two numbers have the same distance,
       choose the one with greater absolute value.


GENERAL LOGIC
-------------

Start near n
      ↓
Check whether candidate is divisible by m
      ↓
If divisible:
      ↓
Calculate |n - candidate|
      ↓
Compare with the best answer found so far
      ↓
If distance is smaller:
      update answer
      ↓
If distance is equal:
      choose greater absolute value
      ↓
Continue checking


WHY DOES THIS WORK?
-------------------

Because eventually we examine the possible multiples of m
around n and compare their distances.


TIME COMPLEXITY
---------------

If we check a range proportional to m, the number of
candidates depends on m.

Therefore:

    Time Complexity = O(|m|)


SPACE COMPLEXITY
----------------

We only maintain a few variables.

Therefore:

    Space Complexity = O(1)


============================================================
APPROACH 2: USE THE QUOTIENT
============================================================

Instead of checking many numbers, we can use division to
directly find the multiples surrounding n.


CORE IDEA
---------

Every multiple of m can be represented as:

    m × q

where q is an integer.


When we divide n by m, the quotient tells us approximately
which multiple of m is near n.


For example:

    n = 13
    m = 4

13 / 4 gives a quotient around:

    3


The multiple corresponding to that quotient is:

    4 × 3 = 12


So 12 is one candidate.


But there may be another nearby multiple:

    4 × 4 = 16


Therefore, we only need to compare the multiples immediately
below and above n.


============================================================
THE TWO CANDIDATES
============================================================

For:

    n = 13
    m = 4

The nearby multiples are:

    12 and 16


Instead of checking:

    9
    10
    11
    12
    13
    14
    15
    16
    17

we directly identify:

    12
    16


This dramatically reduces the amount of work.


============================================================
HOW DO WE FIND THE CANDIDATES?
============================================================

Suppose:

    q = quotient of n / m


One candidate is:

    n1 = m × q


This gives one multiple of m close to n.


The next candidate is obtained by moving one quotient
step in the appropriate direction.

Conceptually:

    Candidate 1:
        m × q

    Candidate 2:
        m × (q + 1)

or, depending on the signs of n and m:

    m × (q - 1)


The reason for considering the sign is that positive and
negative numbers move in different directions on the number
line.


============================================================
WHY DO WE NEED TO THINK ABOUT SIGNS?
============================================================

Consider:

    n = 13
    m = 4

Both are positive.

The quotient is around:

    3

The neighboring multiples are:

    4 × 3 = 12
    4 × 4 = 16


Now consider:

    n = -15
    m = 6

The nearby multiples are:

    -12
    -18


The direction in which the quotient should move depends
on the signs of n and m.

This is why a robust solution must account for:

    n > 0, m > 0
    n > 0, m < 0
    n < 0, m > 0
    n < 0, m < 0


The key idea is:

    Same signs:
        move toward the next multiple in the same direction.

    Opposite signs:
        the neighboring quotient moves in the opposite
        direction.


============================================================
FINAL DECISION
============================================================

After finding the two candidate multiples:

    candidate 1
    candidate 2

we calculate their distances from n.

For each candidate:

    distance = |n - candidate|


Then:

    If distance 1 < distance 2:
        choose candidate 1

    If distance 2 < distance 1:
        choose candidate 2

    If distances are equal:
        choose the candidate with greater absolute value.


============================================================
COMPLETE LOGIC
============================================================

                Given n and m
                     ↓
                Find quotient
                     ↓
        Find nearby multiple #1
                     ↓
        Find nearby multiple #2
                     ↓
       Calculate distance of both
                     ↓
              Compare distances
                     ↓
          ┌──────────┴──────────┐
          ↓                     ↓
     Smaller distance       Equal distance
          ↓                     ↓
       Choose it          Compare absolute
                           values
                                ↓
                       Choose larger |value|
                                ↓
                             ANSWER


============================================================
WHY IS THE QUOTIENT APPROACH BETTER?
============================================================

The checking approach may examine many numbers.

The quotient approach directly identifies the only
relevant candidates around n.


Checking approach:

    Check many possible numbers
            ↓
          O(|m|)


Quotient approach:

    Calculate quotient
            ↓
    Find two candidates
            ↓
    Compare them
            ↓
          O(1)


Therefore:

    Time Complexity = O(1)

and:

    Space Complexity = O(1)


============================================================
WHY ONLY TWO CANDIDATES?
============================================================

Multiples of m are evenly spaced on the number line.

For example, when m = 5:

    ..., -10, -5, 0, 5, 10, 15, 20, ...


If n lies somewhere between two consecutive multiples,
the closest multiple must be one of those two.


For example:

    n = 13
    m = 5

Nearby multiples:

    10 -------- 13 -------- 15

Only 10 and 15 matter.

There is no reason to compare 5 or 20 because they are
already farther away.


This is the key mathematical observation behind the
O(1) solution.


============================================================
EDGE CASES TO THINK ABOUT
============================================================

CASE 1: n IS ALREADY DIVISIBLE BY m

Example:

    n = 20
    m = 5

20 is already a multiple of 5.

Therefore:

    Answer = 20


CASE 2: n IS BETWEEN TWO MULTIPLES

Example:

    n = 13
    m = 4

Nearby multiples:

    12 and 16

Choose the one with smaller distance.


CASE 3: EQUAL DISTANCE

Example:

    n = 15
    m = 6

Candidates:

    12 and 18

Both are 3 away.

Tie-break:

    |18| > |12|

Therefore:

    Answer = 18


CASE 4: NEGATIVE n

Example:

    n = -15
    m = 6

Candidates:

    -12 and -18

Both are 3 away.

Compare:

    |-12| = 12
    |-18| = 18

Therefore:

    Answer = -18


CASE 5: m IS NEGATIVE

Remember:

    m != 0

The sign of m changes the direction of the multiples,
but the set of multiples can still be considered when
finding the closest value.

The solution must therefore handle the sign correctly.


CASE 6: m = 0

This is NOT allowed.

The problem explicitly states:

    m != 0

Why?

Because division or remainder involving zero is undefined.


============================================================
IMPORTANT MATHEMATICAL CONCEPTS
============================================================

This problem combines several concepts:

    1. Division
    2. Quotient
    3. Remainder
    4. Multiples
    5. Absolute value
    6. Distance between numbers
    7. Negative numbers
    8. Sign of numbers
    9. Integer arithmetic
    10. Optimization


============================================================
KEY DSA LESSON
============================================================

The important lesson is NOT simply:

    "Find a number divisible by m."


The real lesson is:

    "Can we avoid checking every possible number?"


First thought:

    Check numbers one by one
            ↓
          O(|m|)


Better mathematical observation:

    Multiples of m are evenly spaced
            ↓
    Only two neighboring multiples can matter
            ↓
    Find them using the quotient
            ↓
          O(1)


This is a classic example of replacing:

        SEARCH

with:

        MATHEMATICAL POSITIONING


============================================================
COMPLEXITY COMPARISON
============================================================

Approach                         Time        Space
---------------------------------------------------------
Iterative checking              O(|m|)      O(1)
Quotient-based approach         O(1)        O(1)


============================================================
FINAL MENTAL MODEL
============================================================

When you see:

    "Find the number closest to n
     that is divisible by m"

Think:

        Multiples of m
              ↓
        Find neighbors
              ↓
        Only two candidates matter
              ↓
        Calculate their distances
              ↓
        Choose smaller distance
              ↓
        If tied:
              ↓
        Choose greater absolute value


The core idea is:

    CLOSEST DIVISIBLE NUMBER
            =
    ONE OF THE TWO NEAREST MULTIPLES


============================================================
"""
#[Naive Approach] Iterative Checking - O(m) Time and O(1) Space

#quaotient based approach


'''def ClosestNumber(n,m):
    q=int(n/m)

    n1=m*q
    if n*m>0:
        n2=m*(q+1)
    else:
        n2=m*(q-1)
    difference1=abs(n-n1)
    difference2=abs(n-n2)

    if difference1<difference2:
        return n1
    elif difference2<difference1:
        return n2
    else:
        if abs(n1)>abs(n2):
            return n1
        else:
            return n2
n=int(input("enter an number: "))
m=int(input("enter an number: "))
print(ClosestNumber(n,m))
'''
def ClosestNumber(n,m):
    q=int(n/m)
    n1=m*q
    if m*q>0:
        n2=(m*q)+1
    else:
        n2=(m*q)-1
    difference1=n-n1
    differennce2=n-n2
    if difference1<differennce2:
        return n1
    elif differennce2<difference1:
        return n2
    else:
        return n1

n=list(map(int,input("enter an array: ").split()))
m=int(input())
print(ClosestNumber(n,m))

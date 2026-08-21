"""
============================================================
                    SWAP TWO NUMBERS
============================================================

PROBLEM STATEMENT
-----------------

Given two numbers `a` and `b`, swap their values.

In simple words:

    Before swapping:

        a = 10
        b = 20

    After swapping:

        a = 20
        b = 10


WHAT DOES "SWAP" MEAN?
----------------------

Swapping means:

    The value stored in `a` moves to `b`
    AND
    The value stored in `b` moves to `a`.

It is NOT changing the values.

The two original values must simply exchange their positions.


EXAMPLE
-------

Before:

        a = 10
        b = 20

After:

        a = 20
        b = 10


Think of it like two boxes:

        ┌─────────┐       ┌─────────┐
        │    a    │       │    b    │
        │   10    │       │   20    │
        └─────────┘       └─────────┘

                SWAP

        ┌─────────┐       ┌─────────┐
        │    a    │       │    b    │
        │   20    │       │   10    │
        └─────────┘       └─────────┘


============================================================
WHY IS SWAPPING NOT AS SIMPLE AS IT LOOKS?
============================================================

Suppose:

        a = 10
        b = 20

We want:

        a = 20
        b = 10


A beginner might think:

        a = b

After this:

        a = 20
        b = 20

The original value of `a` (10) has been LOST.

This is the important problem.

We need to move the values without losing either
of the original values.


============================================================
APPROACH 1: USING A THIRD VARIABLE
============================================================

The safest and easiest way to understand swapping is to
use a temporary variable.

We introduce:

        temp

The temporary variable acts like a safe storage box.

Suppose:

        a = 10
        b = 20


STEP 1:
-------

Store the original value of `a` inside `temp`.

        temp = 10

Now:

        a    = 10
        b    = 20
        temp = 10


STEP 2:
-------

Move the value of `b` into `a`.

        a = 20

Now:

        a    = 20
        b    = 20
        temp = 10


STEP 3:
-------

Move the original value of `a`, which we safely stored
inside `temp`, into `b`.

        b = 10

Final:

        a = 20
        b = 10


VISUALIZATION
-------------

Initial:

        a = 10
        b = 20
        temp = empty


        ↓


        temp = 10
        a = 10
        b = 20


        ↓


        temp = 10
        a = 20
        b = 20


        ↓


        temp = 10
        a = 20
        b = 10


The values have successfully exchanged positions.


KEY IDEA
--------

The temporary variable prevents the original value from
being lost.

This is the most straightforward way to understand swapping.


SPACE COMPLEXITY
----------------

We introduced one additional variable:

        temp

Therefore:

        Space Complexity = O(1)

This is still constant space because the amount of extra
memory does not grow with the input values.


TIME COMPLEXITY
---------------

Only a fixed number of assignments are performed.

Therefore:

        Time Complexity = O(1)


============================================================
APPROACH 2: WITHOUT A THIRD VARIABLE
          USING ARITHMETIC OPERATIONS
============================================================

Now we ask:

    "Can we swap the values without creating another
     variable?"


We can do this using arithmetic operations.

The basic idea is to temporarily combine the two values
using addition.


Suppose:

        a = 10
        b = 20


STEP 1:
-------

Add both values and store the result in `a`.

        a = a + b

Therefore:

        a = 10 + 20
        a = 30

Now:

        a = 30
        b = 20


Notice something important:

The value `30` contains enough information to recover
both original values.

Because:

        30 = 10 + 20


STEP 2:
-------

We want to recover the original value of `a`.

The original value of `a` was 10.

We currently have:

        a = 30
        b = 20

So:

        30 - 20 = 10

Therefore, subtract `b` from `a` and store the result in `b`.

Now:

        b = 10


We have recovered the original value of `a`.


STEP 3:
-------

Now:

        a = 30
        b = 10

We want the original value of `b`, which was 20.

Again use subtraction:

        30 - 10 = 20

Therefore:

        a = 20


Final:

        a = 20
        b = 10


THE COMPLETE LOGIC
------------------

Starting values:

        a = 10
        b = 20


After addition:

        a = 30
        b = 20


After first subtraction:

        a = 30
        b = 10


After second subtraction:

        a = 20
        b = 10


The values are swapped without using a third variable.


IMPORTANT IDEA
--------------

We temporarily combine both values into one variable
using addition.

Then we use subtraction to recover the original values.


ADVANTAGE
---------

No third variable is required.

        Extra Space = O(1)


TIME COMPLEXITY
---------------

Only a fixed number of arithmetic operations are performed.

        Time Complexity = O(1)


IMPORTANT LIMITATION
--------------------

This arithmetic technique can cause an integer overflow
in languages with fixed-size integer types when the values
of `a` and `b` are very large.

For example, if the maximum integer value is limited and:

        a + b

exceeds that limit, the calculation may overflow.

Therefore, although this technique is mathematically
interesting, it is not always the safest practical approach.


============================================================
APPROACH 3: WITHOUT A THIRD VARIABLE
          USING BITWISE XOR
============================================================

Now we can solve the same problem using a completely
different idea: XOR.


FIRST: WHAT IS XOR?
-------------------

XOR is a bitwise operation.

The symbol is:

        ^


XOR works on binary bits.

Its basic rules are:

        0 XOR 0 = 0
        0 XOR 1 = 1
        1 XOR 0 = 1
        1 XOR 1 = 0


The most important property for swapping is:

        x XOR x = 0

and:

        x XOR 0 = x


Another important property is:

        XOR is reversible.


WHY DOES THIS HELP WITH SWAPPING?
---------------------------------

Suppose:

        a = A
        b = B

We perform:

        a = A XOR B


Now `a` contains information about both A and B.


Next:

        b = a XOR b

Substitute the values:

        b = (A XOR B) XOR B

Because:

        B XOR B = 0

we get:

        b = A XOR 0

Therefore:

        b = A


So `b` now contains the original value of `a`.


Now:

        a = a XOR b

We know:

        a = A XOR B
        b = A

Therefore:

        a = (A XOR B) XOR A

Since:

        A XOR A = 0

we get:

        a = B


Therefore:

        a = B
        b = A


The values have been swapped.


============================================================
XOR SWAP EXAMPLE
============================================================

Suppose:

        a = 10
        b = 20


Binary representation:

        10 = 1010
        20 = 10100


The XOR operations manipulate these bits so that the
original values can be recovered without using a third
variable.


The important thing is not to memorize the three statements.

Understand WHY they work:

        XOR can combine information
        ↓
        XOR can cancel identical information
        ↓
        Original values can be recovered
        ↓
        Values are exchanged


TIME COMPLEXITY
---------------

A fixed number of XOR operations are performed.

Therefore:

        Time Complexity = O(1)


SPACE COMPLEXITY
----------------

No additional variable is required.

Therefore:

        Space Complexity = O(1)


IMPORTANT PRACTICAL NOTE
------------------------

XOR swapping is useful for understanding bit manipulation,
but it is usually NOT the preferred way to write a swap
in modern Python.

Its main value in DSA is understanding:

    • Binary representation
    • Bitwise operators
    • XOR properties
    • Reversible transformations


============================================================
APPROACH 4: PYTHON'S BUILT-IN SWAPPING
============================================================

Python provides a much cleaner way to swap values.

Python allows multiple assignment / tuple unpacking.

Conceptually:

        a, b = b, a


This means:

        Take the value of b
        and assign it to a

        Take the value of a
        and assign it to b


Suppose:

        a = 10
        b = 20


After:

        a, b = b, a


we get:

        a = 20
        b = 10


No temporary variable needs to be explicitly created.


WHY IS THIS IMPORTANT?
----------------------

This is one of Python's strengths.

The language provides a concise way to express a common
operation safely and clearly.


TIME COMPLEXITY
---------------

        O(1)


SPACE COMPLEXITY
----------------

Conceptually, Python handles the multiple assignment
internally.

For algorithmic analysis of the swap operation:

        O(1) auxiliary space


============================================================
APPROACH COMPARISON
============================================================

Approach                         Time       Space
---------------------------------------------------------
Third variable                   O(1)       O(1)
Arithmetic operations            O(1)       O(1)
Bitwise XOR                      O(1)       O(1)
Python tuple unpacking           O(1)       O(1)


============================================================
WHICH APPROACH SHOULD YOU USE?
============================================================

For learning:

    1. Third variable
       ↓
       Understand the fundamental idea of swapping.

    2. Arithmetic approach
       ↓
       Understand how values can be manipulated mathematically.

    3. XOR approach
       ↓
       Understand bitwise operations and XOR properties.

    4. Python tuple unpacking
       ↓
       Learn the clean, idiomatic Python solution.


For normal Python programming:

        Prefer tuple unpacking.


============================================================
EDGE CASES
============================================================

Always think about what happens in different situations.


CASE 1: POSITIVE NUMBERS

        a = 10
        b = 20

Result:

        a = 20
        b = 10


CASE 2: ZERO

        a = 20
        b = 0

Result:

        a = 0
        b = 20


CASE 3: BOTH VALUES ARE THE SAME

        a = 10
        b = 10

Result:

        a = 10
        b = 10

Nothing appears to change because both values are identical.


CASE 4: NEGATIVE NUMBERS

        a = -10
        b = 20

Result:

        a = 20
        b = -10


CASE 5: BOTH ARE NEGATIVE

        a = -10
        b = -20

Result:

        a = -20
        b = -10


============================================================
KEY DSA LESSON
============================================================

This problem teaches a fundamental programming concept:

                    VARIABLE STATE

A variable is a named location/reference holding a value.

Swapping means changing which value is associated with
each variable.

The main challenge is:

    "How do we move the values without losing one of them?"


The evolution of the solution is:

        Third variable
              ↓
        Arithmetic manipulation
              ↓
        Bitwise XOR
              ↓
        Language-level abstraction


This is an important pattern in programming:

        Understand the low-level mechanism
                    ↓
        Understand the mathematical/bitwise trick
                    ↓
        Use the clean abstraction provided by the language


============================================================
FINAL TAKEAWAY
============================================================

SWAP means:

        Before:
            a = A
            b = B

        After:
            a = B
            b = A


The fundamental problem is preventing the original values
from being lost.

The simplest conceptual solution uses a temporary variable.

Arithmetic and XOR demonstrate how the same result can be
achieved without explicitly using a third variable.

Python provides tuple unpacking, which makes the operation
simple and readable.

All approaches perform a constant number of operations:

        Time = O(1)

The important lesson is not just how to swap two numbers.

The important lesson is learning to think about:

        • Variable state
        • Data movement
        • Temporary storage
        • Arithmetic relationships
        • Binary representation
        • XOR properties
        • Space complexity
        • Language-level abstractions

============================================================
"""

# 1.Approach Using a Third Variable


#code

a=30
b=40
temp=a
a=b
b=temp
print(a,b)


# 2.Approach Without a Third Variable – Using Arithmetic Operations
#code
a = 10
b = 20

#swap two numbers using arithmetic operators
a = a + b
b = a - b
a = a - b

print(a, b)


#3. Approach Without a Third Variable – Using Bitwise XOR
a=10
b=20
a=a^b
b=a^b
a=a^b
print(a,b)
#4Approach Using Built-in Swap Methods
def swap(a,b):
    return b, a
a=10
b=20
a,b=swap(a,b)
print(a,b)

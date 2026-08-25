'''REMOVE DUPLICATES FROM SORTED ARRAY
-----------------------------------

Problem:
Given a SORTED array, remove duplicates so that
distinct elements come first.

Example:
[1, 2, 2, 3, 4, 4, 5]
→ [1, 2, 3, 4, 5]

IMPORTANT:
Array is already SORTED, so duplicates are adjacent.


BEST APPROACH: TWO POINTER
--------------------------

Use two pointers:

i → position of last unique element
j → scans the array

Logic:

• Start i = 0
• Move j from 1 to end
• If arr[j] != arr[i]:
    → move i forward
    → put arr[j] at arr[i]
• Return i + 1


Example:

[1, 2, 2, 3, 4, 4, 5]

 i
 ↓
[1, 2, 2, 3, 4, 4, 5]
    j

2 != 1 → keep 2

Next 2 == 2 → skip

3 != 2 → keep 3

4 != 3 → keep 4

Next 4 == 4 → skip

5 != 4 → keep 5

Result:

[1, 2, 3, 4, 5]


COMPLEXITY
-----------

Time  → O(n)
Space → O(1)


REMEMBER
---------

SORTED ARRAY
     ↓
Duplicates are together
     ↓
TWO POINTER
     ↓
Keep only different elements'''


#
def RemoveDuplicates(arr):
    seen=set()
    i=0
    for j in range(len(arr)):
        if arr[j] not  in  seen:
            seen.add(arr[j])
            arr[i]=arr[j]
            i+=1
    return sorted(seen)
arr=list(map(int,input("enter an array: ").split()))
print(RemoveDuplicates(arr))



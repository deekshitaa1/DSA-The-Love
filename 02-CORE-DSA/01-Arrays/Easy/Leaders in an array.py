# LEADERS IN AN ARRAY
'''

A Leader is an element greater than or equal to
all elements on its right.

Rightmost element is always a Leader.

Example:
[16, 17, 4, 3, 5, 2]

Leaders → [17, 5, 2]

Logic:
• Traverse from RIGHT → LEFT
• Keep track of maximum
• If current >= maximum → Leader
• Update maximum

Time  : O(n)
Space : O(n) for result

Remember:
RIGHT → LEFT → MAX → LEADER'''

# [Naive Approach] Using Nested Loops - O(n^2) Time and O(1) Space:

def LeadersOfArray(arr):
    res=[]
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]<arr[j]:
                break
        else:
            res.append(arr[i])


    return res
arr=list(map(int,input("enter an an array: ").split()))
print(LeadersOfArray(arr))


#[Expected Approach] Using Suffix Maximum - O(n) Time and O(1) Space:

'''The idea is to scan all the elements from right to left in an array and keep track of the maximum till now.'''

def Leaders(arr):
    result=[]
    n=len(arr)
    maxright=arr[-1]
    result.append(maxright)
    for i in range(n-2,-1,-1):
        if arr[i]>=maxright:
            maxright=arr[i]
            result.append(maxright)
    result.reverse()
    return result
arr = [16, 17, 4, 3, 5, 2]
print(Leaders(arr))

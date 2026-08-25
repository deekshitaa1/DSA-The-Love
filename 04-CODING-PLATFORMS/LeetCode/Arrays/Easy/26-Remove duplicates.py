#REMOVE DUPLICATES FROM SORTED ARRAY
'''
Given a sorted array, remove duplicate elements in-place.
Each unique element should appear only once.
Keep the unique elements in their original sorted order.
Return the number of unique elements, k.
The first k positions must contain the unique elements.

Example:
[1,1,2,2,3] → [1,2,3], k = 3'''

#1 2 3 3 4-> 1 2 3 4
# 1 1 2->1 2
# 0 0 1 1 1 2 2 3 3 4->  output=5->0 1 2 3 4


def removeDuplicate(arr):
    k=1

    for j in range(1,len(arr)):
        if arr[j]!=arr[j-1]:
            arr[k]=arr[j]

            k+=1
    return k
arr=list(map(int,input("enter an array: ").split()))

print(removeDuplicate(arr))

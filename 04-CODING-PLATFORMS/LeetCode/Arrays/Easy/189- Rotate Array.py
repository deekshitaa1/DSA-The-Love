# 189. Rotate Array
'''Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
'''
# approach
'''1)reverse the whole array
2)reverse from k before element and after'''
# code
'''def RotateArray(arr,k):
    n=len(arr)
    k=k%n
    arr.reverse()
    arr[:k]=reversed(arr[:k])

    arr[k:]=reversed(arr[k:])
    return arr
arr=list(map(int,input("enter an array: ").split()))
k=int(input("enter k: "))
print(RotateArray(arr,k))
'''

'''TWO SUM
--------

Problem:
Find two numbers whose sum = target and return
their indices.

Example:
[2, 7, 11, 15], target = 9

Output:
[0, 1]

BEST: HASH MAP

Logic:
• Store number → index
• For each number:
  complement = target - number
• If complement exists → return both indices
• Otherwise store current number

Time  → O(n)
Space → O(n)

Remember:
TARGET - [CURRENT = COMPLEMENT
'''

# HASH MAP[OPTIMIZED]
def TwoSum(arr,target):
    seen={}
    for i , num in enumerate(arr):
        complement=target -num
        if complement in seen:
            return[seen[complement],i]
        seen[num]=i
arr=list(map(int,input("enter an array: ").split()))
target=int(input("enter an number: "))
print(TwoSum(arr,target))

#Brute Force
def TwoSumNumber(arr,target):
    for  i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                return [i,j]

arr=list(map(int,input("enter an array: ").split()))
target=int(input("enter an array: "))
print(TwoSumNumber(arr,target))


# return numbers
def TwoSumNum(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                return [arr[i],arr[j]]
arr=list(map(int,input("enter an array: ").split()))
target=int(input("enter an number: "))
print(TwoSumNum(arr,target))

# All number return
def Twosum(arr,target):

    res=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                res.append([arr[i],arr[j]])
    return res
arr=list(map(int,input("enter an array: ").split()))
target=int(input("enter an number: "))
print(Twosum(arr,target))

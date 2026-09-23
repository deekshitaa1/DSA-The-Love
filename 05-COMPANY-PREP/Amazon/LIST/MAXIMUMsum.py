def maximumSum(nums):
    n=len(nums)
    total=0
    maximum=float('-inf')
    for i in range(0,n):
        total=total+nums[i]
        maximum=max(maximum,total)
        if total<0:
            total=0
    return maximum
nums=list(map(int,input("enter an array: ").split()))
print(maximumSum(nums))


def maximumsub_Array(arr):
    n=len(arr)
    total=0
    maxi=float('-inf')

    for i in range(0,n):
        total=total+nums[i]
        maximum=max(total,maximum)

        if total<0:
            total=0
    return maxi
arr=list(map(int,input("enter an array: ").split()))
print(maximumsub_Array(arr))


#time complexity=o(n)
#space complexity=o(1)

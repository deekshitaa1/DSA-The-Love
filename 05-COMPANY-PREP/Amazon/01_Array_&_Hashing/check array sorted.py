def array_sorted(nums):
    n=len(nums)
    for i in range(0,n-1):
        if nums[i]>nums[i+1]:
            return False
    return True
nums=list(map(int,input("enter an array: ").split()))
print(array_sorted(nums))

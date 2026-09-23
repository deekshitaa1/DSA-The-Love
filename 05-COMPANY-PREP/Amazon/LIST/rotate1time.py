#rotate 1 place
def rotate_1(nums):
    n=len(nums)
    temp=nums[n-1]
    for i in range(n-2,-1,-1):
        nums[i+1]=nums[i]
    nums[0]=temp
    return nums
nums=list(map(int,input("enter an array:  ").split()))
print(rotate_1(nums))
#time complexity=o(n)
#space complexity=o(1)

#return index of target number
def linearsearch(nums,target):
    n=len(nums)
    for i in range(0,n):
        if nums[i]==target:
            return i
    return -1
nums=list(map(int,input("enter an array: ").split()))
target=(int(input("enter an array: ")))
print(linearsearch(nums,target))

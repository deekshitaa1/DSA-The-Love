def rearrange(nums):
    n=len(nums)
    result=[0]*n
    pos_index,neg_index=0,1
    for i in range(0,n):
        if nums[i]>=0:
            result[pos_index]=nums[i]
            pos_index+=2
        else:
            result[neg_index]=nums[i]
            neg_index+=2

    return result
nums=[5,20,-3,-1,-10,6]
print(rearrange(nums))

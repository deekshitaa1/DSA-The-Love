def movezeroes(nums):
    if len(nums)==1:
        return nums
    i=0

    while i<len(nums):
        if nums[i]==0:
            break
        i+=1
        if i==len(nums):
            return nums
        j=i+1

        while j<len(nums):
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            j+=1
    return nums
nums=list(map(int,input("enter an array ").split()))
print(movezeroes(nums))

#time complexity =o(n)
#space complexity =0(1)

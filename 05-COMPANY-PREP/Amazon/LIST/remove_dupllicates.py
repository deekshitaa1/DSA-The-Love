#remove duplicates
'''def remove_Duplicates(arr):

    unique=[]
    for num in arr:
        if num not in unique:
            unique.append(num)

    return unique
arr=list(map(int,input("enter an array: ").split()))
print(remove_Duplicates(arr))
'''
#get only unique
def unique_num(nums):
    freq={}
    unique=[]
    for num in nums:
        if num not in freq:

            freq[num]=1
            unique.append(num)

    return unique
nums=list(map(int,input("enter an array: ").split()))
print(unique_num(nums))

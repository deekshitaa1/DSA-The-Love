# contains Duplicate
'''Given an interger array  if num occur appear at least two time return RETURN true else return false if values are distict
exxample:
[1,2,3,4]=false
[1,1,2,2,3,4,5]
'''
#
def ContainsDuplicate(arr):
    freq={}
    for num in arr:
        if num  in freq:
            freq[num]+=1
        else:

            freq[num]=1

    for num in freq:
        if freq[num]>1:

            return True
    return False
arr=list(map(int,input("enter an array: ").split()))

print(ContainsDuplicate(arr))

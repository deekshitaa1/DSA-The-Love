# SINGLE NUMBER
'''Given a non empty interfers array.every element appears twice excpcet for one find that array.'''

#
def SingleNumer(nums):
    freq={}
    for num in nums:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1
    single=[]
    for num in freq:
        if freq[num]==1:
            single.append(num)
    return single
nums=list(map(int,input("enter an array: ").split()))
print(SingleNumer(nums))

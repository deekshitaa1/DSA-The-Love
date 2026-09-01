# 350-Intersection of two Arrays
'''
'''

#

def intersect(nums1,nums2):
    freq={}
    result=[]
    for num in nums1:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1
    for num in nums2:
        if num in freq and freq[num]>0:
            result.append(num)
            freq[num]-=1
    return result
nums1=list(map(int,input("enter an array: ").split()))
nums2=list(map(int,input("enter an array: ").split()))
print(intersect(nums1,nums2))

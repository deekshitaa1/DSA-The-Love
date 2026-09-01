#Intersection of two numbers
'''Given Two intergers array nums1 and nums2 return an array pf their intersection .each element in the result must be unique and you may return in any order '''

#code

from sqlalchemy import intersect


def IntersectionTwoArrays(nums1,nums2):
    intersect=[]
    for val in nums1:
        if val in nums2:
            intersect.append(val)

    return intersect
nums1=list(map(int,input("enter an array: ").split()))
nums2=list(map(int,input("enter an array: ").split()))
print(IntersectionTwoArrays(nums1,nums2))

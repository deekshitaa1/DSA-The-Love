#
'''from math import *
def Countdigits(n):
    return int(log10(n)+1)
n=int(input(": "))
print(Countdigits(n))
'''
#
def countdigits(n):
    n=abs(n)
    if n==0:
        return 1
    count=0
    while n>0:
        count+=1
        n=n//10
    return count
n=int(input(": "))
print(countdigits(n))

'''import math
def PrimeNumber(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i==0:
            return False
    return True
n=int(input("enter an number: "))
print(PrimeNumber(n))'''
from sympy import false
import math

def prime_number(num):
    if num<=0:
        return False
    if num==2:
        return True
    if num%2==0:
        return False
    for i in range(3,int(math.sqrt(num))+1,2):
        if num%i==0:
            return False
    return True
num=int(input("enter an number: "))
print(prime_number(num))

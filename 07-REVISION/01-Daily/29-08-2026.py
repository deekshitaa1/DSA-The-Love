#Array
#CHECK EVEN OR ODD
def isEven(num):
    if num%2==0:
        return f" {num} is even number."
    return  f" {num} is not even number."
num=int(input("enter an number: "))
print(isEven(num))

#multiplication table
def multiplicationTable(n,i=1):
    if i ==11:
        return
    print(n,"*",i ,"=", n*i)
    multiplicationTable(n,i+1)
n=int(input("enter an  number: "))
multiplicationTable(n,i=1)
#sum of natural numbers
def SumOfNum(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum
n=int(input("enter an number: "))
print(SumOfNum(n))
#sum of square
def SumOfsquares(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i**2
    return sum
n=int(input("enter an num : "))
print(SumOfsquares(n))
#swap two numbers


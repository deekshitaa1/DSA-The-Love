def F(n):
    if n<=1:
        return n
    else:
        return F(n-1)+F(n-2)
n=int(input("enter an number: "))
print(F(n))

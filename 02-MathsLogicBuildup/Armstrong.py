def Armstrong(n):
    if n<0:
        return False
    count=len(str(n))
    orginal=n
    Result=0
    while n>0:
        digits=n%10
        result=result+(digits**count)
        n=n//10
        

    if result==orginal:
        return True

    return False
n=int(input("enter an number: "))
print(Armstrong(n))

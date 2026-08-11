def DivisorNumber(n):
    n=abs(n)
    seen=set()
    for i in range(1,n+1):
        if n%i==0 :
            seen.add(i)
    return seen
n=int(input(": "))
print(DivisorNumber(n))

def ReverseNumber(n):
    n=abs(n)
    while n>=10:
        reverse=0


        while n>0:
            digits=n%10
            reverse=reverse*10+digits
            n=n//10
        return reverse

n=int(input(": "))
print(ReverseNumber(n))

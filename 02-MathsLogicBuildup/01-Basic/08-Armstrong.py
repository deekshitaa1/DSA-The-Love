from re import A


def ArmStrongNumber(n):
    count=len(str(n))
    orginal=n
    result=0
    while n>0:
        digits=n%10
        result=result+digits**count
        n=n//10
    if result==orginal:
        return f" {orginal} is an armstrong number."
    return f"{orginal} not an armstrong number."
n=int(input("enter an number: "))
print(ArmStrongNumber(n))

def palindrome(n):
    
    orginal=n
    palindrome=0
    if n<0:
        return False
    while n>0:
        digits=n%10
        palindrome=palindrome*10+digits
        n=n//10
    if palindrome==orginal:
        return True
    return False
n=int(input("enter an number: "))
print(palindrome(n))

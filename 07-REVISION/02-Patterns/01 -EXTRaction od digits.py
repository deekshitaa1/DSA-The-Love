# count digits
'''def count_digits(num):
    count=0
    while num>0:
        count+=1
        num=num//10
    return count
num =int(input("enter an array: "))
print(count_digits(num))'''
#reverse a number
'''def reverse_number(num):
    n=num
    if n <0:
        sign=-1

    n=abs(n)
    reverse=0
    while n>0:
        digits=n%10
        reverse=(reverse*10)+digits
        n=n//10
    return sign*reverse
n=int(input("enter an number=  "))
print(reverse_number(n))

'''

#check palindrome or not
#1 sting
'''def palindrome_string(s):

    str=len(s)
    i=0
    j=str-1



    while i<j:
        if s[i]!=s[j]:
            return f"not an palindrome."


        i+=1
        j-=1
    return f"is an palindrome."
s=input("enter an word:  ")
print(palindrome_string(s))'''
#palindrome number
'''def palindrome_number(n):
    orginal=n
    pal=0
    while n>0:
        digits=n%10
        pal=(pal*10)+digits
        n=n//10

    if pal==orginal:
        return f"{orginal} is an palindrome number."
    else:
        return f"{orginal} not an palindrome number."

n=int(input("enter an number= "))
print(palindrome_number(n))'''

#reverse an string

def reverse_String(str):
    s=len(str)
    i=0
    j=s-1
    S=list(str)
    while i<j:
        S[i],S[j]=S[j],S[i]

        i+=1
        j-=1


    return  "".join(S)
str="deekshita"
print(reverse_String(str))

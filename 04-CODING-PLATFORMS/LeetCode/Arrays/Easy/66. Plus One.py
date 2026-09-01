# 66- PLUS ONE

'''START FROM LEFT-> IF DIGITS<9-> ADD ONE DONE-> IF DIGITS==9->MAKE IT O-> CARRY GOES TO FIRST'''
#
def PlusOne(digits):
    for i in range(len(digits)-1,-1,-1):
        if digits[i]<9:
            digits[i]+=1
            return  digits
        digits[i]=0
    return [1]+digits
digits=list(map(int,input("enter an array: ").split()))
print(PlusOne(digits))

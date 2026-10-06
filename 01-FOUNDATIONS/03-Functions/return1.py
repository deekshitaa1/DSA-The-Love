def addition(num1,num2):
    total=num1+num2
    return total

print(addition(1,2))


# ask 2 numbers from user calculate  total of  two number then print  if the sum is odd or even

def sum_evenodd(num1,num2):
    total=num1+num2

    if total%2==0:
        return f"even number"
    else:
        return f" is odd number"
num1=12
num2=12
print(sum_evenodd(num1,num2))

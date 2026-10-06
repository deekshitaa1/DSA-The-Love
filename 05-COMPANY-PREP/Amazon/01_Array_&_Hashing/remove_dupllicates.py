#remove duplicates
'''def remove_Duplicates(arr):

    unique=[]
    for num in arr:
        if num not in unique:
            unique.append(num)

    return unique
arr=list(map(int,input("enter an array: ").split()))
print(remove_Duplicates(arr))
'''
#get only unique
def unique_num(nums):
    freq={}
    unique=[]
    for num in nums:
        if num not in freq:

            freq[num]=1
            unique.append(num)

    return unique
nums=list(map(int,input("enter an array: ").split()))
print(unique_num(nums))

#

def unique_number(nums):
    if not nums:
        return None
    freq={}
    unique=[]
    for num in nums:
        if num  in freq:
            freq[num]+=1
            unique.append(num)

            if not unique:
                return None
    return unique
while True:
    user_input=input("enter an input: ")
    if user_input.lower()=='exit':
        print("Good bye!")
        break
    if not user_input.strip():
        print("please enter valid input")
        continue

    try:
        nums=list(map(int,user_input.split()))
        print(unique_number(nums))

    except ValueError:
        print("Invalid input! enter an valid input")

from multiprocessing import Value

from sympy import use
'''

def two_sum(nums,target):
    if not nums:
        return None
    seen={}
    for i in range(len(nums)):
        needed=target-nums[i]

        if needed in seen:
            return [seen[needed],i]



        seen[nums[i]]=i


while True:
    user_input=input("enter an input: ")
    if user_input.lower()=='exit':
        break

    if not user_input.strip():
        print("please enter input! ")
        continue

    try:
        nums=list(map(int,user_input.split()))
        target=int(input())
        print(two_sum(nums,target))
    except ValueError:
        print("Invalid input! enter valid input ")'''
 #
'''
def two_sums(nums,target):
    if not nums:
        return None
    seen={}

    for i in range(len(nums)):
        needed=target-nums[i]

        if needed in seen:
            return [seen[needed],i]

        seen[nums[i]]=i
while True:
    user_input=input("enter an input: ")
    if user_input.lower()=='exit':
        break

    if not  user_input.strip():
        print("please enter input: ")

        continue

    try:
        nums=list(map(int,user_input.split()))
        target=int(input("enter target: "))
        print(two_sums(nums,target))

    except ValueError:
        print("Invalid input! enter valid input.")

'''
# two sum
def two_summ(nums,target):
    if not nums:
        return None
    seen={}

    for i,num in enumerate(nums):
        needed=target-nums[i]

        if needed in seen:
            return [seen[needed],i]

        seen[nums[i]]=i
while True:
    user_input=input("enter an  input: ")
    if user_input.lower()=='exit':
        print("Good Bye")
        break
    if not user_input.strip():
        print("please enter input!")
        continue


    try:
        nums=list(map(int,user_input.split()))
        target=int(input("enter an target: "))
        print(two_summ(nums, target ))


    except ValueError:
        print("Invalid Input!,Enter valid input")

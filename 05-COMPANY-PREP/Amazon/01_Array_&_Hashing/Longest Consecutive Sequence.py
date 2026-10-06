# find the length of the longest consecutive sequence
from regex import T
from sympy import use


def longest_consecutive(nums):

    if not nums:
        return None
    num_set=set(nums)
    longest_streak=0
    for num in num_set:
        if num-1 not in num_set:
            current=num
            current_streak=1

        while current+1 in num_set:

            current+=1
            current_streak+=1
        longest_streak=max(longest_streak,current_streak)
    return longest_streak
while True:
    user_input=input("enter an input: ")
    if  user_input.lower()=='exit':
        print("Good bye !")
        break

    if not user_input.strip():
        print("please enter input!")
        continue


    try:
        nums=list(map(int,user_input.split()))
        print(longest_consecutive(nums))

    except ValueError:
        print("Invalid input! enter an valid input")
#


def longest_consecutives(nums):
    if not nums:
        return None
    num_set=set(nums)
    longest_streak=0
    for num in num_set:
        if num-1 not in num_set:
            current_num=num
            current_streak=1

            while current_num+1 in num_set:
                current_num+=1
                current_streak+=1
            longest_streak=max(current_streak,longest_streak)
    return longest_streak
while True:
    user_input=input("enter an input : ")
    if user_input.lower()=='exit':
        print('Good Bye!')
        break

    if not user_input.strip():
        print("please enter input")
        continue
    try:
        nums=list(map(int,user_input.split()))
        print("longest streak: \t",longest_consecutives(nums))

    except ValueError:
        print("Invalid input! enter valid input.")

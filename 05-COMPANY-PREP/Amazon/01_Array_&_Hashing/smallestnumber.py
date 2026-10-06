#time complexity= The work grows with the input. o(n)

#space complexity= num is upfdtaing num taking  only one o(1)



def smallest_number(nums):
    if not nums:
        return None
    smallest=float('inf')

    for i in range(len(nums)):
        if nums[i]==nums[i+1]:
            return f"all numbers are equl so there is no small number"
    for num in nums:

        if num<smallest:
            smallest=num

            if smallest==float('inf'):
                return None


    return smallest
while True:
    user_input=input("enter an array: ")
    if user_input.lower()=='exit':
        break
    if not user_input.strip():
        print("please put the input to continue. ")
        continue

    try:
        nums=list(map(int,user_input.split()))
        result=smallest_number(nums)
        print("The smallest number is: {smallest}")
    except ValueError:
        print("Invalid input! please enter numbers only.")


def smallest_num(nums):
    if not nums:
        return None
    seen={}
    smallest=float('inf')
    for num in nums:
        if num<smallest:
            smallest=num

            if smallest==float('inf'):
                return None


    return smallest

while True:
    user_input=input("enter an input: ")
    if user_input.lower()=='exit':
        print("Good bye!")
        break
    if not user_input.strip():
        print("please enter input!")
        continue

    try:
        nums=list(map(int,user_input.split()))

        print(smallest_num(nums))
    except ValueError:
        print("Invalid input!...Enter valid input")

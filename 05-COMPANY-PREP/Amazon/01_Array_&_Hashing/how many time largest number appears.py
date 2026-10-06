def largest_number(nums):
    count=0
    largest=float('-inf')
    for num in nums:
        if num>largest:
            largest=num
            count=1 #3  9 3 9 4

        elif num==largest:
            count+=1

    return count
while True:
    user_input=input("enter an array: ")
    if user_input.lower()=="exit":
        break

    nums=list(map(int,user_input.split()))
    print(largest_number(nums))


#
def count_largest(nums):
    if not nums:
        return None
    largest=float('-inf')
    count=0
    for num in nums:
        if num>largest:
            largest=num
            count=1
        elif num==largest:
            count+=1
    return count
while True:
    user_input=input("enter an array: ")
    if user_input.lower()=='exit':
        break

    if not user_input.strip():
        print("enter value to continue please ")
        continue
    try:
        nums=list(map(int,user_input.split()))
        result=count_largest(nums)
        print(f"the total count of largest number is {result}")
    except ValueError:
        print("invalid input! enter valid input: ")
#tc=o(n)
#sc=o(1)

def maximumSum(nums):
    n=len(nums)
    total=0
    maximum=float('-inf')
    for i in range(0,n):
        total=total+nums[i]
        maximum=max(maximum,total)
        if total<0:
            total=0
    return maximum
nums=list(map(int,input("enter an array: ").split()))
print(maximumSum(nums))


def maximumsub_Array(arr):
    n=len(arr)
    total=0
    maxi=float('-inf')

    for i in range(0,n):
        total=total+nums[i]
        maximum=max(total,maximum)

        if total<0:
            total=0
    return maxi
arr=list(map(int,input("enter an array: ").split()))
print(maximumsub_Array(arr))


#time complexity=o(n)
#space complexity=o(1)

def maximum_sub(nums):
    if not nums:
        return None
    total=0





    maximum=float('-inf')

    for num in nums:


        total=total+num

        maximum=max(total,maximum)
        if nums==float('-inf'):
            return None

        if total<0:
            return 0

    return maximum
while True:
    user_input=input("enter an input: ")
    if user_input.lower()=='exit':
        print("Good bye!")
        break
    if not user_input.strip():
        print("Please enter an input!")
        continue
    try:
        numa=list(map(int,user_input.split()))
        print(maximum_sub(nums))
    except ValueError:
        print("Invalid input! enter valid input")

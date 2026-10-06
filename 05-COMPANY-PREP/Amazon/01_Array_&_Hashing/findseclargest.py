# tc= o(n)
#sc=o(1)
def second_smallest(nums):
    if nums is None:
        return None
    smallest=float('inf')
    second_smallest=float('inf')

    for num in nums:
        if num<smallest:
            second_smallest=smallest
            smallest=num
        elif num<second_smallest and num!=smallest:
            second_smallest=num
    if second_smallest==float('inf'):
                return None
    return second_smallest
while True:
    user_input=input("enter an array: ")
    if user_input.lower()=='exit':
        break

    if not user_input.strip():
        print("enter input to continue: ")
        continue

    try:
        nums=list(map(int,user_input.split()))
        print(second_smallest(nums))

    except ValueError:
        print(" invalid input! please add valid input.")

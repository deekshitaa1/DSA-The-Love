def first_nonrepeating(nums):
    if not nums:
        return None
    freq={}
    for num in nums:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1

    for num in freq:
        if freq[num]==1:
            return num
    return None
while True:
    user_input=input("enter an input: ")
    if user_input.lower()=='exit':
        break

    if not  user_input.strip():
        print("please enter an input! ")
        continue
    try:
        nums=list(map(int,user_input.split()))
        print(first_nonrepeating(nums))

    except ValueError:
        print("Invalid input! enter an corrected input.")
#
def non_repeating(nums):
    freq={}
    for num in nums:
        if num not in freq:
            freq[num]=1
        else:
            freq[num]+=1

    for num in freq:
        if freq[num]==1:
            return num
    return None

while True:
    user_input=input("enter an input: ")
    if user_input.lower()=='exit':
        break

    if not  user_input.strip():
        print("please enter an input! ")
        continue
    try:
        nums=list(map(int,user_input.split()))
        print(non_repeating(nums))

    except ValueError:
        print("Invalid input! enter an corrected input.")

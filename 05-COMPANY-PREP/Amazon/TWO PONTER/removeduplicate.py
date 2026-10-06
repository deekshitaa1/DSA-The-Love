def remove_duplicate(nums):
    if not nums:
        return None
    freq={}
    for num in nums:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1

    unique=[]
    for num in freq:
        if freq[num]==1:
            unique.append(num)
    return unique
while True:
    user_input=input("enter an input: ")
    if user_input.lower()=='exit':
        print("Good Bye!")
        break
    if not user_input.strip():
        print("please enter an input!")
        continue
    try:
        nums=list(map(int,user_input.split()))
        print(remove_duplicate(nums))
    except ValueError:
        print("Invalid input! enter valid input")

def remove_duplicates(nums):
    freq={}
    unique=[]
    for num in nums:
        if num not in freq:
            freq[num]=1
            unique.append(num)

    return unique
while True:
    user_input=input("enter an input: ")
    if user_input.lower()=='exit':
        print("Good Bye!")
        break
    if not user_input.strip():
        print("please enter an input!")
        continue
    try:
        nums=list(map(int,user_input.split()))
        print(remove_duplicates(nums))
    except ValueError:
        print("Invalid input! enter valid input")
# tc:o(n)
#sc:o(n)

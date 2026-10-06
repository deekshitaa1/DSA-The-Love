def lengthlongest(nums,target):
    if not nums:
          return None
    left=0

    sum=0
    maximum_length=0

    for  right in range(len(nums)):
        sum+=nums[right]
        while sum>target and left<=right:
                sum-=nums[left]
                left+=1

        if sum==target:
            current_length=right-left+1




            maximum_length=max(current_length,maximum_length)
    return maximum_length
while True:
    user_input=input("enter an input : ")
    if user_input.lower()=='exit':
        print("Good  Bye!")
        break

    if not user_input.strip():
        print("please enter the input")
        continue
    try:
        nums=list(map(int,user_input.split()))
        target=int(input("enter an target: "))
        print(lengthlongest(nums,target))

    except ValueError:
        print("Invalid Input! Enter valid input...")


def longestlengths(nums,target):
    left=0
    current_sum=0
    maximum_length=0

    for right in range(len(nums)):
        current_sum+=nums[right]

        while  current_sum>target and left<=right:
            current_sum-=nums[left]
            left+=1

        if current_sum==target:
            current_length=right-left+1

            maximum_length=max(maximum_length,current_length)
    return maximum_length

while True:
    user_input=input("enter an input: ")
    if user_input.lower()=='exit':
        print("Good Bye!")
        break
    if  not user_input.strip():
        print("please enter valid input!")

        continue

    try:
        nums=list(map(int,user_input.split()))
        target=int(input("enter an number: "))
        print(longestlengths(nums,target))

    except ValueError:
        print("Invalid Input!, Enter valid Input.")

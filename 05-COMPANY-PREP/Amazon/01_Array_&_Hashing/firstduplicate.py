def dupli_number(nums):

    seen=set()
    for num in nums:
        if num  in seen:
            return num



        seen.add(num)
while True:
    user_input=input("enter an array: ")
    if user_input.lower()=="exit":
        break


    nums=list(map(int,user_input.split()))
    print(dupli_number(nums))

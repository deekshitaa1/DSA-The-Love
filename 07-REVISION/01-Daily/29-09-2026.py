def largest_number(arr):
    largest= float('-inf')
    sec_largest=float('-inf')
    for num in arr:
        if num>largest:
            sec_largest=largest
            largest=num
        elif num>sec_largest and num!=largest:
            sec_largest=num
    if  sec_largest==float('-inf'):
        return None
    return sec_largest
while True:
    user_input=input("enter an array: ")
    if user_input.lower()=='exit':
        break
    arr=list(map(int,user_input.split()))
    print(largest_number(arr))

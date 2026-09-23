def sec_largest(arr):
    largest=float('-inf')
    sec_largest=float('-inf')

    for num in arr:
        if num >largest:
            sec_largest=largest
            largest=num
        elif num >sec_largest and num !=largest:
            sec_largest=num
    return sec_largest
arr=list(map(int,input("enter an array: ").split()))
print(sec_largest(arr))

def find_smallest(arr):

    minVal=float('inf')
    for i in arr:
        if i<minVal:
            minVal=i

    return f"lowest values {minVal}"
arr=list(map(int,input("enter an array: ").split()))
print(find_smallest(arr))

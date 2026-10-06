def Two_Sum(arr,target):
    seen={}
    for i , num in enumerate(arr):

        complement =target-num
        if complement in seen:
            print(seen[complement],i)
        seen[num]=i
    return None
arr=list(map(int,input("enter an array: ").split()))
target=int(input("enter an target number: "))
print(Two_Sum(arr,target))

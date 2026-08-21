# Alternate elements of an array

'''Given an array arr[], the task is to print every alternate element of the array starting from the first element.

Examples:

Input: arr[] = [10, 20, 30, 40, 50]
Output: 10 30 50
Explanation: Print the first element (10), skip the second element (20), print the third element (30), skip the fourth element(40) and print the fifth element(50).

Input: arr[] = [-5, 1, 4, 2, 12]
Output: -5 4 12'''


# Iterative Approach(BEST APROACH)
'''Time complexity: O(n)
Space complexity: O(n)'''
def getAlternatives(arr):
    res=[]

    for i in range(0,len(arr),2):
        res.append(arr[i])
    return res
if __name__ == "__main__":
    arr=list(map(int,input("enter an input: ").split()))
    res=getAlternatives(arr)
    print(" ".join(map(str,res)))


# Recursive Approach
'''Time complexity: O(n)
Space complexity: O(n)'''
def GetAlternative(arr, idx, res):
    if idx < len(arr):
        res.append(arr[idx])
        GetAlternative(arr, idx + 2, res)


def GetAlternatives(arr):
    res = []
    GetAlternative(arr, 0, res)
    return res


arr = list(map(int, input("Enter an array: ").split()))

print(GetAlternatives(arr))

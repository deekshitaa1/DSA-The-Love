# print 1 to N without loop
def helper(current,n):
    if current>n:
        return
    print(current,end=" \n")
    helper(current+1,n)

n=int(input(": "))
helper(1,n)

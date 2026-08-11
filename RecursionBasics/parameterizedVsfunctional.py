#sum of n natural number
#parametarized
def func(sum,i,n):
    if i>n:
        print(sum)
        return
    func(sum+i,i+1,n)
func(0,1,10)

#functional recursion

def sum(N):
    if N==1:
        return 1
    return N+sum(N-1)
N=int(input(": "))
print(sum(N))

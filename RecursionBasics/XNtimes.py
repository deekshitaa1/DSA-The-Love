'''def func(x,n):
    if n==0:
        return
    print(x)
    func(x,n-1)
func(15,4)
'''
#
def func(i,n):
    if i>n:
        return

    print(i)
    func(i+1,n)
func(1,8)


#when u  dont know how many input
def add(*args):
    print(sum(args))
add(1,2,3)

#
def adds(*args):
    print(args)
adds([1,2],[100,200],45,100)
#kwaargss its dictinory output: {'name': 'aniruddha', 'age': 100, 'gender': 'male'}

def adda(*args,**kwargs):
    print(kwargs)
adda(name="aniruddha",age=100,gender="male")
#
def ad(n1,n2,n3,*args,**kwargs):
    print(f"{n1= }")
    print(f"{n2= }")
    print(f"{n3= }")
    print(f"{args= }")
    print(f"{kwargs= }")
ad(5,10,15,100,300)

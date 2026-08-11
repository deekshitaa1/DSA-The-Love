# without condition which gives error cuz it maximimu recursion(996) depth excited
''''def greet():
    print("Aniruddhha")
    greet()
greet()
'''
# with condition

'''def greet(count=0):

    if count==4:
        return

    print("Hello future quadralatrioner")


    greet(count+1)


greet()'''


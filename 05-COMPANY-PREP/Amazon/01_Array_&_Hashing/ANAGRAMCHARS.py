'''def anagram(s,t):
    if len(s)!=len(t):
        return False
    count={}
    for ch in s:
        count[ch]=count.get(ch,0)+1
    for ch in t:
        count[ch]=count.get(ch,0)-1

    return all(value==0 for value in count.values())
while True:
    user_input=input("enter an words: ")
    if user_input.lower()=='exit':
        print("Good Bye!")
        break

    if not user_input.strip():
        print("please enter an input!")
        continue
    try:
        s= user_input
        t=input("Enter the second word: ")
        print(anagram(s,t))
    except ValueError:
        print("Invalid input!,  enter valid input")'''
#
import string

from tomlkit import value


def anagram(s,t):
    if not string:
        return None
    if len(s)!=len(t):
        return False
    count={}

    for ch in s:
        count[ch]=count.get(ch,0)+1
        count[ch]=count.get(ch,0)-1

    return all(value==0 for value in count.values())
while True:
    user_input=input("Enter an first input: ")
    if user_input.lower()=='exit':
        print("Good Bye!")
        break
    if not user_input.strip():
        print("please enter input!")
        continue
    try:
        s=user_input
        t=input("enter an second input: ")
        print(anagram(s,t))
    except ValueError:
        print("Invalid input! Enter an Valid input.")

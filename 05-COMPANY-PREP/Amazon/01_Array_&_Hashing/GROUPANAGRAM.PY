def GroupAnagram(words):
    group={}



    for word in words:
        count=[0]*26

        for ch in word:
            index=ord(ch)-ord('a')
            count[index]+=1

        key=tuple(count)

        if key not in group:
            group[key]=[]

        group[key].append(word)

    return list(group.values())

while True:
    user_input=input("enter an input: ")
    if user_input.lower()=='exit':
        print("Good Bye!")
        break
    if not user_input.strip():
        print("please enter input!")
        continue
    try:
        words=user_input.split()
        print(GroupAnagram(words))

    except ValueError:
        print("Invalid input! enter valid input")

def group_anagrams(words):
    if not words:
        return None
    group={}

    for word in words:
        count=[0]*26

        for ch in word:
            index=ord(ch)-ord('a')
            count[index]+=1
        key=tuple(count)
        if key not in  group:
            group[key]=[]
        group[key].append(word)
    return list(group.values())
while True:
    user_input=input("enter an input")
    if user_input.lower()=='exit':
        print("Good bye!")
        break
    if not user_input.strip():
        print("Please enter an input!")
        continue
    try:
        words=user_input.split()
        print(group_anagrams(words))
    except ValueError:
        print("Invalid input! enter valid input.")

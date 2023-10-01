
def findcount(string):
    upno=0
    lowno=0
    for i in string:
        if i.isupper():
            upno=upno+1
        elif i.islower():
            lowno=lowno+1
    print("uppercase letters= ",upno)
    print("lowercase letters= ",lowno)

str=input("enter the string:")
findcount(str)
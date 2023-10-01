string=input("enter the string: ")
vowels=['a','e','i','o','u']
vowelno=0
for i in string:
    if i in vowels:
        vowelno=vowelno+1
print("vowels= ",vowelno)
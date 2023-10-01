string=input("enter the string:")
list=[]
for i in string:
    list.append(string[i])
    for j in range(1,4):
        list.append(string[j])
        for k in range(2,4):
            list.append(string[k])
            for m in range(3,4):
                list.append(string[m])

print(list)
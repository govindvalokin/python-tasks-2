list=[]
list2=[]
for i in range(8):
    sample=input("enter the numbers: ")
    list.append(sample)
for i in list:
    if (list.index(i)%2)!=0:
        list2.append(i)
print(list2)
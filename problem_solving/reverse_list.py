list1=[1,2,3,4]
print(len(list1))
list2=[]
for i in range(len(list1)-1,-1,-1):
    list2.append(list1[i])
print(list2)
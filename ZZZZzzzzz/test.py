# string1="my name is lokeswar reddy"
# string2=""
# for i in string1:
#     if i in "aeiou":
#         continue
#     else:
#         string2 +=i
# print(string2)

# num=100
# prime_list=[]
# for i in range(num+1):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count +=1
#     if count==2:
#         prime_list.append(i)
# print(prime_list)

# list=[1,4,2,3,2,1,5,4,5,5]
# new_list=[]
# for i in list:
#     if i in new_list:
#         continue
#     else:
#         new_list.append(i)
# print(new_list)

# new_dict={}
# for i in list:
#     if i in new_dict:
#         new_dict[i] +=1
#     else:
#         new_dict[i]=1
# print(new_dict)

# list= [90,112,71,70,10,20]
# temp=""
# for i in range(len(list)):
#     for j in range(i+1,len(list)):
#         if list[i]>list[j]:
#             temp=list[i]
#             list[i]=list[j]
#             list[j]=temp
#         print(list)
# print(list)

# a=[1,2,3]
# b=[4,5,6]
# x=list(map(lambda x,y:x+y, a,b))
# print(x)


# list =[1,2,3,4,1,2,3,4]
# list.reverse()
# print(list)

# dict=dict()
# dict["1"]=1
# dict["1"]=2
# dict["1"]=2
# print(dict)

# list=[1,[2,3],4,5,6]
# print(list[1])
# list.insert(1,9)
# print(list[1])
# print(list[2])
# list2=[1,[2,3],4,5,6]
# list2[1].insert(1,(10,11))
# print(list2)
# list2[1].append(1,(12,13))
# print(list2)

# str="hello"
# print(str[5:])
# print(str[5])

print(ord("G"))
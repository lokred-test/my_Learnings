test_list = [1, 5, 3, 6, 3, 5, 6, 1]
# print(test_list[1]) #for list iteration->[]
# new_list=[]
# for i in test_list:
#     if i in new_list:
#         continue
#     else:
#         new_list.append(i) #for append
# test_list=new_list
# print(test_list)

#OR
x=set(test_list)
test_list=x
print(test_list)
####################################
dict1={
    'car':["ford","toyota","ford","toyota"],
    "brand":['mustang','ranz','mustang','ranz']
}
dict2={}
for key,value in dict1.items():
    dict2[key]=set(value)
print(dict2)  #set value
dict3={}
for key,value in dict2.items():
    dict3[key]=list(value)
print(dict3)  #list value

###symmetric Diference-remove duplicates 
set1={1,2,4,5}
set2={2,1,5,7}
rem_dup=set1.symmetric_difference(set2)
print(rem_dup)





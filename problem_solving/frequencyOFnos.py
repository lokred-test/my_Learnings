from collections import Counter
a="BANANA"
x=[1,2,3,1,4,2,8,9,4]
# count={} #dictionary
# for i in x:
#     if i in count:
#         count[i] +=1
#     else:
#         count[i]=1
# print(count)

b=Counter(a)
print(b)
y=Counter(x)
print(y)

#deleting duplicates
z=list(set(y))
print(z)
c=list(set(a))
print(c)

mylist = ["apple","banana","grap"] #
mytuple = ("apple","banana","grap")
mydict={"apple":50,"banana":25,"grap":20}
myset={"apple","banana","grap"}

#ordered or unordered
print(mylist)
print(mytuple)
print(mydict)
print(myset) #unordered(only set)

#changing value's
mylist[1]="blueberry"
print(list)
# mytuple[1]="blueberry" #TypeError 'tuple' object does not support item assignment
mydict["banana"]=35
mydict[1]=45
print(mydict)
# set[1]="blueberry" #TypeError 'set' object does not support item assignment

#Allow or not duplicates(how to add new items to DS)
mylist.append("apple")
print(mylist)
#tuple does not allow to add items directly 
x=list(mytuple)
x.append("apple")
mytuple=tuple(x)
print(mytuple)
mydict.update({"apple":40}) #does not allow dup values(and, replaces original value)
print(mydict)
myset.update({"apple"}) #does not allow dup values(and, replaces original value)
print(myset)

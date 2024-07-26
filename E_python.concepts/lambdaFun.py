
#lambda function
twice=lambda x:x*2
list1=[4,5,6]
for i in list1:
    print(twice(i))

#filterFunction
arr=[1,2,3,4,5,6,7,8,9,10]
arr2 = []
arr2 = filter(lambda x: x % 2 != 0, arr)

#MapFunction
map(lambda x: x ** 2, arr2) # Map returns the computation result to the same called seq and so No need to assign any variable to the map function
arr3=list(arr2)
print(arr3)

#Reduce function
import functools
reduceresult=functools.reduce(lambda x,y:x+y,arr3)
print(reduceresult)
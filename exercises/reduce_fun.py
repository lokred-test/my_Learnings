import functools
num = [1,2,3,4]
rt = functools.reduce(lambda x,y:x+y,num)
print(rt)
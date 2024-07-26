def length_of_lastWord(A):
    arr=A.split()
    print(arr)
    lastword=arr[-1]
    length=len(lastword)
    return length


A="hello world"
result=length_of_lastWord(A)
print(result)


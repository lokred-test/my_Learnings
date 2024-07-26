def sollution(A):
    seen=set()
    for num in A:
        if num<1 or num>len(A) or num in seen:
            return 0
        seen.add(num)
    return 1

A= [1,2,3,4,6]
print(sollution(A))
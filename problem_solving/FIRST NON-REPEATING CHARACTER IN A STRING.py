def func(A):
    count={}
    # for i in range(len(A)):
    #     if A[i] in count:
    #         count[A[i]] +=1
    #     else:
    #         count[A[i]]=1
    for i in A:
        if i in count:
            count[i] +=1
        else:
            count[i]=1
    print(count)
    for i in count:
        if count[i]==1:
            return i
A="netsetosnet"
print(func(A))

def missing(A):
    m=max(A)
    if m<1:
        return 1
    chair=[0]*m
    for i in A:
        if i>0:
            chair[i-1]=1
    print(chair)
    for i in range(len(chair)-1):
        if chair[i]==0:
            return i+1
    return i+2  #if nothing is missing then the next to max number is missing
    

A=[-5,8,-22,50,77,1,2,3,4,5,6,]
result=missing(A)
print(result)
        

def solution(A):
    m=max(A)
    if m<1:
        return 1
    # if len[A]==1:
    #     return 2 if A[0]==1 else 1
    s=[0]*m
    for i in range(len(A)):
        if A[i]>0:
            if s[A[i]-1]!=1:
                s[A[i]-1]=1
    for i in range(len(s)):
        if s[i]==0:
            return i+1
    return i+2
A=[1,10,1,2,-66,-9,3,1,2]
print(solution(A))



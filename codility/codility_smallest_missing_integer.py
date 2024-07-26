def sollution(A):
    m=max(A)  #to find max num in the list
    if m<1:
        return 1
    # if len[A]==1:
    #     return 2 if A[0] ==1 else 1
    s=[0]*m                  # creating max[A] no.ed indexed list               
    for i in range(len(A)):  #assigning 1 to their respective index's(ex: 1-oindex,5-4thIndex,...n-(n-1)thIndex)
        if A[i]>0:
            if s[A[i]-1]!=1:   
                s[A[i]-1]=1
    
    for i in range(len(s)):  #finding the first 0 value in the s list
        if s[i]==0:
            return i+1
    return i+2  

A=[1,10,1,2,-66,-9,3,1,2]
print(sollution(A))


    

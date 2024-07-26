def rotatestring(A):

    temp=A+A                          #to add the initial eliminated char at the end
    for i in range(len(A)):
        for j in range(len(A)):
            print(temp[i+j],end='')
        print()
    
    #or
    temp=""
    for i in range(len(A)):
        print(A[i:]+temp)
        temp +=A[i]

A="netset"
rotatestring(A)

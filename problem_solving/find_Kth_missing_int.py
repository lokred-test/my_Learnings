def k_int(n,k):
    s=max(n)
    chairs=[0]*s
    for i in n:
        if i>0:
            chairs[i-1]=1
        
    print(chairs)
    missings=[]
    for i in range(len(chairs)):
        if chairs[i]==0:
            missings.append(i+1)
    print(missings)
    try:
        return missings[k-1]
    except:
        print("searching number is out of range")


n=[2 ,3,-9,4,6-7,7,8,9,20]
k=2
print(k_int(n,k))
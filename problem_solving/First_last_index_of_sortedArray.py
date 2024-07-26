def first_and_last(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            start=i
            while arr[i+1]==target :
                i +=1
            return [start,i]
    return [-1,-1]
        
arr=[1,2,3,6,6,6,6,20,20,30]
target=20
print(first_and_last(arr,target))
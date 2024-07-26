def twosum(arr,sum):
    for i in range(len(arr)-2):
        for j in range(i+1,len(arr)-1):
            if arr[i]+arr[j]==sum:
                print(f"the num's are:{arr[i] } & {arr[j] }")
arr=[5,7,4,3,9,8,19,21]
sum=17
twosum(arr,sum)




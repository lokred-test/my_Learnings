arr=[63,54,98,34,89,42,18]
res=max(arr)
print(res)
res=min(arr)
print(res)
#or
min=arr[0]
for i in range(len(arr)):
    if min>arr[i]:
        min=arr[i]
print(min)
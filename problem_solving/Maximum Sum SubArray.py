def max_sum(A):
    cur_sum=0
    max_so_far=A[0]
    for i in range(len(A)-1):
        cur_sum=cur_sum+A[i]
        if cur_sum>max_so_far:
            max_so_far=cur_sum
        if cur_sum<0:
            cur_sum=0
    return max_so_far
A=[4,-3,-2,2,3,1,-2,-3,6,-6,-4,2,1]
result=max_sum(A)
print(result)

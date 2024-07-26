
num=50
prime_numbers=[]
for num in range(2,51):
    for i in range(2,num):
        if num==2:
            prime_numbers.append(num)
        elif num%i==0:
            break
    else:    
        prime_numbers.append(num)


print(prime_numbers)

#or
prime_list=[]
for i in range(2,20):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count +=1
    if count==2:
        prime_list.append(i)
print(prime_list)

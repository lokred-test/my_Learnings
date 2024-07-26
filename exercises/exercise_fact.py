# Factorial of a number using recursion

def recur_factorial(n):
   if n == 0:
       return 1
   else:
       return n*recur_factorial(n-1)

num = 5
rt=recur_factorial(num)

print(rt)
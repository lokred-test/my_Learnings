#using recurssion
def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-2)+fib(n-1)
for i in range(10):
    print(fib(i),end=" ")
print()

#using Generator function
def fib():
    a=0
    b=1
    while True:
        yield a
        c=a+b
        a=b
        b=c
a=fib()
for i in range(10):
    print(next(a),end=" ")

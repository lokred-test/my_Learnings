def fib():
    a=0
    b=1
    while True:
        yield a
        c=a+b
        a=b
        b=c
x=fib()    #in generetor concept=> the next() accepts only function variable, not any direct function
for i in range(10):
    print(next(x), end=" ")
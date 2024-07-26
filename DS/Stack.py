#stack implimentation using list DS
stack=[]
def push():
    if stack==max_limit:
        print("stack full!")
    else:
        element=int(input("enter the item"))
        stack.append(element)
def pop():
    stack.pop()   #to remove the data that is entered first(STACK)
def display():
    print(stack)

max_limit=int(input("enter the max limit for stack"))
while True:
    chioce=int(input("options:1.push,2.pop,3.display,4.exit"))
    if chioce==1:
        push()
    elif chioce==2:
        pop()
    elif chioce==3:
        display()
    elif chioce==4:
        break
    else:
        print("enter the correct chioce")

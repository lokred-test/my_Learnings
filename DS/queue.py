#queue implimentation using list DS
stack=[]
def enqueue():
    if stack==max_limit:
        print("stack full!")
    else:
        element=int(input("enter the item"))
        stack.append(element)
def dequeue():
    stack.pop(0)  #to remove the data that is entered first(QUEUE)
def display():
    print(stack)

max_limit=int(input("enter the max limit for stack"))
while True:
    chioce=int(input("options:1.push,2.pop,3.display,4.exit"))
    if chioce==1:
        enqueue()
    elif chioce==2:
        dequeue()
    elif chioce==3:
        display()
    elif chioce==4:
        break
    else:
        print("enter the correct chioce")

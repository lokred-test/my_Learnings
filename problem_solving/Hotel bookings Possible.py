def hotel_book(arrival,departure,rooms):
    event=[(a,"red")for a in arrival]+[(d,"blue")for d in departure]
    event=sorted(event)
    print(event)

    guest=0                    #for 1room=in,out,in,out(and, for 2rooms in/in,out/out)
    for e in event:
        if e[1]=='red':
            guest=guest+1
        else:
            guest =guest-1
    
        if guest>rooms:        #when guests>rooms return room not available
            return 0
    return 1                   #return room available


arrival=[1,3,5]
departure=[2,6,8]
result=hotel_book(arrival,departure,1)
print(result)
result=hotel_book(arrival,departure,2)
print(result)
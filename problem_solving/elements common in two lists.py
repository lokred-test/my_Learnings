def common(list1,list2):
    count=0
    common_elements=[]
    for i in list1:
        for j in list2:
            if i==j:
                common_elements.append(i)
                count=count+1
    print(common_elements)
    print(count)

    ###using dictiony

    # list3={}
    # common_elements=[]
    # for i in list1:
    #     list3[i]=1
    # for i in list2:
    #     if i in list3:
    #         common_elements.append(i)
    #         count=count+1
    # print(common_elements)
    # print(count)
    
        
list1=[40,50,60,80]
list2=[50,90,60,100]
common(list1,list2)

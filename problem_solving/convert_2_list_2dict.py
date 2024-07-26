
def list_to_dict(keys,values):
        my_dict=dict(zip(keys,values))
        print(my_dict)
def list_to_tuple(my_dict):
        # my_tuple=tuple(my_dict)
        # print(my_tuple)
        my_list=[]  #As we cannot add items to the tuple
        for i in my_dict.items():
                my_list.append(i)
        print(my_list)
        my_tuple=tuple(my_list)
        print(my_tuple)
                
            

keys=[1,2,3]
values=["one","two","three"]
list_to_dict(keys,values)

my_dict={1: 'one', 2: 'two', 3: 'three'}
list_to_tuple(my_dict)

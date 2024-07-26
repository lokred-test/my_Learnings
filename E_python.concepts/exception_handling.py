list=[1,2,3,4]
# list[4]  #IndexError: list index out of range
# list1[3] #NameError: name 'list1' is not defined. Did you mean: 'list'?

# 5/0        #ZeroDivisionError: division by zero

#######handlinding exception##################
# import math
# try:
#     print(math.factorial(-5))  #ValueError: factorial() not defined for negative values
# except ValueError:
#     print("-ve value for fact not defined")
# except:
#     print("some error occured")

#######Raise Exceptin###############
try:
    num=int(input("enter number"))
    100/num
    if num<=0: #In case <0,it will raise exception(in case of 0 it wont work as we handling the 0 in except block)
        raise ValueError("that is not a +ve number")
except ZeroDivisionError:  #in case of 0 except block will excute, else won't execute
    print("error")

finally:
    print("job done, bye!")


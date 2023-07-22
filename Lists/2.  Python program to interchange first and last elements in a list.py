#    2.  Python program to interchange first and last elements in a list
 

list = [10,20,30,40,50,60,70,80,90,100] 
list[0],list[-1] = list[-1],list[0]
print(list)


# using temporary functions

list = [10,20,30,40,50,60,70,80,90,100]
temp = list[0]
list[0] = list[-1]
print(list)
list[-1] = temp
print(list)

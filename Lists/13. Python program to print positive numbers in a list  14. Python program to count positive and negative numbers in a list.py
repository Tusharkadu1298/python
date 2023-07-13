# 13. Python program to print positive numbers in a list
# 14. Python program to count positive and negative numbers in a list

l =[1,-1,2,-2,3,-3,4,-4,5,-5,6,-6,7,-7,8,-8,9,-9,10,-10]
negative_num = []
positive_num = []
for i in l:
    if i >= 0:
        positive_num.append(i)
    else:
        negative_num.append(i)
print(positive_num)
print(negative_num)

# 6.  Write a python program to Count occurrences of an element in a list

a = [10,20,30,33,40,47,50,53,70,71,80,50,90,10,50,93,95,50,97,100,10,20,30,10,20,10,80,10,90,10,53,78,10,100]
print(a.count(10))




#without using count functions
a = [10,20,30,33,40,47,50,53,70,71,80,50,90,10,50,93,95,50,97,100,10,20,30,10,20,10,80,10,90,10,53,78,10,100]
count = 0
for i in a:
    if i == 10:
        count += 1
print(count)

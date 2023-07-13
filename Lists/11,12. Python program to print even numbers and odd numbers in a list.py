# 11. Python program to print even numbers in a list
# 12. Python program to print odd numbers in a List

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
num_even = []
num_odd = []
for i in l:
    if i%2 == 0:
        num_even.append(i)
    else:
        num_odd.append(i)
print(num_even)
print(num_odd)

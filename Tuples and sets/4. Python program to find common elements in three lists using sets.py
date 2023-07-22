#  4. Python program to find common elements in three lists using sets

a = [1,2,3,4,5]
b = [6,7,1,4,8]
c = [9,1,4,10]

d = (set(a)&set(b)&set(c))
print(d)

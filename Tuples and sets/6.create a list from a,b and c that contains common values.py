# 6. a = [2,3,4,5,1]
#    b = [4,8,2,5,3]
#    c = [6,8,3,5,9]
#    create a list from a,b and c that contains common values.

a = [2,3,4,5,1]
b = [4,8,2,5,3]
c = [6,8,3,5,9]
d = (list(set(a)&set(b)&set(c)))
print(d)

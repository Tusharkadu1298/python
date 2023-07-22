#   3. Check if two lists have at-least one element common

l = [1,2,3,4,5,6]
m = [7,3,8,4,9,5]
n = ((set(l)&set(m)))
print(n)

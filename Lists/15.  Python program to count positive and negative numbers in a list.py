#  15.  Python program to count positive and negative numbers in a list

a = [10,20,-30,33,40,-47,50,53,-70,71,80,50,-90,10,-50,93,95,50,-97,100,10,-20,-30,-10,-20,-10,80,10,-90,10,-53,78,-10,100]
negative = 0
positive = 0
for i in a:
    if i>0:
        positive += 1
    else:
        negative += 1
print(positive)
print(negative)

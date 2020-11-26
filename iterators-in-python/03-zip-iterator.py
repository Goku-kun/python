"""
zip() returns an iterator of two or more iterator elements. Zip is used when you'd like to iterate over two or more elements simultaneously. 
We can use the indices of these lists to iterate over them but python provides us with zip to do that for us.
"""

listA = [1, 2, 3, 4]
listB = [4, 5, 6, 7]

for left, right in zip(listA, listB):
    print(left, " is the value of list A and ", right, "is the value of list B.")

"""
If there are lists of different sizes, don't fret. Zip will use the shorter length as the length for its iterator
for ex:
"""
listC = [1, 2, 3, 4]
listD =  [3, 4, 5]

# below for loop will only execute 3 times since list D has a length of 3 and it's the shorter out of list C and list D.
for left, right in zip(listC, listD):
    print(left, "is the value of list C and", right, "is the value of the list D.")
    
"""
Any number of iterables can be zipped together. But the rule of the shortest iterator still applies
"""

for val1, val2, val3, val4 in zip(listA, listB, listC,listD):
    print(val1, val2, val3, val4)

listE = list(zip(listA, listB, listC, listD))
print(listE)


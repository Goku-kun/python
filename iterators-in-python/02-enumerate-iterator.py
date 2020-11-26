"""
Enumerate helps keep track of the index of the element in an iterator.

Although, we can do something like this:
"""
listA = [1, 2, 3, 4]

for i in range(len(listA)):
    print(i, listA[i])

"""
Python provides an easier and more cleaner way of doing this using enumerate
Both of these codes would iterate through the list and their corresponding index.
"""

for i, val in enumerate(listA):
    print(i, val)


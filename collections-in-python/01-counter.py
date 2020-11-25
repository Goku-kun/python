from collections import Counter

string = "Repeat Repeat Repeat"
counter = Counter(string)
# Counter() returns an iterator but the .most_common() method is the most used method in a counter and elements() too!
print(counter)
# returns a list of 2 most common characters in the counter
most_common = counter.most_common(2)
print(most_common)
# prints the most common available character in the counter; always returns a list
print(counter.most_common(1))

# to extract all the characters in string(repeating), use the following .elements() method.
# By default .elements() method returns an iterator which can be passed to a list() method to get a list of characters

elements = list(counter.elements())
print(elements)

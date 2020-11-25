from collections import OrderedDict
# Regular Dict but it remembers the order of the elements entered in the dictionary.
# It has become less relevant since the Dict() class also has the properties to do this since python 3.7.

ordereddict = OrderedDict()
ordereddict['a'] = 1
ordereddict['b'] = 2
ordereddict['c'] = 3
print(ordereddict)
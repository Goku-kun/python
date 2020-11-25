from collections import defaultdict

# default dict provides a default value to a previously undeclared key
# dict() would throw an error because the key-value pair wasn't declared but defaultdict() will return a default value
d = defaultdict(int) # we can even specify the type of the default value we want returned.
d['a'] = 1
d['b'] = 2

# But if we try to access 'c' which is not a declared key, it'll still return a value 0 of int type.
print(d['c'])

default = defaultdict(float)
print(default['a']) # this will return a default float value 0.0

dictionary = dict() 
# this would throw a key not found error.
print(dictionary['a'])
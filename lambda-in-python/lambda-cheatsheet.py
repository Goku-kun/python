# if we have a 2D list or tuples to sort and if we use sorted, for example,
a = [(1,2), (3,4),(-1,1), (0,100)]

sort_a = sorted(a)
print(sort_a)
# by default it sorts using the first element of the tuple. However, if we want to sort it using the second element, we can use the lambda function

sort_a_element_1 = sorted(a, key=lambda x: x[1])
# this would've sorted the list by the second element of the tuple.
print(sort_a_element_1)




# Using lambda in map and filter
# syntax map(function, sequence/iterable)
list_a = [1, 2, 3]
list_squared = list(map(lambda x: x**2, list_a))
print(list_squared)

# syntax filter(function, sequence/iterable)
list_less_than_3 = list(filter(lambda x: x<3, list_a))
print(list_less_than_3)

# map and filter are the same as ones used in JavaScript. map() maps a function to an iterator and returns it and filter() filters out a set of values based on a condition.

for val in map(lambda x: x**2, range(5)):
    print(val)

squared_numbers = list(map(lambda x: x**2, range(5)))
print(squared_numbers)

for val in filter(lambda x: x%2==0, range(10)):
    print(val)

even_numbers = list(filter(lambda x: x%2==0, range(10)))
print(even_numbers)

from itertools import product
# product computes the cartersian product of the iterators passed into it

a = [1, 2]
b = [3, 4]

prod = list(product(a,b))
print(prod)
from itertools import permutations

a = [1, 2, 3]

permutations_of_a = permutations(a)
# by default, the arguments are length p length meaning 3p3 in this case.

print(list(permutations_of_a)) # this will generate all the possible permutations of list a containing three values.

permutations_of_a_taking_2_at_a_time = permutations(a, 2)
print(list(permutations_of_a_taking_2_at_a_time)) # same as 3p2

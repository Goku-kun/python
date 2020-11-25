from itertools import combinations, combinations_with_replacement

a = [1, 2, 3]

# similar execution to the permutations

comb = combinations(a, 2) # 3C2
print(list(comb))

comb_wr = combinations_with_replacement(a, 1)
print(list(comb_wr))
from itertools import count, cycle, repeat

# count starts counting from the argument passed to it till infinity
for i in count(10):
    print(i)
    if i == 13:
        break

a = [1, 2, 3]

# cycle keeps on cycling on the sequence passed to as a argument infinitely

sum = 0
for i in cycle(a):
    print(i)
    sum += i
    if sum == 12:
        break

# repeat keeps on repeating the same number passed to it infinitely

counter = 0
for i in repeat(15):
    print(i)
    counter += 1
    if counter == 3:
        break
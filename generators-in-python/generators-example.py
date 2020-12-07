import sys
def mygenerator():
    yield 2
    yield 11
    yield 5

g = mygenerator()
print(g) # This is a generator object
for i in g:
    print(i)

for i in g:
    print(g)# This will not print anything since this generator object has been exhausted.

# But we can create another generator object and it'll function as expected again.

l = mygenerator()
print(list(l)) # This creates the list of the generator by storing the values.

s = mygenerator()
print(sorted(s)) # This creates a sorted list of the generated values


# How these generators work is as follows:

def countdown(value):
    
    while value>0:
        yield value
        value -= 1


count_down = countdown(5)
for i in count_down:
    print(i)

def infinite_counter(value):
    while value>0:
        yield value
        value+=1
        if value == 5:
            break

for i in infinite_counter(1):
    print(i)


def firstn_list(num):
    final = list()
    for i in range(num):
        final.append(i)
    return final

def generator_firstn(num):
    n = 0
    while n < num:
        yield n
        n+=1

print(sys.getsizeof(firstn_list(1000)))
print(sys.getsizeof(generator_firstn(1000)))

print("This is the advantage of generators. THey don't occupy as much space because the list is never explicitly generated.")

def fibonacci(num):
    a, b = 0, 1
    while a< num:
        yield a
        a, b = b, a+b
    
print(list(fibonacci(10)))

"""
Range iterators are a really great way to traverse through a list of numbers. 
The iter object is a container which gives access to the next object as long as it's valid.
This is incredibly useful because it allows python to treat lists which are actually not lists.
range() function returns a special range object which is an iterator.
However, it doesn't explicity declare a list which conserves memory and which is why we can declare something as big as the following:
range(10**12)
If range were to actually create this list of trillion values, it would occupy tens of terabytes of machine memory.
Since range doesn't explicitly declare an entire array, the memory is not occupied this way and one can still iterate through the entire range of numbers.
Pretty cool, isn't it?
"""

print(range(5))

print(iter(range(5)))
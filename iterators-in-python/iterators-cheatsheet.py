# Iterators

"""
An iterator is an object representing a stream of data; this object returns the data one element at a time. 
A Python iterator must support a method called __next__() that takes no arguments and always returns the next element of the stream. 
If there are no more elements in the stream, __next__() must raise the StopIteration exception. Iterators don’t have to be finite, though; it’s perfectly reasonable to write an iterator that produces an infinite stream of data.

The built-in iter() function takes an arbitrary object and tries to return an iterator that will return the object’s contents or elements, raising TypeError if the object doesn’t support iteration. 
Several of Python’s built-in data types support iteration, the most common being lists and dictionaries. 
An object is called iterable if you can get an iterator for it.
"""
a = [1, 2, 3, 4]
iterator = iter(a)

print(iterator.__next__())
print(iterator.__next__())
print(list(iterator)) # if we look here, the data from the stream has been popped and no longer exists there. print() prints [3,4]

# This is a default functionality for all iterators except range()

# Another example can be:
b = [5, 6, 7, 8]
c = zip(a,b)

print(c) # its a zip iterator
print(c.__next__()) # It'll return the first element from the stream of data
print(list(c)) # The first data is no longer part of the stream.

"""
Once the data from the stream is extracted and if not saved, is lost forever.

"""
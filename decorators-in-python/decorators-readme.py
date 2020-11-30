

"""
Functions in python are first class objects just like in JavaScript. These functions can be passed to another functions, returned from 
other functions, and declared in other functions.

Decorators, as the name suggests, is the extra work done before and after executing the function, in turn decorating a function.
Below given is the standard template of a decorator which can be used as per the instructions given below

functools are only imported to allow the python help to function properly. The decorator will work even without the import of functools and
@functools.wraps(func) decorator before the wrapper method.

"""

import functools

def my_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Do something before the function execution starts!")
        result = func(*args, **kwargs)
        print("Do something after the function ends")
        return result
    
    return wrapper

@my_decorator
def print_name(name):
    print(name, "is my name!")
    print("This is a inside the function inside the decorator!")
    return name

print(print_name("Goku kun"))

print()
print("*"*20)
print()



"""
To understand the basics of the decorators, this is how a decorators works. Without using decorators, implementing the functionality
of wrapper using functions.

"""

def start_end_wrapper(func):

    def wrapper(*args, **kwargs):
        print("This is where the wrapper starts")
        func(*args, **kwargs)
        print("This is where the wrapper ends.")
    return wrapper

def my_name(name):
    print(name)

my_name = start_end_wrapper(my_name) # if we use wrapper, we don't have to do this assignment.

my_name("Gkun")

print()
print("*"*20)
print()


# Example - 1

def repeat(num_times):

    def decorator_repeat(func):

        def wrapper(*args, **kwargs):

            for _ in range(num_times):
                func(*args, **kwargs)
            return None
        return wrapper
    return decorator_repeat



@repeat(num_times = 3)
def greet(name):
    print("Hello, {}!".format(name))

greet("Leo") # this function will execute 3 times by default!


print()
print("*"*20)
print()




"""
There are two types of decorators. Above we saw the function decorators, and now we'll take a look at the class decorators.

"""

class count_num_of_calls:

    def __init__(self, func) -> None:
        self.count = 0
        self.func = func
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(self.count)
        return self.func(*args, **kwargs)


@count_num_of_calls
def say_hello(name):
    print('Hello, {}'.format(name))

say_hello("Pegasus")
# The class variable count keeps a count of the number of times the function is executed.
say_hello("Igneel")


@count_num_of_calls
def say_hola():
    print('Testing with this!')

say_hola()
say_hello("Ash")
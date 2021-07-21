# Object Oriented Python

## What is an Object?

Everything in python is an Object. Variables, functions, classes are all python Objects.
Almost everything in python has some attributes and methods.

## Class

Every object is an instance of a class.
42 is an instance of class `int`.
Hello World is an instance of class `str`.

### self keyword

`self` keyword is used inside class methods to refer to the instance of the class.
`self` binds itself to the instance variable or object.

### type, isinstance & issubclass

type() takes an object and returns the type of the object. Eg:
`type('hello')`

The isinstance() function takes an object and a class, and returns True if the object you pass it is an instance of the class. Eg:
`isinstance(32, int)`

The issubclass() method takes two classes and checks if the first argument class is a subclass of the second argument class. Eg:
`issubclass(int, obj)`

### Magic Methods in Python Classes

1. `__init__(self)`

Classes have an optional magic method called `__init()` and it serves as an constructor to initialize the class instance.

2. `__str__()` and `__repr__()`

Both of the above mentioned magic method is responsible for debugging. Both functions return a string representation of an object.

`__str__()` should return user readable string representation of the object.

`__repr__()` should return the python code necessary to rebuild the object.

### Inheritance in Python Classes

Refer program files for a working example in python3

A subclass can inherit from a parent class

```python
class Parent:
  pass

class SubClass(Parent):
  def __init__(self):
    super().__init__() # calling the Parent __init__() magic method
```

There can also be a multiple inheritance in python.

A python class can inherit from multiple classes. One common use case for doing this is creating something called a Mixin.
This type of design mostly encourages code with composable architecture. Multiple inheritance is mostly used in Libraries.

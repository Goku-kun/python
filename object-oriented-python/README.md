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

## built-in `property` function

`property` function accepts four arguments: `fget`, `fset`, `fdel` and `doc`. The first three are getter, setter and deleter methods for the property and the last one is the docstring.

```python
class Person:

  def __init__(self, weight):
    self.__weight = weight

  def getWeight(self):
    return self.__weight

  def setWeight(self, newWeight):
    if newWeight > 0:
      self.__weight = newWeight

  def delWeight(self):
    del self.__weight

  weight = property(getWeight, setWeight, delWeight, "Docstring for Weight property")


person = Person(10)

print(person.weight) #this calls .getWeight()

person.weight = 5 #this called .setWeight()

del person.weight #this calls .delWeight()

person.weight = -5 #person.__weight is unchanged
```

The approach has many advantages:

1. `weight` attribute can now be used as if it was public. No need to use getters/setters/deleters.
2. Even though methods are not called directly, the typechecks and value checks are still applied as part of these methods
3. If these methods were used at multiple places in codebase and we had to change the names, it'd be troublesome. Instead, directly relying on the property name would make this easier.

While these are some of the advantages, we can go one step further with the `@property` decorator.

## @property Decorator

getters, setters and deleters can be defined by the `@property` decorator. It's a syntactic sugar for using the `property()` function

```python
class Person:

  def __init__(self, weight):
    self.__weight = weight

  @property
  def weight(self):
    """Docstring for the weight property"""
    return self.__weight

  @weight.setter
  def weight(self, newWeight):
    if newWeight > 0:
      self.__weight = newWeight

  @weight.deleter
  def weight(self):
    del self.__weight

  weight = property(getWeight, setWeight, delWeight, "Docstring for Weight property")


person = Person(10)
print(person.weight) #this calls .getWeight()
person.weight = 5 #this called .setWeight()
del person.weight #this calls .delWeight()
person.weight = -5 #person.__weight is unchanged

```

There are 3 rules to be followed:

1. All three methods must have the same member name.
2. The first method must be getter and is identified using the `@property` decorator.
3. The decorator for the setter and the deleter is defined by the name of the method `@property` is used with.

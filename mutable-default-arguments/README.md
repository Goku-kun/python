# Mutable Default Arguments in Python

There are two types of data structure/ data type objects available in python:

1. Mutable Object: refers to various container in python that are intended to be changed like list, dictionaries, sets etc.

2. Immutable Object: refers to values that aren't prone to change. They can be replaced but not modified like int, float, string, tuples, etc.

> Always use immutable object values as default arguments.

> Never use mutable object values as default arguments

The Official Documentation says:

> Default parameter values are evaluated from left to right when the function definition is executed. This means that the expression is evaluated once, when the function is defined, and that the same 'pre-computed' value is used each time the function is called.

```python
def createList(aList=[]):
    aList.append(1)
    return aList


list_1 = createList()
print(list_1)

list_2 = createList()
print(list_2)  # WHAT? Why would it print [1, 1]?

# The answer is because the same list aList gets appended 1 everytime the function is ran. A new list isn't created like in JavaScript.
```

## The `None` Workaround

If we wish to have mutable values as default arguments, we can use `None` as a special value to indicate that the no argument has been passed in.

```py
def createList(aList = None):
  if aList is None:
    aList = []
  return aList
```

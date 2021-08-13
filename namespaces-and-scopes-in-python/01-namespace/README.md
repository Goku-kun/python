# Namespaces and Scopes

## Table of Content

| Sr. | Name                                                                        |
| --- | --------------------------------------------------------------------------- |
| 1.  | [Introduction to Name and Namespaces](#introduction-to-name-and-namespaces) |
| 2.  | [Built-in](#built-in)                                                       |
| 3.  | [Global Namespace](#global-namespace)                                       |
| 4.  | [Local Namespace](#local-namespace)                                         |
| 5.  | [Enclosing Namespace](#enclosing-namespace)                                 |

## Introduction to Name and Namespaces

In python, a _name_ is an identifier for an object.

Python uses a system of name to differentiate between objects(strings or functions or int, etc).

To track all these names, python creates what's called a **namespace**

> A namespace is a collection of names and the objects that they reference. It's in the form of a dictionary which is hosted where the keys are the names that have been defined and the mapped values are the objects that they reference.

```py
variable_name = 'some value'
def printer():
  pass


# python creates a namespace that looks something like this:

{
  'variable_name': 'some value',
  'printer': <function printer at 0x339fxs>
  }

# so if we tried to print the value of the variable variable_name
# Python would search the above given dictionary for the variable name and access the corresponding value.
```

![namespace graph](name-space-graph.png)

There are 4 distinct types of namespaces that python generates.

1. Built-in
2. Global
3. Local
4. Enclosing

## Built-in

One of the four types of namespaces that exist in python is called the Built-in namespace.

The functions such as `print()` and `str()` exist in this namespace. Thus, they can be called in any python program we write.

In order to see what is provided in the Built-in namespace, we can use the following line of code.

```py
print(dir(__builtins__))

# This prints the following array:

['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
```

In total, there are 152 names that include exceptions, functions, types, special attributes, and other Python built-in objects.

It even constraints such as `True` or `False`.

`builtins` module is not accessed directly. Unless, you're writing a module which accesses on of the `builtins` module's methods than it can be used for direct access.

As an implementation detail, most modules have the name `__builtins__` made available as part of their globals

```py
import builtins
def UpperOpen(path):
  f = builtins.open(path, 'r')
  return f.read().upper()
```

## Global Namespace

The _global_ namespace exists one level below the built-in namespace. Generally, it includes all non-nested names in the module (file) we are choosing to run the Python interpreter on. The global namespace is created when we run our main program and has a lifetime until the interpreter terminates (usually when our program is finished running).

We can print the values stored in the global namespace using the `globals()` function.

Depending on where we call `globals()` we will have a different namespace generated. This means `globals()` will show the namespace at the time it was executed.

```py
print(globals()) # it won't print any information about user created globals since there aren't any such globals declared before this line
global_variable = 'this is one global variable'


def printer():
  global_variable = 'not a global variable'

print(globals()) # this will print all the globals including global_variable and the printer function and not the global variable inside the printer function since it's not global.
```

The global namespace contains all the non-nested objects of our program.

Also, if we're using `import` to import a module into a file, python creates a separate namespace for that imported module so that it doesn't pollute the namespace of the current file.

## Local Namespace

The deepest of all the namespaces is the local namespace.

Similar to how a global namespace exists until the program terminates, the local namespace exists until a function terminates.

Also, similar to `global()`, python provides a `locals()` function to see any generated local namespace. If `locals()` is called outside any function, then it behaves the same as `globals()`.

```py
global_variable = 'global'

def add(num1, num2):
  nested_value = 'Inside Function'
  print(num1 + num2)
  print(locals())

add(5, 10)
# in the global scope, locals() == globals()

# output
15
{'num1': 5, 'num2': 10, 'nested_value': 'Inside Function'}
```

As seen above, the value printed from calling `locals()` represents the namespace that exists only inside the function. Notice that it doesn't include the `global_variable` while printing the values nor did it include the `add()` function.

## Enclosing Namespace

Enclosing namespaces are created specifically when we work with nested functions and just like with the local namespace, will only exist until the function is done executing.

We can simply use the `locals()` function to visualize the enclosing space as well.

```py

global_variable = 'global'

def outer_function():
  outer_value = "outer"

  def inner_functon():
    inner_value = "inner"

    def inner_nested_function():
      nested_value = 'nested'
      print(locals())

    inner_nested_function() # prints the enclosing scope of inner_nested_function

    print(locals()) # prints the local scope of inner_function
  inner_functon()

outer_function()
```

## Summary

- Names are identifiers for objects in Python.
- The built-in namespace can be accessed using **builtins**.
- The global namespace can be accessed using globals().
- The local namespace can be accessed using locals().
- The enclosing namespace - a special type of local namespace that occurs when working with nested functions.

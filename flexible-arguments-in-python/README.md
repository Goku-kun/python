# Arguments in Python

## Types of Arguments in Python

There are 4 types of arguments that can be specified in the function declaration in python.

1. Standard Positional Arguments (If declared, are compulsory specified)
2. \*args
3. Standard Keyword Arguments
4. \*\*kwargs

These need to be specified in the above given order from left to right, if used all at once.

## Variable number of arguments: \*args

`print()` function doesn't care about how many arguments it receives.

How does the print operator do that?

> There is an additional operator called \* (unpacking operator)

The unpacking operator allows us to give our functions a variable number of arguments by performing what’s known as positional argument packing.

```py
def function_name(*args):
  print(args)

function_name("I", "can", "give", "any", "number", "of", "positional", "arguments")
# It prints: ("I", "can", "give", "any", "number", "of", "positional", "arguments")
```

Whatever name follows the unpacking operator (args in the example above), will store the arguments received in the form of a tuple.

This concept is like the `...` operator in JS.

If \*args is used in the variable declaration or parameter declaration, it gathers the values as per the arrangement.
Eg:

```py
array = [1,2,3,4]
a,*vals,b = array
print(a) # prints 1
print(vals) # [2,3]
print(b) # print 4

# Similarly for functions as well.
def function_name(a, *b):
  print(a)
  print(b) # b would be a tuple of arguments

function_name(*array) # unpacking operator unpacks the array into individual arguments
# This would print a as 1 and b as (2,3,4)

function_name(array) # array would go into a as the only argument since it's not being unpacked
# This would print a as [1,2,3,4]

```

Eg 2:

```py
nums = [1,2,3,4]

def add(num1,num2,num3,num4):
  print(num1,num2,num3,num4)

add(nums[0], nums[1], nums[2], nums[3]) == add(*nums)

# *nums unpacks the list into individual args
```

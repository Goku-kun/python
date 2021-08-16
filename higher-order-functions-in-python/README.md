# Higher Order Functions

## Table of Content

| Sr. No. | Topics                                                                |
| ------- | --------------------------------------------------------------------- |
| 1.      | [Functions as First Class objects](#functions-as-first-class-objects) |
| 2.      | [Higher Order Functions](#higher-order-functions)                     |

## Functions as First Class Objects

In python, functions are treated just like other objects.

> In Python, all Functions are classified as First Class Objects(also called First Class Citizens or First Class Functions).

They have four important characteristics:

1. First Class Objects can be stored in variables.
2. First Class Objects can be passed into functions as arguments
3. First Class Objects can be returned by a function
4. First Class Objects can be stored in a Data Structure (eg: list, dictionary).

```py
uppercaser = str.upper
uppercaser("superman") # returns SUPERMAN

nullcaser = [str.upper, str.lower]
value = "captain"
for func in nullcaser:
  value = func(value)
```

## Higher Order Functions

Higher Order Functions operate on other functions via arguments or via return value. This means it can either:

- Accept a function as an argument
- return a functions as a value

```py
def total_bill(func, value):
  total = func(value)
  return total

def add_tax(value):
  tax = value * 0.06
  new_total = value + tax
  return new_total

def add_tip(value):
  tip = value * 0.2
  new_total = value + tip
  return new_total

print(total_bill(add_tax, 100)) # 106
print(total_bill(add_tip, 100)) # 120


# But as we can see, it's not particularly useful this way.

# What if we had to uniformize the outputs for both add_tax and add_tip functions?

def total_bill(func, value):
  total = func(value)
  return f"The total value is {'{:.2f}'.format(total)}$. Thank you!"

```

No matter what function is passed, the output will always look the same. We can consistently format the total. Higher Order functions are also useful when implementing iterations.

Higher Order Functions can also be returne from a function.

```py

def make_box_volume_function(height):
    # defines and returns a function that takes two numeric arguments,
    # length &  width, and returns the volume given the input height
    def volume(length, width):
        return length*width*height

    return volume

box_volume_height_15 = make_box_volume_function(15)

print(box_volume_height_15(3,2))
```

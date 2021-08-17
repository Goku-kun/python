# Higher Order Functions

## Table of Content

| Sr. No. | Topics                                                                |
| ------- | --------------------------------------------------------------------- |
| 1.      | [Functions as First Class objects](#functions-as-first-class-objects) |
| 2.      | [Higher Order Functions](#higher-order-functions)                     |
| 3.      | [Built in Higher Order Functions](#built-in-higher-order-functions)   |

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

## Built in Higher Order Functions

The most used built-in higher order functions in python are:

- map
- reduce
- filter

### map

returned_map_object = map(function, iterator)

```py
a = [3,6,9]
double = lambda x: x*2

double_a_map_object = map(double, a)
double_a = list(double_a_map_object)
print(double_a) # doubles each element in a: [6, 12, 18]
```

Eg:
Say we stored our course grades in a list, but some of the grades were on a four-point scale and others were on a 100-point scale. To get all the grades on the same scale, try using a lambda function with the map() function to multiply just the grades on the four-point scale by 25 to get all of the grades on the same 100-point-scale.

```py
grade_list = [3.5, 3.7, 2.6, 95, 87]

# assign the result of your map function to the variable grades_100scale
grades_100scale = map(lambda x: 25*x if x<4 else x, grade_list)

# convert grades_100scale to a list and save it as updated_grade_list
updated_grade_list = list(grades_100scale)

# print updated_grade_list
print(updated_grade_list)

```

### filter

Similar to `map()`, the `filter()` function takes on two arguments, a function and an iterable.

The filtering function should return `True` or `False`. The returned `filter` object will only hold those values for which the filter function turned out `True`.

```py
names = ["margarita", "Linda", "Masako", "Maki", "Angela"]

M_names = filter(lambda x: x[0].lower() == "m")
print(list(M_names))
```

Eg:
We were given a list of lists, where each sublist holds the title of a famous book that has a year as its title and the last name of the author that wrote the book. Unfortunately, when this list was made, each of the books was accidentally entered twice—once with the title as a numeric value and once with the title as a string. Use the filter() function to deduplicate the list and keep only the sublists that have the book title stored as a string:

```py
books = [["Burgess", 1985],
  ["Orwell", "Nineteen Eighty-four"],
  ["Murakami", "1Q85"],
  ["Orwell", 1984],
  ["Burgess", "Nineteen Eighty-five"],
  ["Murakami", 1985]]

string_titles = filter(lambda x: type(x[1]) == str, books)
string_titles_list = list(string_titles)
print(string_titles_list)
```

### Reduce

Reduce must be imported from `functools` module to use it.

Rather then returning a reduce object, reduce returns a single value.

```py
int_list = [3, 6, 9, 12]

reduced_int_list = reduce(lambda x,y: x*y, int_list)

print(reduced_int_list)
# 3*6*9*12 = 1944
```

Eg:Given a list of letters, use the reduce() higher-order function with a lambda function to combine the letters into a single word:

```py
from functools import reduce
letters = ['r', 'e', 'd', 'u', 'c', 'e']
word = reduce(lambda x,y: x+y, letters)

print(word) # 'reduce'
```

## Summary

- The map() function applies a passed function to each element in an iterable and returns a map object.
- The filter() function applies a filtering function (a function that returns a boolean) to each element in an iterable. filter() returns a filter object with only the elements for which the filtering function returned True.
- reduce() must be imported from the functools module. It reduces an iterable to a single value by cumulatively applying a passed function to the first pair of elements in the iterable and then each sequential element with the return value.

These three functions streamline code on their own, but they are even easier to read when they are used in conjunction with lambda functions.

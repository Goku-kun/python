from collections import namedtuple
# It is similar to a struct in C

Point = namedtuple('Point', 'x,y')
# this will create a class called Point with field x and y

pt = Point(2, 3)
print(pt)
# We can directly access the properties assigned to the class using the . operator. `(objectname.fieldname)` will return the value of that field for that object.
print(pt.x)
print(pt.y)

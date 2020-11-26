# *args and **kwargs are passed to functions as flexible arguments. 
# These are used when one doesn't know how to arguments shall be passed by the user while declaring the function.

# *args returns a tuple or a sequence of arguments
def catch(*args):
    print("args = ",args)
    print(args[5]) # you can access each argument in the same way you'd access a tuple

catch(1,2,3,4,5,"abc",True)

# **kwargs are known as key word arguments which expands the arguments as a dictionary

def catch_kwargs(**kwargs):
    print("kwargs = ", kwargs)
    print(kwargs['key4']) # It can be accessed in the same way as a dictionary can be accessed

catch_kwargs(key1=1, key2="hello", key3="nice", key4=True)

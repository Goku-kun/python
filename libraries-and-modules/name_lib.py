def print_name():
    print("My name is Dharma")


def name_length(name):
    print(f"The length of my name is {len(name)}")


def name_upper(name: str):
    print(f"My name in upper case is {name.upper()}")


print("The name of name_lib is", __name__,
      " and it's not main since it's being used as a library file")

if __name__ == 'main':
    print("Since this is inside the main method, it won't be executed.")

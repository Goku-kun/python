# Libraries and Modules in Python

## `main` Method in Python

Using the main method is common practice seen in python programs. It helps isolate the statements when the file is being used as a library file. When a .py file is executed, it's `__name__` change to 'main' but if it's being used a library file, it's `__name__` value is set to the original filename.

So,

```py
if __name__ == 'main':
  # some statements that would execute only if the file is executed directly.
  # Won't execute ifthe file is being used as a library
```

## Virtual Environments

Virtual Environments are very important to create a versioned python program which is self contained (similar to using npm init). They also make it very easy to store the dependencies that the python program uses.

To create virtual environment use,

```
python3 -m venv name_of_folder
```

The -m flag suggests that the command be used to execute as a module.

Like package.json, requirements.txt is a file wherein all the dependencies are stored along with their versions.

To create this file, run the following command

```bash
pip freeze > requirements.txt
```

To install the dependencies again, use the command

```bash
pip install -r requirements.txt
```

## Libraries

Using the `import` keyword, external libraries can be imported into a python file. While import statements can go anywhere inside the file, it'd make much more sense to list them out at the top of the file.

Importing modules using the `import` keyword is usually the best way to import since it preserves the namespace of the file but another common way of importing is `from <module> import <object>` to import a specific function, object, class, subclass, etc.

External modules can also be installed from an index called PyPI.org(the python package index) using the command:
`python3 -m pip install <package_name>`

Python follows the batteries included philosophy which means most of the functionalities are available as part of python under the Standard Libraries.

`import sys` can be used for system specific calls. `import os` can be used for operating system interfaces such as for accessing directories and `os.path` is an excellent submodule used for handling paths on any operating system. There's a `math` library and a `json` library as well. `datetime` to deal with dates and times.

There are a lot of packages on PyPI, and they’re not always up-to-date. Sometimes it helps to look at a package before installing it. Simply search for a package name on PyPI.org - for example, here’s the page for the redis package. If you follow the Homepage link, you’ll be taken to the project’s GitHub page, where you can see that the latest commit was very recently. So you know this package is actively maintained, and will probably work in your up-to-date version of Python.

## Modules

A directory becomes a module if it contains the `__init__.py` file inside it. (It's no longer mandatory for python3 but still supported)

### PYTHONPATH

PYTHONPATH is a list of paths under which python will look for packages

1. It first starts looking at the current working directory.

# Python

This project contains programs and concepts of python for beginners.

Refer `./concepts` dir for the docs and `./sample` dir for complex python program.

we are using python 3.8.2

## Python Features

- **Interpreted Language**: Python is not compiled language, as there is not intermediate code generated for Python.
- **Scripting language**: Python can also be used as scripting language. But python is NOT a scripting language but a general purpose language.
- **Functional Programming**: Python consider function as first class citizen and provides many techniques which support functional programming paradigm.
- **Object Oriented programming**: Python is a object oriented programming language. Supports concept of class and object. Everything(function, properties) in Python is object, which is very similar to Javascript.

<details>

<summary>python Commands:</summary>

```shell script
# check the version of python
python --version

# execute a program
python to/file/path/test.py

# enter python command line
python

# exit from the python command line
>>>exit()

# use python3 as python
alias python='python3'
```

</details>


## virtual environment

```sh
python3 -m pip install --user --upgrade pip
python3 -m pip install --user virtualenv
python3 -m venv env # name should be venv
```

## What is the use of pypirc and pip.conf

- pypirc is file used by multiple tools, but not by *pip*. For example `twine` and `easy_install`. Its mostly used by package used for publishing, if you are not publishing we mostly dont need this file.

- pip.conf - this file is only used by pip, so if you are using any other tools like poetry or other its never used.

## What is package in Python

Package bundles all Python code that is required to create a module.

## Statistics basics

### Mean

Mean is average. Sum of all the values divided by number of values

### Median

Median is middle of the sorted values in ascending.

### Mode

Mode is the most frequently data.

## What difference between Java Package and Python module

<details>

<summary>Java Package and Python module</summary>
can it be span across multiple files??
yes we dan do it

form algo.mod import test

__init__.py this file are executed when a module is imported.

use cases:

- empty __init__.py file are kept to make user understand that its a python module.
- what * includes in the module(files) __all__= []

__pycache__ are compiled files, just used in local to speed up execution, not to be versioned or ship in modules or binary.

</details>

## Best practices

- Unlike Java we need to create a class per file, in python all class which are used together by user are kept in same file.
- We create few class in python than in Java, because different type of data structure

## Whats $PYTHONPATH env variable

## dir() function

defines what particular module defines.

## what are diff between _ and __

_ are private variable, as there are no concept of private in Python
__  python internal methods have special meaning (also known as DUNDER)

## Reference of python

askpython - read about any python modules, inbuilt function just search it will throw result
pypi - its like npm, contains all the python modules and its a python default registry.

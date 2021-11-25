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

## What is PIP

Like Node has NPM as package manager, similarly pip is package manager for Python.

Default registry for PIP is https://pypi.org

<details>

<summary>PIP Commands:</summary>

```sh
# to make pip to work from command prompt
alias pip='python -m pip'# in ~/.bashrc

# make sure pip is installed
# latest version of python comes with pip
python -m pip --version

# install a package
pip install <package-name>

# uninstall a package
pip uninstall <package-name>

# list all installed packages
pip list

# update pip version
pip install --upgrade pip
```

</details>

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

askpython - read about any python modules

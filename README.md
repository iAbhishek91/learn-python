# Python

This project contains programs and concepts of python for beginners.

Refer `./concepts` dir for the docs and `./sample` dir for complex python program.

we are using python 3.8.2

## Python Features

- **Interpreted Language**: Python is not compiled language, as there is not intermediate code generated for Python.
- **Scripting language**: Python can also be used as scripting language. But python is NOT a scripting language but a general purpose language.
- **Functional Programming**: Python consider function as first class citizen and provides many techniques which support functional programming paradigm.
- **Object Oriented programming**: Python is a object oriented programming language. Supports concept of class and object. Everything(function, properties) in Python is object, which is very similar to Javascript.

## Commands

```shell script
# check the version of python
python --version

# execute a program
python to/file/path/test.py

# enter python command line
py

# exit from the python command line
>>>exit()

# use python3 as python
alias python='python3'
```

## What is PIP

Like Node has NPM as package manager, similarly pip is package manager for Python.

Default registry for PIP is https://pypi.org

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
```

## What is package in Python

Package bundles all Python code that is required to create a module.

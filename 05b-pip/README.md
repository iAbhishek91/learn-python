# Dependency and packaging a project

- install and download packages and list them in requirements.txt using pip
- building Docker image
- few examples

## Pre-requisite

- install python3 and pip3

## Dependency management

## What is PIP

Like Node has NPM as package manager, similarly pip is package manager for Python.

Default registry for PIP is https://pypi.org

There are other package manager as well like: poetry

Few limitation of pip

- synchronous while downloading dependency, hence really slower.
- cant do build or publish modules.

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
pip install <package-name>==<version>
pip install -r requirements.txt

# uninstall a package
pip uninstall <package-name>

# list all installed packages
pip list

# update pip version
pip install --upgrade pip

# list all python packages that are installed in the system
pip freeze
```

</details>

## How to auto create requirements.txt

Requirements file can be created automatically with the help of the below module.
This scan your codebase and all the imports and auto creates the file.

```shell
pip install pipreqs
pipreqs /path/to/the/project
```

## Examples

Example-1: hello world app
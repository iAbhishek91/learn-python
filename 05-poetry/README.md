# Poetry

Poetry is a tool(binary really) for dependencies management, build and Packages in python.

- manage install/update for you.

## difference b/w poetry and pip and others

- pip is synchronous, whereas poetry is asynchronous so bit faster than pip

## Install

There are couple of way to do download the binary

- Install using pip(non recommended)
- Install using poetry using curl (it keeps poetry separate in the system and not tied to python)

```sh
ln -s ~/.poetry/bin/poetry ~/.local/bin
```

## Commands

```sh
# use poetry to create a project
poetry new project-created-by-poetry

# add a package
poetry add requests # adds requests module and its dependencies, it also add the dependencies in poetry.lock file
poetry add pytest black --dev # add as dev dependencies
poetry add request==2.25.1

poetry env info # python virtual env and some other metadata

poetry update # reinstalls all the dependencies

poetry build # build the project in package, creates a dist folder and puts the gz file there

poetry publish # publish to global python registry
```

## New project created by poetry

This scaffolds multiple file.

- pyproject.toml: is the configuration file, very similar to package.json. Contains details about the project, authors, dependencies, dev-dependencies and version.

## environment variables

environment variables are handled differently, unlike pip where we can use `.env`.

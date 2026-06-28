# uv workflows

## uv.lock is source of truth: yes but it's not so easy...

Sometimes we want to reproduce a project and we think that a simple `uv sync` can create our environment without yelling anything but no!

Sometimes the pyproject.toml is old, python version has changed, softwares have MAJOR updates and dependencies can break, so you have to know if:
- working with these pinned versions are essential: 
    - if yes you have to go on Pypi and searches for Python requirements in first
    - if no, you have to choose the latest versions of theses packages and add them to the project

In my case, I chose to recreate a project with latest versions from packages that I need:
- `pyfiglet`
- `black`
- `flake8`
- `pre-commit`
- `pytest`
And a version of Python that is stable in 2026 and works with new packages : 3.13 version.

## Group dependencies

These packages we quoed don't have the same goal in the project:
- pyfiglet is used for the main application and for the user then expected in **production**
- black,flake8,pre-commit are used by the developer without any need to be in production: **dev**
- pytest is about testing our project: **test**

All these categories can be used to create groups in the `pyproject.toml`, so this way we can manipulate all these dependencies according what we do with our app.

### Create group dependencies with uv

In the case you want to recreate a `uv.lock` with newer versions with for starting point the name of the packages:

- once you have 'uv' on your machine: in your working directory of your project:
    ```
    uv init
    ```
- choose the '3.13' version of Python for pinning by default your venv with uv:
    ```
    uv python pin 3.13 --global
    ```
- add the packages to your project with a group dependencies:
    ```
    uv add --group dev black flake8 pre-commit
    uv add --group test pytest
    uv add pyfiglet
    ```
After these commands, the pyproject.toml looks like this:
```
[project]
name = "python-development-good-practices"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "pyfiglet>=1.0.4",
]

[dependency-groups]
dev = [
    "black>=26.5.1",
    "flake8>=7.3.0",
    "pre-commit>=4.6.0",
]
test = [
    "pytest>=9.1.1",
]
```
The versions that are indicated are the latest in June 2026.
We observe that production dependencies are in : [project]  
**Note:** 'uv add' command modify .toml, .lock & the venv.
It creates a venv when there doesn't exist it

### Use the virtual environment with uv

To activate it in your shell:
```
source .venv/bin/activate
```
To use it to run a program into it:
```
uv run python sign_printer/sign_printer.py <text>
```
### DIfferences/resemblances with Poetry

A lot of concepts are shared between uv and POetry and it's pretty normal because they respect PEP621 specifying to store project's metadatas in a pyproject.toml with the same template.

For example, you can **build a uv.lock from a pyproject.toml created with Poetry**.

If you have the .toml in your directory, you can run:
```
uv lock
```
You will create a uv.lock in function.

#### Resemblances

Add a package in your venv and your .lock and .toml files:
```
uv add requests
poetry add requests
```
Remove a package:
```
uv remove requests
poetry remove requests
```
LOck a .toml:
```
uv lock
poetry lock
```
Sync a .lock with .venv
```
uv sync 
poetry sync
```

#### DIfferences

The equivalent to: 
```
poetry install
```
which allows to install missing dependencies from .lock in the .venv without deleting those which aren't in the .lock

For **uv** it's :
```
uv sync --inexact
```




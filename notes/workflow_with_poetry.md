# Workflow with poetry

Poetry can create environments and manage dependencies, the concept of reproducibility of an environment is also here through files and it owns specialized features to create packages that we could build according to standards to be uploaded on packages repositories like Pypi.

1) **Download Poetry via pip/pipx or natively:**
```
# pip
python -m pip install poetry
```
**or** install it like a software on your Linux system:

```
curl -sSL https://install.python-poetry.org | python3 -
```
You can also install it with pipx which is globally the same than with curl:
```
pipx install poetry
```
pipx is used to install Python CLI applications globally while still isolating them in virtual environments. pipx will manage upgrades and uninstalls when used to install Poetry.

So no need to install Poetry in an environment to access it via 'poetry' command.

2) **Initialize a project with a pyproject.toml**

```
poetry init
```
**Result:** Poetry guides you to customize your pyproject.toml for your package, so make this command in the repository itself.
- Interactively you can input:
  - the package name
  - the version
  - the description
  - the author
  - license or not
  - the tied Python version
  - dependencies

When you inform all these informations, poetry creates a `pyproject.toml` in function of this in the repo.

**Tip**: Something of pretty cool that often ignored, we often invoke a package that's already on Pypi but it exists different ways to include a dependency in a project:
```
You can specify a package in the following forms:
          - A single name (requests): this will search for matches on PyPI
          - A name and a constraint (requests@^2.23.0)
          - A git url (git+https://github.com/python-poetry/poetry.git)
          - A git url with a revision         (git+https://github.com/python-poetry/poetry.git#develop)
          - A file path (../my-package/my-package.whl)
          - A directory (../my-package/)
          - A url (https://example.com/packages/my-package-0.1.0.tar.gz)
```

3) **Add packages in our poetry environment**:

**Add packages by CLI**:

```
poetry add pyfiglet
```
**Result:**: 
- This command adds the `pyfiglet` package to the pyproject.toml
- Creates a poetry.lock file and modifies it for integrating `pyfiglet`
- A `venv` is created with `pyfiglet` in the `site-packages`
- For each add, poetry tells us if there is dependencies to install with the package added and the state of the .lock compared to the .toml

Notes: -  the .lock file contains references to folders like .whl, tar.gz and sha256 hashes. It's generated/modified by poetry after a state change in the project and shouldn't be modified by hand. Without it, it's impossible to recreate the environment. That's like the modern version of requirements.txt respecting new standards.

**Modify manually the pyproject.toml**

Add a package  in your `dependencies=[]` parameter in your .toml:
```
dependencies = [
    "pyfiglet (>=1.0.4,<2.0.0)",
    "requests",
]
```
Run:
```
poetry lock
```
**Result:** 
- It will synchronize the .toml which is source of truth with your .lock file

Then:
```
poetry install --no-root
```
**Result:**
- It installs new synchronized packages
- --no-root flag is to avoid downloading the entire project

4) **Remove packages in our poetry environment**:

**Remove packages by CLI**:

```
poetry remove requests
```
**Result:**: 
- Removes `requests` from venv
- Updates the .toml & the .lock

**Modify manually the pyproject.toml**

Remove a package  in your `dependencies=[]` parameter in your .toml:
```
dependencies = [
    "pyfiglet (>=1.0.4,<2.0.0)",
]
```
Run:
```
poetry lock
```
**Result:** 
- It will synchronize the .toml which is source of truth with your .lock file

Then:
```
poetry sync
```
**Result:**
- It uninstalls packages from venv that aren't in the updated .lock file

5) **Activate/Deactivate the .venv environment from your Poetry:**

From your Linux shell to activate your local environment:
```
eval $(poetry env activate)
```
**Result:**
- Poetry is going to activate the .venv created by an "add" or "install" command.

For deactivating it:
```
deactivate
```

### Some configuration tips

According to the way you install Poetry with pip or pipx or maybe the versions you download, Poetry isn't configured from the same way.

1. With pipx for example, I found some new differences that i didn't know:
- the environment doesn't load in the project directory but in the cache of POetry in ~/.cache/pypoetry/virtualenvs/ directory: it changes when you're accustomed to manage the .venv in your directory project.
    - To change this you have to access to the config of the Poetry and change some parameters:
      ** COnfiguration parameters of Poetry:** 
      ``` 
      poetry config --list
      ```
      **FInd the `virtualenvs.in-project` parameter and set it to `true`:**
      ```
      poetry config virtualenvs.in-project true
      ```

2. When you run some ```poetry install```, Poetry expects you build a package(yes contrary to pip or venv it's package oriented) and you want to reproduce an environment but you don't always want to build a package , or maybe not for the moment.
   - To set a Poetry environment from a .lock file without Poetry yelling, add this config in your .toml:
     ```
     [tool.poetry]
     package-mode = false
     ```
     **Then**:
     ```
     poetry install --no-root
     ```
     If you do not want to install the current project(the core of your package) use --no-root


3. To manage the environments with POetry, the `env` command is all you need:

Infos about your actual venv:
```
poetry env info
```
Infos about Poetry environments:
```
poetry env list
```
Delete an environment:
```
poetry env remove <venv-name>
```

4. **Importance to manage dependencies**

- In a simple pip environment all the dependencies are in the same `requirements.txt` without distinguishing any group. Is the package is for development, production, linting?
With Poetry you can set different groups for installed packages in .toml file:
  ```
  [dependency-groups]
  test = [
      "pytest (>=8.0.0,<9.0.0)",
  ]
  lint = [
      "ruff (>=0.11.0,<0.12.0)",
  ]
  dev = [
      { include-group = "test" },
      { include-group = "lint" },
      "tox",
  ]
  ```
  Result:
  - you can make sections, subsections

- Then, you can choose what package to add into the group you want:
    ```
    poetry add pytest --group test
    ```
    The add command is the preferred way to add dependencies to a group.

- you can remove from a group:
  ```
  poetry remove pytest --group test
  ```
- you can install from a .lock:
  ```
  poetry install --without test
  poetry install --only lint
  poetry install --only main
  ```
  **Result**
  - you can exclude some groups from the installs with `--without`
  - you can choose only groups you chose with `--only`
  - you can choose to select only the main deps from [project] with `--only main`
  
- same idea with `sync`:
  ```
  poetry sync --without test
  poetry sync --only lint
  poetry sync --only main
  ``` 

Dependencies management is what to transform personal projects to production projects.

### Rua apps in a poetry environment

Place you in your working directory and run:

```
poetry run python sign_printer/sign_printer.py hello
```

or

```
poetry run sign_printer/sign_printer.py hello
```
Poetry is enough smart to find the Python of your environment with a simple .py file

Output:

```
                           
    /           /   /      
---/__----__---/---/----__-
  /   ) /___) /   /   /   )
_/___/_(___ _/___/___(___/_
                           ```
```

  
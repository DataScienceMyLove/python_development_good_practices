# A fast stop on Semantic versioning

You already know Semantic versioning without being a software engineer from the moment you installed your first software. The version of your software is always numeroted with 3 numbers spaced with dots.When you don't develop softwares you don't care about that but when you're beginning to make little projects with third-party libraries, you understand that you won't go far away without caring about that.

Semantic versioning can be important in different ways in your development journey:
Some ideas where it's important : 
- Manage the Python versions with dependencies in an environment without having conflicts
- Identify software/packages by their versions and their features you interested for
- Forecast and develop in function of version changes
- Understand the evolution of a software by its history

### How does it work?

From the [semver.org](semver.org) website, we have this clear definition:

Semantic Versioning 2.0.0
Summary
Given a version number **MAJOR.MINOR.PATCH**, increment the:

- MAJOR version when you make incompatible API changes
- MINOR version when you add functionality in a backward compatible manner
- PATCH version when you make backward compatible bug fixes
Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.

When a big software like Python for example changes of MAJOR version(2.7.0=>3.1.0), it breaks code from developers. So if you use a software or a software is a dependency of your project and operates a MAJOR version, you have to expect your application breaks.

### What does it mean in a Python project?

You always have to care about which version is compatible with another.

Example: you want to reproduce a cool project you found but it's a little old.

On your local machine you have a recent version of Python and you run a virtual environment from it.

You use your package manager to try reproducing the environment according to the versions of the listed packages in the pyproject.toml but something breaks:
- either Python interpreter is too advanced to read old rules from old code
- either dependencies changed and some packages cannot be installed

In these cases you will need semantic versioning to handle those kind of situations because you have informations on compatible dependencies versions for a Python package on PyPi...

### COnstraints on dependencies in pyproject.toml

With this Semantic versioning concept, we have abilities to adapt our project in function to avoid it breaks or to have flexibility from softwares that we cannot control the evolution. That's why **constraints** are practical.

- Sometimes in your .toml files you will find these type of notations:
```
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
- Take an example with pyfiglet: the pinned version is 1.0.4 with a greater than or equal sign
What this means: “Install any version greater than or equal to 1.0.4, with no upper limit.”

How it works: If, tomorrow, the author of pyfiglet releases version 2.0.0 or 3.0.0 with major changes that break the compatibility of your code (known as ‘breaking changes’), an update command (such as `uv lock --upgrade`) will install it anyway. Your code could then crash.

- Imagine we want to supervise the versions before the package takes a MAJOR change, we can do this:
  ```
  dependencies = [
    "pyfiglet>=1.0.4,<2.0.0",
    ]
  ```

- Or same than the last example with Poetry only:
  ```
  pyfiglet = "^1.0.4"
  ```
  The carret has the same action to avoid reaching the next MAJOR change. 
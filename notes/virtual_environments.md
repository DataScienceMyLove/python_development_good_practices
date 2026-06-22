# Virtual environments

Install dependencies on your system when you are on your local machine is not a recommended practice.

Simply because we don't know what is it, if somebody left malicious code...

### What's the purpose of a Python virtual environment?

1. Dependencies management

COmplex applications have a ton of dépendencies & they can enter in conflict with what's in your system.

In a system, we can have different versions of Python, pip and you really want to an isolated & standardized environment.

2. Consistency improvements

When you build a project, you often need third party packages which are on distant repositories like PyPi.

Package managers(pip is the oldest and most famoust) are tied to these repositories and allow to download these third-party package in an Python environment (system, shims pyenv, a virtual environment).

These package managers have the power to reproduce an existing environment which makes it portable : packages, versions and this thanks to a text file.(requirements.txt, pyproject.toml).

When we stay in the portability idea, you often want to customize Python versions, Python packages such a way they are compatible, like the pieces of a puzzle some of which are incompatible with others, it's important to find a place where makes this like a laboratory.

When you chose your Python version, you define dependencies & their versions(yes! they are softwares..) & you install them in a virtual environment you can ensure that anyone using your app could use the same dependencies & the same versions to reproduce your project.

### What's a virtual environment technically?

We often call it 'venv' when we name it.

That's a lightweight tool: the venv folder contains a size near to 0kB when it's created, the Python being contained is a link to another Python on the machine, not the executable.

That focuses specifically on creating and managing virtual environment. That comes with a large ecosystem of plugins & integrations.

We can create these venv folders by the Python standard library which comes with a `venv` module, old software like `virtualenv` or the new comers: a mixture of package manager, venv creators,end-to-end manager of a project: `uv` or `poetry`.

**Transition**: We are going firstly use simple virtual environments in [v4](https://github.com/DataScienceMyLove/python_development_good_practices/tree/v4)
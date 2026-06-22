# Classic old workflow with python,venv module and pip

### Start with Python version choice

When we want to create a virtual environment, a question is central: what version of Python I want to for my project?

Because with the venv module, we are going to create an environment with the tied version of Python.

Tools like `pyenv` allow to manage perfectly Python versions in building with C dependencies a pre-compiled version of Python of your choice.

Then ***Python shims*** will allow you to manage versions, create temporary virtual environments, manage the Python of your system. It's a great tool but it seems to be condamned by the arrival of new softwares that combine all-in-one and written in compiled languages.(**uv from astral, the creator of Ruff**) 

### Create and manage your environment

You chose a version of Python on your system.

1. **Create your virtual environment in opening your terminal in your working directory and run:**

```
python -m venv sign_printer_venv
```
**Result:** That creates a folder named sign_printer_venv.

It contains:
- binaries in the folder `bin`
- libraries when you will download with `pip install` (precisely in `site-packages`)
- `pyvenv.cfg` : a little file that helps libraries to redirect to the `site-packages` of the venv and not this of the system.

2. To activate the virtual environment, run the following command:

```
source sign_printer_venv/bin/activate
```
**Result:** This command will inject the environment in our shell:
- the `activate` script is going to modify the PATH environment variable and when you will execute Python it will be this of the venv

3. Recreate the environment & run the application

To install the app's dependencies, run the following command:

```
pip install -r requirements.txt
```
**Result:** This command will avoid the 'pip install' repetition.

The developper has listed all the used packages in his venv with its versions, all of this in `requirements.txt`.

It's the most important part for reproducibility because with pip, we can download all the packages of this list in one command in our venv.

4. Want to add your touch and modify/experiment at your tastes:

- Add packages, features in the app then recreates a `requirements.txt` with:
```
pip freeze > requirements.txt
```
**Result:**
- `pip freeze` lists all the packages of your venv in the stdout of your terminal
- `> requirements.txt` redirects the output of pip freeze in the `requirements.txt` & overwrites it 

Note: If you want a specified version of a package, go to [Pypy(https://pypi.org/)]( Python Package Index)

- Search a package & Go to its page
- Click on 'release history' & you'll see versions from the latest to the oldest. You will find dependencies for all these versions too.


1. You finished with this project

- To exit the virtual environment, run the following command:

```
deactivate
```
**Result:** You will retrieve the Python of your system in your terminal and all the downloaded packages won't be redirect to your venv

6. Good practice

- you want to clean up a little your repo before committing :
    - Write the name of the venv in your `.gitignore`: virtual environments has no its place in a repository in Github
    - you can delete your venv to avoid accumulating venv on your machine: dependencies can be heavy: it's practical, all in the same folder.


**Transition:** In [V5](https://github.com/DataScienceMyLove/python_development_good_practices/tree/v5), we're going to use a more powerful & centralized tool which allow to tie environment management & dependency management in one place.
# Automations tools

## Make & Makefiles

**Make** is an old unix software created to avoid recompiling big C projects to the root and just recompile the dependencies you need.

That's probably on your OS if you are on GNU Linux.

It will look for a file called **Makefile**
These Makefiles work with a system of targets, dependencies & commands.

Example:
```Makefile
example: dependency
    @uv run python sign_printer/sign_printer.py hello
```
To run the `example` target for the uv command:
```bash
make example
```
**Makefiles** are pretty nice, that's a nice way to wrap what can become a long & often used command into an **alias**.
You can even run some little personalized scripts thanks to them.

### Different concepts, one file

Example with our Makefile that runs many parts of our project upstream:

```Makefile
example:
	@uv run python sign_printer/sign_printer.py hello

test:
	uv run pytest --verbose tests/

lint:
	uv run flake8 --show-source

format:
	uv run black --diff .

clean:
	find . -type d -name '__pycache__' -exec rm -rf {} +
```

1. Run our app for an example in our uv virtual environment:
```
make example
```
**Note**: The @ before the command indicates that we don't want to the command prints out the stdout.

2. Test our app through tests with pytest targetting tests/ directory:
 ```
 make test
 ```
 **Note**: The command runs perfectly all the tests with verbose
 ```
 ========================================================================================================================= test session starts =========================================================================================================================
platform linux -- Python 3.13.13, pytest-9.1.1, pluggy-1.6.0 -- /home/gaetan/python_development_good_practices/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /home/gaetan/python_development_good_practices
configfile: pyproject.toml
collected 3 items                                                                                                                                                                                                                                                     

tests/test_utils.py::test_fonts_are_strings PASSED                                                                                                                                                                                                              [ 33%]
tests/test_utils.py::test_random_font_returns_a_random_font PASSED                                                                                                                                                                                              [ 66%]
tests/test_utils.py::test_required_argument PASSED                                                                                                                                                                                                              [100%]

========================================================================================================================== 3 passed in 0.00s =======================================================================================================
```
3. Linting with flake8:
   ```
   make lint
   ```
**Note**: DOn't forget to add your .venv in your .flake8 in `exclude` else flake8 will handle your site-packages
```
./tests/test_utils.py:4:1: F401 'pytest' imported but unused
import pytest
^
make: *** [Makefile:8 : lint] Erreur 1
```
**Tip**: You can pass the error you want to ignore in the flag `--ignore=` rather than in the .flake8.

```
uv run flake8 --show-source --ignore=F401
```

4. Formatting with Black:
    ```
    make format
    ```

**Note**: 
- The `--diff` flag in black command won't modify your repo whereas usually it will.
It's interested to see before applying.
- `--target-version py313` is to avoid to black to format according its last version, write your python version!!

**Output:**
```
--- /home/gaetan/python_development_good_practices/sign_printer/sign_printer.py 2026-06-24 17:30:56.690897+00:00
+++ /home/gaetan/python_development_good_practices/sign_printer/sign_printer.py 2026-06-24 23:36:58.891769+00:00
@@ -1,9 +1,10 @@
 #!/usr/bin/env python3
 """
 Module sign_printer contains the sign_printer app.
 """
+
 import sys
 import utils
 from pyfiglet import Figlet
 
 
would reformat /home/gaetan/python_development_good_practices/sign_printer/sign_printer.py
--- /home/gaetan/python_development_good_practices/tests/test_utils.py  2026-06-24 17:30:56.690897+00:00
+++ /home/gaetan/python_development_good_practices/tests/test_utils.py  2026-06-24 23:36:58.893380+00:00
@@ -1,8 +1,9 @@
 """
 test_utils contains unit tests for the sign_printer utilities.
 """
+
 import pytest
 from sign_printer.utils import FONTS, random_font, validate_args
 
 
 def test_fonts_are_strings():
would reformat /home/gaetan/python_development_good_practices/tests/test_utils.py
--- /home/gaetan/python_development_good_practices/sign_printer/utils.py        2026-06-24 17:30:56.690897+00:00
+++ /home/gaetan/python_development_good_practices/sign_printer/utils.py        2026-06-24 23:36:58.904977+00:00
@@ -1,8 +1,9 @@
 """
 utils contains utilities for the sign_printer app.
 """
+
 import random
 
 USAGE = "Usage: python sign_printer <text>"
 
 
would reformat /home/gaetan/python_development_good_practices/sign_printer/utils.py

All done! ✨ 🍰 ✨
3 files would be reformatted, 2 files would be left unchanged.
```
**Note:** Just newlines to add


5. Cleaning with a bash command: `find`
   ```
   make clean
   ```
  **That's typically the command we want to include in a Makefile. It's long, you don't remember, characters are tedious to reproduce.Include it in a template can really save your time.**

  **Note:** 
  - The `find` command searches :
    - for all the whole directory `.`
    - all directories : `-type d`
    - directory with name: `-name` '__pycache__'
    - for all directories you will find, execute this command in just one command: `-exec rm -rf {} +`
    - `{}` is a placeholder: it captures all found results
    - `+` puts all the args in one command, not several commands with one argument

**`find` is a powerful command, it searches for recursively in all layers of your tree**

## Pre-commit tool and git hooks

**Pre-commits** is is a powerful tool particulary if you're collaborating with people in a repository.

*It's called pre-commits because it's essentially a script that runs before you do a git commit.*

This tool/software will let you run a script that is called **hooks** & the trigger is the commit.

SO it's really adopting this kind of shift left mentality to catch any errors before we commit to the repo.

These tools allow to avoid commits with dumb syntax errors, or indentation errors, your team will thank you because when a pipeline breaks, all the team receives an alert.

Pre-commits, linting, formatting avoid that...

### How does it work?

**Install pre-commit**:

To enable the pre-commit hook, you have to run the command `pre-commit install` in the environment where it's installed so:
```
uv run pre-commit install
```
This command informs us that :
```
pre-commit installed at .git/hooks/pre-commit
```
SO it created a folder in our .git folder.

When we run the previous command, the software is looking at the the default configuration YAML named `pre-commit-config.yaml` & try to analyze what we need to configure just before a commit.
Through the YAML we give to pre-commit package the pathes towards the scripts to execute.

### Build your YAML

That's in this file you will give all the instructions you want to before a commit.
It can be linting with flake8, formatting with black, specificity in your code. It can also be on a distant repo on Github (repo precommit-hooks, black,flake8) or a script/repo you have in local.
The options are large to build your yaml.
To interact with pre-commit software, the name of the YAML will always be ".pre-commit-config.yaml".

#### Parameters of a pre-commit-config.yaml

Here is a template on what looks like a `pre-commit-config.yaml`:
```yaml
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: check-added-large-files
-   repo: https://github.com/psf/black
    rev: 26.5.1
    hooks:
    -   id: black
-   repo: https://github.com/PyCQA/flake8
    rev: 7.3.0
    hooks:
    -   id: flake8
```

In .pre-commit-config.yaml - top level you have the `repos` parameter: that's the side where you define the parameters of repos mapping.
The repository mapping tells pre-commit where to get the code for the hook from.

For example, .pre-commit-config.yaml - repos parameters:

- `repo`: the repository url to git clone from or one of the special sentinel values: local, meta.

- `rev`: the revision or tag to clone at.
Note: you can retrieve this info in the repo of your software on Github in the `tags` menu.
Choose the version of the package you want to use.
**Note:** It's preferable to choose a version of your software which is the same to what you have in your environnment to avoid conflicts in your IDE.

- `hooks`:  A list of hooks mapping.
  The list of .pre-commit-config.yaml - hooks parameters are also pretty large .
  But you have to mention the `id` to help pre-commit to retrieve the hook in question.
  Often the hooks are theirselves in a yaml: `.pre-commit-hooks.yaml` which redirects to the script file.

  **Example:**

   in the pre-commit-hooks repo you have the yaml of all the hooks wrote by the community in https://github.com/pre-commit/pre-commit-hooks/blob/main/.pre-commit-hooks.yaml.

  All these `id` redirects to the real code in 'pre_commit_hooks folder with .py files:
  https://github.com/pre-commit/pre-commit-hooks/tree/main/pre_commit_hooks
  
  **All the informations are on this page at pre-commit website:**

  https://pre-commit.com/#plugins

### Git & hooks

#### Pre-commit method
It's git which redirects to a script when we commit.
In the .git directory of each git repo, we have the hooks whether pre-commit hooks or own hooks: that's in '.git/hooks'

- When you make: 
 ```
 pre-commit install
 ```
 and you've configured a .yaml, pre-commit package indicates how to find the scripts for the hooks. 

 For example, a pre-commit workflow under the hood:
   - configure your yaml
   - `pre-commit install`
   - GIt creates a script in `.git/hooks/pre-commit`
   - This script will redirect to the repos where are scripts before each `git commit`


#### With local scripts

- You can also create your own script and place it in `.git/hooks/`; then change your .yaml file this way:
 ```yaml
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: check-added-large-files
-   repo: https://github.com/psf/black
    rev: 26.5.1
    hooks:
    -   id: black
        args: [--target-version, py313]
-   repo: https://github.com/PyCQA/flake8
    rev: 7.3.0
    hooks:
    -   id: flake8
-    repo: local
     hooks:
     -  id: run-unit-tests
        name: Run Unit Tests
        entry: .git/hooks/run-unit-tests
        language: system
        pass_filenames: false
```

And i placed this script in the .git/hooks folder:
```bash
#!/usr/bin/env bash

make test
```
**Note:**

DOn't forget to make the script executable with:
```bash
chmod +x run-unit-test
```

**RECAP:**

So I recap the pre-commit hooks i expect for each of my commit:
- 4 scripts from pre-commit repo:
    - trailing-whitespace
    -  end-of-file-fixer
    -  check-yaml
    -  check-added-large-files
- 1 script from black repo which executes black with args(according to my python version)
- 1 script from flake8 repo to lint .py files
- 1 local script which handles tests

**Note:** I adapt passed versions in the yaml in function of last package versions found in PyPi to have the same packages in my environment and my hooks.(Maybe avoided conflicts with Pylance)


### Example of a git worflow with pre-commit hooks

#### Some tips with .yaml

1. Before initializing a commit pre-configured with pre-commit, always add your .yaml in your staging area:
   ```
   git add pre-commit-config.yaml
   ```

2. Always indent keys with same level , level of indentation is crucial if you don't want to an error
3. When you run a software on a repo, you can also simulate the command line with the parameter `args` 
   
**Example:** with black, to simulate:

```bash
black --target-version py313
```

Add for the black hook:

`args: [--target-version, py313]` in the .yaml file

#### pre-commit workflow

Our main concepts are linting, formatting, testing.
For each of one, we make a workflow to understand specificities:

**Linting**:
A common lint error is: **import a unused module**

1. I make this error in a file called `test_utils.py`.
2. I save the file.
3. I add the file to the staging area with the pre-commit-config.yaml: `git add`
4. I commit with a message
5. Here the output:
```
[WARNING] Unstaged files detected.
[INFO] Stashing unstaged files to /home/gaetan/.cache/pre-commit/patch1782593577-70788.
trim trailing whitespace.................................................Passed
fix end of files.........................................................Passed
check yaml...........................................(no files to check)Skipped
check for added large files..............................................Passed
black....................................................................Passed
flake8...................................................................Failed
- hook id: flake8
- exit code: 1

tests/test_utils.py:5:1: F401 'pytest' imported but unused

Run Unit Tests...........................................................Passed
[INFO] Restored changes from /home/gaetan/.cache/pre-commit/patch1782593577-70788.
```
**Notes**:
- flake8 detected the error and pre-commit indicated it failed
- the other hooks which succeed are 'passed' in face of their test software/scripts
- the useless tests are skipped (no YAML in the commit)
- flake8 doesn't modify the file like its behaviour in command line
- the commit is accepted isn't accepted by git if only one test doesn't pass

6. After the output we decide to delete the unused import in the .py file but but we make an error of formatting in leaving too much spaces between docstrings and imports and we save it.

**FOrmatting**:

7. We add the .py file again and commit it with message.
8. Here the output :
```
   [WARNING] Unstaged files detected.
[INFO] Stashing unstaged files to /home/gaetan/.cache/pre-commit/patch1782594519-72016.
trim trailing whitespace.................................................Passed
fix end of files.........................................................Passed
check yaml...........................................(no files to check)Skipped
check for added large files..............................................Passed
black....................................................................Failed
- hook id: black
- files were modified by this hook

reformatted tests/test_utils.py

All done! ✨ 🍰 ✨
1 file reformatted.

flake8...................................................................Passed
Run Unit Tests...........................................................Passed
[INFO] Restored changes from /home/gaetan/.cache/pre-commit/patch1782594519-72016.
```
**Notes**:
- The black hook has failed but has modified the file like its original behavior

9. The .py file is modified so we add it to the staging area again but we change another snippet of code to provoke an error for our tests.
10. We add the file we commit.
11. Here the output:
```
[WARNING] Unstaged files detected.
[INFO] Stashing unstaged files to /home/gaetan/.cache/pre-commit/patch1782595550-75507.
trim trailing whitespace.................................................Passed
fix end of files.........................................................Passed
check yaml...........................................(no files to check)Skipped
check for added large files..............................................Passed
black....................................................................Passed
flake8...................................................................Passed
Run Unit Tests...........................................................Failed
- hook id: run-unit-tests
- exit code: 2

uv run pytest --verbose tests/
============================= test session starts ==============================
platform linux -- Python 3.13.13, pytest-9.1.1, pluggy-1.6.0 -- /home/gaetan/python_development_good_practices/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /home/gaetan/python_development_good_practices
configfile: pyproject.toml
collected 3 items                                                              

tests/test_utils.py::test_fonts_are_strings FAILED                       [ 33%]
tests/test_utils.py::test_random_font_returns_a_random_font PASSED       [ 66%]
tests/test_utils.py::test_required_argument PASSED                       [100%]

=================================== FAILURES ===================================
____________________________ test_fonts_are_strings ____________________________

    def test_fonts_are_strings():
        """Fonts should be strings"""
>       assert all(isinstance(font, int) for font in FONTS)
E       assert False
E        +  where False = all(<generator object test_fonts_are_strings.<locals>.<genexpr> at 0x77812ef8dc40>)

tests/test_utils.py:10: AssertionError
=========================== short test summary info ============================
FAILED tests/test_utils.py::test_fonts_are_strings - assert False
========================= 1 failed, 2 passed in 0.02s ==========================
make: *** [Makefile:5 : test] Erreur 1

[INFO] Restored changes from /home/gaetan/.cache/pre-commit/patch1782595550-75507.
```  
**Note**: Pytest indicates the AssertionError line 10 but doesn't modify the file.
12. We fix the error but we add a newline to change the file.
13. Add, commit.
14. Here the output:
```
[WARNING] Unstaged files detected.
[INFO] Stashing unstaged files to /home/gaetan/.cache/pre-commit/patch1782596574-78686.
trim trailing whitespace.................................................Failed
- hook id: trailing-whitespace
- exit code: 1
- files were modified by this hook

Fixing tests/test_utils.py

fix end of files.........................................................Failed
- hook id: end-of-file-fixer
- exit code: 1
- files were modified by this hook

Fixing tests/test_utils.py

check yaml...........................................(no files to check)Skipped
check for added large files..............................................Passed
black....................................................................Passed
flake8...................................................................Passed
Run Unit Tests...........................................................Passed
[INFO] Restored changes from /home/gaetan/.cache/pre-commit/patch1782596574-78686.
```
**Notes:**
- The two hooks from pre-commit repo have modified the file.

15. Now we test precommit with a successful file we know it will work: we modify a little the docstrings from `sign_printer.py`
16. git add and commit.
17. Here the output:
```
[WARNING] Unstaged files detected.
[INFO] Stashing unstaged files to /home/gaetan/.cache/pre-commit/patch1782597251-79765.
trim trailing whitespace.................................................Passed
fix end of files.........................................................Passed
check yaml...........................................(no files to check)Skipped
check for added large files..............................................Passed
black....................................................................Passed
flake8...................................................................Passed
Run Unit Tests...........................................................Passed
[INFO] Restored changes from /home/gaetan/.cache/pre-commit/patch1782597251-79765.
[v6 57af7af] sign_printer.py: add docstrings precisions
 1 file changed, 2 insertions(+), 1 deletion(-)
 ```
 **Note:**
 - all the steps are passed or skipped
 - the commit is accepted

### some last tips with pre-commit

1. SOmetimes you don't want to search for the tags of the softwares you run in your yaml so after installing pre-commit in your .git folder:
```
uv run pre-commit install
```
To update all the versions of your tag repos to their latest versions:
```
uv run pre-commit autoupdate
```
2. To disable pre-commit hooks:
```
uv run pre-commit uninstall
```

## Conclusion

Automation tools like Makefiles and pre-commit hooks are powerful tools for automation.
THey allow :
- to gain time for repetitive processes 
- to avoid errors that can be integrated in important commits(for example work with a team in a pipeline)


That's important to have a shift left mentality in listing the concepts you want to integrate to your project:
- Define with your team the standardization to apply
- Think your automation tools in line with it
- Reverberate in a yaml all the tools you need for your precommits
  - test= pytest
  - lint= flake8
  - format = black
  - common patterns to correct: pre-commit-hooks repo
- Think about all the repetitive commands you don't want to rerun: make Makefiles
- Think about all you can automate

**Make changes,run tests, validate,commit: with automation tools it's even more integrated into your development workflow.**

Opening on :
- make aliases in your config files of your system: .zshrc, .bashrc:
  - git commit = gc
  - git status = gs
It's very long to write this each time.

#### Transition

To run softwares more securely, more portable way, with all our stuff within a container without fearing to retrieve an environment which is broken Monday morning.

The continuation of local automation to global automation assuring the reproductibility of our environment anywhere we can access a machine (local or remote).

That's the last milestone of an optimized app: [Containerization](https://github.com/DataScienceMyLove/python_development_good_practices/tree/v7/)
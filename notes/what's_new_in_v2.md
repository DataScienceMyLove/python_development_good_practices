# What's new in our repository?

## Improvements since v1

#### Repository:


1) we have a README, now we have informations about this repository:
  - Prerequisites to run the app
  - Usage of the app
  - How to run tests
   

2) we have a .gitignore which have to list all files we don't want to commit in our project: 
    - all unsignificant files/folders like cache files/folders (__pycache__,pytest_cache,.venv)
    - all sensitive informations in files like .env which can contain API keys from web/cloud services
     

#### Code:


3) a `tests/`directory which contains:
    - a `__init__.py`: That's a convention to signify that the directory `tests/` is a Python package, it doesn't to be empty usually there's going to be like important functionalities in there as well. Something like version a variable that shows the version of the package.Is it mandatory? Strictly speaking, it’s mandatory for Python, but it’s still strongly recommended for testing (Pytest) and build tools.
    If you fill it in, it’s to include internal imports to make life easier for whoever is going to use your code.
    For any Python developer who clones your project, the presence of __init__.py instantly signals: “This is the application’s source code”. It is a fundamental visual landmark.
    - `tests__utils.py`: the core of our tests.
    This follows the naming convention for pytest where you have your tests in a directory called 'tests'.
    And then you prefix your text filenames with `tests_`, so here we're testing the utils of the project.
    Contains a nice docstring...



4) `sign_printer`directory which contains the core logic of our app:
   - a `__init__.py` : That shows that's a package and we can access to the description of the package because __doc__ attribute will thanks to its docstring into it.
    Note: VSCode has access to it with its hover over feature that can allow to see the docs. Great!!
   - `sign_printer.py`: the v2 of the App.py v1
     - docstrings
     - imports at the top
     - shebang line : #! /usr/bin/env python3 (helps to find the interpreter for an executable file)
     - `main()` function with an entrypoint (if __name__=='__main__') when we want to execute by CLI
   - `utils.py`: That's a library that our `sign_printer.py` app imports from, differents fonts selected by a function, another function that validates the passed arguments from the CLI



5) All is not perfect but it works:
    - **sign_printer works**
    -
    ``` 
      .##.....##.########.##.......##........#######.
      .##.....##.##.......##.......##.......##.....##
      .##.....##.##.......##.......##.......##.....##
      .#########.######...##.......##.......##.....##
      .##.....##.##.......##.......##.......##.....##
      .##.....##.##.......##.......##.......##.....##
      .##.....##.########.########.########..#######.
      ```

    - **tests work:**
     
     ```
     =================================================================================================== test session starts ====================================================================================================
     platform linux -- Python 3.12.1, pytest-9.0.2, pluggy-1.6.0
     rootdir: /workspaces/python_development_good_practices
     plugins: anyio-4.12.1
     collected 3 items                                                                                                                                                                                                     

     tests/test_utils.py ...                                                                                                                                                                                              [100%]

     ==================================================================================================== 3 passed in 0.03s =====================================================================================================
     ```
  
## Persistent bad practices:

1) We advice to the user in the README to make :
   ```
   pip install pyfiglet
   ```
   That's a pretty bad practice, at least for a new comer.
   You generally avoid to messing with your Python system packages & we usually want to do this within a container or a virtual environment.


2) Other detail:
    ```
    python sign_printer/sign_printer.py <text>
    ```
    Better to be more expressive with the version of Python: `python3`


3) Presence of several `__pycache__`folders il a yellow/red flag in a repository.
   A cache file has absolutely no business being on GitHub
  

**Transition**:
We 're going to capture a lot of errors thanks to the unit tests and pytest in sight of cleaning development pipelines towards production.

But there are more steps to go forward for cleaning up our Python code more in depth. 

Some of them are: [Linting & formatting](https://github.com/DataScienceMyLove/python_development_good_practices/tree/main/notes/linting_formatting.md)
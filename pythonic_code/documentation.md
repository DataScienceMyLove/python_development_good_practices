# Documentation

[PEP257](https://peps.python.org/pep-0257/) talks about **docstrings** convention.

That's a must-do in every function, classes, methods, modules, packages, you have to inform what your object does.

---

## Built-in Functions and Docstrings

Built-in functions have their docstrings.

For each object mentioned above, you can access its docstrings by the **dunder attribute** `__doc__`.

Besides, you can retrieve it when you call the `dir()` built-in function of the object.

---

## Example: Understanding Docstrings

### Starting Point

We are coming back on the [mypy_example.py](/pythonic_code/mypy_example.py)

We are adding a docstring to our function:

```python
"""
This is my app!!!
"""

def hello(name: str,age: int) -> str:
    """
    This function takes a name and an age as input and returns a greeting message.
    """
    return f"Hello {name}, you are {age} years old!"

if __name__ == "__main__":
    print(hello("Alice", 30))
    print(hello("Bob", 25))
    print(hello("Charlie", 35))
```

### In the Terminal

Then we're going in the terminal to launch a REPL in the same directory of our .py file:

```bash
python3
```

Import the module:

```REPL
>>>import mypy_example
```

### Using dir() to Explore

Then use the `dir()` keyword:

```REPL
>>>dir(mypy_example)
```

**Outputs:**

```
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'hello']
```

You retrieve the `hello()` function you created and the `__doc__` dunder attribute.

### Accessing Module Docstrings

You verify the theory:

```REPL
>>>mypy_example.__doc__
```

**Outputs:**

```
'\nThis is my app!!!\n'
```

Here is the docstring for the module.

### Accessing Function Docstrings

And for the function:

```REPL
>>>mypy_example.hello.__doc__
```

**Outputs:**

```
'\n    This function takes a name and an age as input and returns a greeting message.\n    '
```

---

## Important Notes

**The `help()` built-in function:** The `help()` built-in function is tied with `__doc__`. It uses it in a manual page with a better presentation without escape characters.

**The `__pycache__` folder:** A `__pycache__` folder appears when you import a .py module file. It contains precompiled files in bytecode for the interpreter. There is no interest to keep it in your repository...

---

**Another example of good practices with documentation at the repo/project level is: build [a well-documented README.md](/notes/why_a_README.md)**
# Writing Pythonic Code

## What is Pythonic Code?

There is something called **Python Enhancement Proposals** (alias **PEP**) & among those PEP, the famous **PEP8** which talks about code style.

If you're in a battle with a colleague and you are talking about: "Should we use tabs or space?" ==> [Go the pep8 website "source of truth" of all PEP8 believers](https://peps.python.org/pep-0008/)


### PEP8 Standards

All these rules like:
- indentation
- maximum line length
- spaces
- docstrings
- etc

are the references of linting & formatting tools like Flake8 or Black.

### Beyond PEP8

**But Pythonic code ISN'T JUST PEP8.**

It's built by the mantra that readability matters, and that you can understand the code without being a Python developer.

---

## Pythonic Code Examples

[Here what to expect of a Pythonic code through data structures and concepts](pythonic_examples.py)

---

## Type Hinting

### Benefits of Type Hinting

- Integration with IDEs
- Documentation in the code itself
- a package like MyPy can detect problems before it arrives
  

### Purpose

In an interview, type hinting allows you to stand out and levels up the code quality of team projects.

When a codebase becomes complex or when you're trying to just start out on the right feet, using type hinting can be very valuable because mixing types can lead to unexpected behaviors.

Tools like `MyPy` can detect any potential type mismatches.

#### MyPy Tool: Static Type Checking

**MyPy with type hinting is a powerful combo.** Python is becoming almost a typed language.

##### Historical Context

Historically, Python has been a dynamically typed language. You create a variable, put whatever you like into it, and it's at runtime that Python checks whether or not it causes a crash.

##### How MyPy Works

MyPy introduces the concept of **static type checking**. It doesn't change the way Python executes your code (Python remains dynamically typed at runtime), but it acts as a safeguard before execution (often directly within your IDE or in your CI/CD pipeline).

Type hinting (standardised by PEP 484) allows code to be documented by the code itself, so it makes stronger the Pythonic concept: "Readability counts"

---

## Practical Example: MyPy in Action

### 1. Define a Function with Type Hints
```python
def hello(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old!"

print(hello("Alice", 30))
print(hello("Bob", "25"))
print(hello(123, "Bob"))
```

### 2. Running Without Type Checking

```bash
python mypy_example.py
```

**Output:**
```
Hello Alice, you are 30 years old!
Hello Bob, you are 25 years old!
Hello 123, you are Bob years old!
```

**Exit code:**
```bash
echo $?
# Returns: 0 (success - no errors detected)
```

### 3. Running With MyPy

Install MyPy:
```bash
pip install mypy
```

Run MyPy analysis:
```bash
mypy mypy_example.py
```

**Output:**
```
mypy_example.py:5: error: Argument 2 to "hello" has incompatible type "str"; expected "int"  [arg-type]
mypy_example.py:6: error: Argument 1 to "hello" has incompatible type "int"; expected "str"  [arg-type]
mypy_example.py:6: error: Argument 2 to "hello" has incompatible type "str"; expected "int"  [arg-type]
```

**Exit code:**
```bash
echo $?
# Returns: 1 (failure - type errors detected)
```
### Key Takeaways

**MyPy has detected in CLI all unexpected types in each function call where it mismatches.**

Without MyPy, types are **implicit**. With MyPy, they become **explicit**.

MyPy helps catch bugs before they make it into production. For example, if you accidentally pass an integer to a function that expects a string, MyPy will flag this immediately whilst you're coding, saving you from a crash later on.

#### Advantages of Using MyPy

- You can run MyPy on a whole package
- We could integrate it into CI/CD pipelines or into a pre-commit hook

So we can catch these potential type mismatches before we deploy our code.
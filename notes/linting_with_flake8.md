# Linting with Flake8

### How does flake8 work?

**Download the package by opening your terminal:**
```
pip install flake8
```

**Verify it's on your system:**
```
flake8 --version
```

**Use it in your repository at the root or the folder you want to test:**
```bash
flake8
```

That's the basic workflow to use flake8.

### How does it work?

**Flake8** identifies all issues in your .py files and displays them in the terminal.

**For example:**

Running flake8 in a working directory with tests and sign_printer folders:

```
flake8
```

**Output:**
```
./sign_printer/utils.py:82:17: W292 no newline at end of file
./tests/test_utils.py:4:1: F401 'pytest' imported but unused
./tests/test_utils.py:9:1: E303 too many blank lines (3)
```

The output shows:
- All .py files where flake8 has reported errors
- Error codes (E303, F401, W292)
- Line number and character position in the file (test_utils.py:4:1)

It's easy to retrieve and fix the errors once you identify them.

**For example:** To fix the W292 error in utils.py:
1. Go to line 82, character 17
2. Add a newline at the end of the file
3. Run flake8 again—the error will no longer appear

By default, **flake8** does not modify files with style errors; you must fix them manually.

### What are the encoded errors based on?

All error codes are documented here: https://pep8.readthedocs.io/en/release-1.7.x/intro.html#error-codes

This link is also referenced in the `.flake8` file.

#### The .flake8 file

The `.flake8` file is how you configure flake8 to choose which errors to check and which files to exclude from scanning.

**Parameters:**

- `ignore =` parameter: Specify error codes you want to ignore from the error list
  
    Example:
    ```
    ignore = W292,F401
    ```
    This will ignore "no newline at end of file" and "imports not used in the module" during the scan.

- `exclude=` parameter: Exclude specific files or directories from the scan
 
    Example:
    ```
    exclude = git,
              __pycache__,
              .venv,
              build,
              dist
    ```

#### Help with flake8

Flake8 is a highly configurable tool. For more configuration options, run:

```bash
flake8 --help
```

#### Alternative configuration methods

**Developer tip:** To avoid typing configuration commands every time, you can centralize the configuration in a `pyproject.toml` or `setup.cfg` file in the root directory of your project.

The approach depends on your project's goals and whether you're building a package.

#### Consequences of a non-linted project

1. **Simple bugs go unnoticed**

    Example:
    ```python
    import json

    def process_data(data):
        result = parse_data(data)
        return results
    ```

    A linter would flag:
    - `json` is imported but never used
    - `results` is not defined (probably a typo for `result`)

    Without linting, you'll only discover these errors at runtime.

2. **Performance issues:** Unused imports have a cost. Many unused imports can impact performance.

3. **CI/CD pipelines:** In a CI/CD pipeline, you'll waste time fixing simple formatting issues. Linting catches these early, saving time and improving your workflow.


**Transition**:
Another tool which can help to avoid errors upstream in a pipeline and based on pythonic code, readibility: [**Black**](/notes/formatting_with_black.md)
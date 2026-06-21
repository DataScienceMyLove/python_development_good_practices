# Linting with Flake8

### How does flake8 work?

**Download the package in opening your terminal:**
```
pip install flake8
```
**Verify it's on the system:**
```
flake8 --version
```
**Use it in your repository at the root or the folder you want to test:**
```bash
flake8
```
That's the basic workflow to use flake8.

### How does it act?

**Flake8** points in each .py file all the issues in the code through .py files in terminal.

For example:

I run on my working directory where we have my tests and sign_printer folders:
```
flake8
```
**Outputs:**
```
./sign_printer/utils.py:82:17: W292 no newline at end of file
./tests/test_utils.py:4:1: F401 'pytest' imported but unused
./tests/test_utils.py:9:1: E303 too many blank lines (3)
```
- All the .py files where flake8 have repertoried errors are listed 
- The errors are encoded (E303,F401,W292)
- The line and the number of the line character in the file are spotted(test_utils.py:4:1:)

So it's easy to retrieve the errors and rectify them

By example, We want to rule the W292 in utils.py.

We go in the file, line 82, character 17 and we add a newline.

**flake8** will stop to list this error the next time we run it.

So yes; by default, **flake8** doesn't modify the files which have errors of style and it seems to me that we can't configure it to do it.*

### On what flake8 is based for the encoded errors?






# Formatting with Black

Formatting is more about **standardization** than linting.

The two are often confused because they run at the same time (often when saving or before a commit), but they serve completely different purposes.

To put it simply: the linter assesses the **quality** and **security** of your code, whilst the formatter deals solely with its appearance and this is guided by PEP8.

Linting applies PEP8 and adds a layer of security (forecasting bugs before they arrive); formatting fully respects PEP8 guidelines.

### How does Black work?

Black is a pretty cool project, though aging by 2026.

Moreover, it can be replaced by Ruff, which is an alternative to the combo Black+Flake8.

It integrates very well into pyproject.toml, like mypy (natively).

**Workflow**:

Install:
```
pip install black
```
Run it in your working directory where you want to use black:
```
black sign_printer
```
Outputs:
```
reformatted /home/gaetan/python_development_good_practices/sign_printer/sign_printer.py
reformatted /home/gaetan/python_development_good_practices/sign_printer/utils.py

All done! ✨ 🍰 ✨
```
Two files in our app folder are reformatted. 

Unlike mypy or flake8, black modifies the .py files it finds.

For our 2 modified files:

```
git diff sign_printer/utils.py
```
```
"""
utils contains utilities for the sign_printer app.
 """
+
 import random
 
 USAGE = "Usage: python sign_printer <text>"
@@ -79,4 +80,4 @@ def validate_args(args):
     """Validates the arguments passed from the command-line."""
     if len(args) > 1:
         return True
-    return False
\ No newline at end of file
+    return False
```
Results:
- Addition of a newline between docstrings and first import
- Addition of a newline at the end of the file

```
git diff sign_printer/sign_printer.py
```
```
def main():
     """Main function gets called when invoked from the command-line"""
     figlet = Figlet(font=utils.random_font())
-    text_to_print = ' '.join(sys.argv[1:])
+    text_to_print = " ".join(sys.argv[1:])
     print(figlet.renderText(text_to_print))
```
Results:
- Black replaces `''` with `""`

### Configure black

Manual page of black:
```
black --help
```

An example of the most commonly used feature:
```
black --diff
```
Result:
You can print out the difference in the terminal before/after a black command without making any changes to the files directly, like before.

#### Restore the repo or a file

```
git restore [<file>]
```
Restore any changes after a modification or after a black command that you want to undo.

**Transition:**

Black can be natively integrated into a package's pyproject.toml.

First, we need [virtual environments](https://github.com/DataScienceMyLove/python_development_good_practices/tree/main/notes/virtual_environments.md) that isolate dependencies from the Python of our system, a reproducible environment where all the dependencies can be retrieved in one command to avoid multiple 'pip install' calls.


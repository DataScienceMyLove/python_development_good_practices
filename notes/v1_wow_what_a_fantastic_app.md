# Version 1: Wow, What a Fantastic App

## The Starting Point

That's our wonderful first version.

If you're a software/Python developer, you flee this repo in the same second you enter it.

We're going to do an exhaustive list of what's going wrong—or we can simply say: it exists!

---

## Issue 1: No README.md

**The README.md is the plan of your project when entering on your repo.**

Without it, there is no purpose for your project and no interest from others.

---

## Issue 2: Poor Commit Messages

If you refer to the App.py file in the repo, you observe the tied commit message 'blah blah'. Without judging its capabilities, the developer could surely have a better descriptive message for this commit.

**A commit message has to be descriptive of what it changes on the repo.**

### Good Example

```
"fix: linting on file.py"
```

### Why This Matters

It's better if it encompasses less files possible—if you create a bug, it will be simpler to come back to this commit to retrieve the cause.

Keep it simple & stupid (KISS) and as atomic as possible.

**Other problem:** if a professional arrives on this repo, their opinion of you will plummet. ([professionalism](https://github.com/DataScienceMyLove/python_development_good_practices/blob//main/notes/readability.md) remember)

If it's your interviewer, they think: "this person is lazy"; "collaboration—"

---

## Issue 3: File Naming Conventions

In the repo we can see that the name of the .py file is `App.py`.

**The casing is important when you name files.**

A lot of devs from the data science community like to capitalize the first letter of a filename. This can create troubleshooting issues later when you believe you named `app.py`.

---

## Issue 4: Code Quality in App.py

### Current Content

```python
from pyfiglet import Figlet
f= Figlet(font = "slant")
import sys
s = sys.argv[1]

print(f.renderText(s))
```

### Problems Identified

- The code begins at line 3
- The equals treatments are not uniformized
- No space between `=` and the variable `f`
- Too many spaces for `=` in the parameters' definition
- A variable assignment between the modules' imports
- No information about what the module/app makes: no docstrings
- Zero information about this pyfiglet module (which is not very famous)

---

## Conclusion

All of these observations lead us to the key question: ***How to write Pythonic code?***

A code agreed upon by most Pythonistas.
# What's new in v4?

### Changes compared to v3

- The README.md incorporates a tutorial for the user to handle virtual environment and reproduce the project on his machine.
- `pip install` repetition disappeared
- a `requirements.txt` with pinned package versions appeared in the repository

#### What doesn't change?

- The code is the same
- tests/linting/formatting

**Note**: A little error is on the README, we downloaded `virtualenv` which is an old package to manage virtual environments with more features than the module venv of the standard library.
But we use the venv module of the standard library, the 2 tools aren't the same tool, `virtualenv` is a third-party package.

### Some problems still

- In the requirements.txt, the development and production dependencies are not separated: the user is going to download useless packages for its user experience.


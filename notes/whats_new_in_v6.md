# What's new in v6?

**Repository changes:**

- we have `.python-version`,`uv.lock`,`pyproject.toml`: these 3 files are present to reproduce the environment
- we have a Makefile that automates tasks
- we have a .pre-commit-config.yaml: a config file followed by the pre-commit package which accomplishes hooks before a commit: you can lint, format your files.
- we changed of package manager, we prefer to use `uv`instead of `poetry`:Why?
  - it's almost the same commands with same PEP517 including pyproject.toml
  - uv is built in Rust, it's faster
  - uv can manage python versions in a easy way
Some tips [here](/notes/some_uv_tips.md) to make the transition.


Concepts added:
- **Automation:**
  -  We simplified the worflow in adding a **Makefile** which allow to make big commands simpler with simple name targets which resume the action to realize.
  -  we automated actions like linting,formatting before committing with hooks in git workflows or pre-commit configuration with pre-commit package and a .yaml file.
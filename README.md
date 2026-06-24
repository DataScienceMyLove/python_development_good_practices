# sign_printer

This is a simple Python command-line application that uses the `pyfiglet` library to generate ASCII art from the text entered by the user.

### Installation and Usage
```
# pip
python -m pip install poetry

# macOS
brew install poetry

# Linux / Windows
curl -sSL https://install.python-poetry.org | python3 -
```

### Initialize
```
poetry init
```

### Install dependencies
```
poetry install # install dependencies, doesn't remove packages from environment
poetry sync # sync the environment strictly with .lock
```
### Synchronize pyproject.toml and poetry.lock
```
poetry lock
```

### Activate virtual environment
```
eval $(poetry env activate)
```

### Deactivate virtual environment
```
deactivate
```

### Run the app
```
poetry run python sign_printer/sign_printer.py <text>
```

### Add a package
```
poetry add pyfiglet
```
### Remove a package 
```
poetry remove pyfiglet
```
### Uninstall
```
# pip
python -m pip uninstall poetry

# macOS
brew uninstall poetry

# Linux / Windows
curl -sSL https://install.python-poetry.org | python3 - --uninstall
```
Note: if you want the complete workflow to create a project with dependencies management with [poetry](/notes/workflow_with_poetry.md) or [uv](/notes/workflow_with_uv.md), follow the instructions.
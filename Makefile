example:
	@uv run python sign_printer/sign_printer.py hello

test:
	uv run pytest --verbose tests/

lint:
	uv run flake8 --show-source

format:
	uv run black --diff --target-version py313 .

clean:
	find . -type d -name '__pycache__' -exec rm -rf {} +
	find . -type d -name '.pytest_cache' -exec rm -rf {} +

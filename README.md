# PyTamaro
![Test](https://github.com/LuCEresearchlab/pytamaro/workflows/Test/badge.svg)
![Lint](https://github.com/LuCEresearchlab/pytamaro/workflows/Lint/badge.svg)
![TypeCheck](https://github.com/LuCEresearchlab/pytamaro/workflows/TypeCheck/badge.svg)

PyTamaro is a Python educational library designed for teaching **problem decomposition** using **graphics**.

[API Documentation](https://pytamaro.readthedocs.org)

## Development

This project is managed using [Poetry](https://python-poetry.org/).
After cloning the project, you can install the dependencies with `poetry install`.

Mention your changes in the `CHANGELOG.md` file.

## Test, TypeCheck, Style Guidelines

We use `pytest` to execute our test suite (written in the `tests` folder). Verify that all tests pass by calling;
```bash
poetry run pytest tests
```

We use `pylint` and `pycodestyle` to uniform our style. Make sure they report no errors by running:
```bash
poetry run pylint pytamaro
poetry run pycodestyle .
```

We use `pyright` to type check our code. Verify that it reports no errors:
```bash
poetry run pyright
```

## Release a new version

- Make sure you have installed `bumpversion`: `poetry self add poetry-bumpversion`.
- Execute the relevant poetry command to bump the version (e.g., `poetry version patch --dry-run`).
- Move the changes in `CHANGELOG.md` from "unreleased" to the proper version
- Commit and push the new version
- Publish the new version on PyPI using `poetry publish`.
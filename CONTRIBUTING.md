## How to setup your environment for development

This project is managed using [uv](https://docs.astral.sh/uv/).

### Install dependencies

```sh
# Base dependencies
uv sync
# Dev dependencies
uv sync --group dev pyproject.toml
```

## Test, TypeCheck, Style Guidelines

We use `pytest` to execute our test suite (written in the `tests` folder). Verify that all tests pass by calling;

```sh
uv run pytest tests
```

We use `pylint` and `pycodestyle` to uniform our style. Make sure they report no errors by running:
```sh
uv run pylint pytamaro
uv run pycodestyle .
```

We use `pyright` to type check our code. Verify that it reports no errors:
```sh
uv run pyright
```

## How to build the documentation

The documentation can be built in different formats. For example, we can build the HTML version:

```sh
cd docs
make html
```

The homepage will be available at `_build/html/index.html` (inside the `docs` folder).

## When developing

- Mention your changes in the `CHANGELOG.md` file.

## How to release a new version

- Upgrade the version in `pyproject.toml` and `__init__.py`.
- Upgrade the version in `docs/conf.py` and `docs/judicious_transformer.py`
- Move the changes in `CHANGELOG.md` from "unreleased" to the proper version
- Commit and push the new version
- Build the new version using `uv build`.
- Publish the new version on PyPI using `uv publish`.
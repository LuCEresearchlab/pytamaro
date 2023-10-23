## How to setup your environment for development

This project is managed using [Poetry](https://python-poetry.org/).
After configuring Poetry on your operating system, you can install the dependencies using

```sh
poetry install
```

## Test, TypeCheck, Style Guidelines

We use `pytest` to execute our test suite (written in the `tests` folder). Verify that all tests pass by calling;

```sh
poetry run pytest tests
```

We use `pylint` and `pycodestyle` to uniform our style. Make sure they report no errors by running:
```sh
poetry run pylint pytamaro
poetry run pycodestyle .
```

We use `pyright` to type check our code. Verify that it reports no errors:
```sh
poetry run pyright
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

- Make sure you have installed `bumpversion`: `poetry self add poetry-bumpversion`.
- Execute the relevant poetry command to bump the version (e.g., `poetry version patch --dry-run`).
- Move the changes in `CHANGELOG.md` from "unreleased" to the proper version
- Commit and push the new version
- Publish the new version on PyPI using `poetry publish`.
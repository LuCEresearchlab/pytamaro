## How to setup your environment for development

We use [Poetry](https://python-poetry.org/) to manage the dependencies.
After configuring Poetry on your operating system, you can install them using

```sh
poetry install
```

## How to run tests

```sh
poetry run pytest
```

## How to run the linter

```sh
poetry run pylint pytamaro
poetry run pycodestyle .
```

## How to run the type checker

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

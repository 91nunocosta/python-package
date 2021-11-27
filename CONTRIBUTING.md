
# Preparing the development environment

If you want to test or change the source code, prepare your local environment.

1. Clone the repository.

   ```bash
   git clone git@github.com:91nunocosta/python-package.git
   ```

2. Open the project directory.

   ```bash
   cd python-package
   ```

3. Install [_poetry_](https://python-poetry.org/) _package and dependency manager_.
Follow the [poetry installation guide](https://python-poetry.org/docs/#installation).
Chose the method that is more convenient to you, for example:

   ```bash
   curl -sSL\
        https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py \
      | python -
   ```

4. Create a new virtual environment (managed by _poetry_) with the project dependencies.

   ```bash
   poetry install
   ```

5. Enter the virtual environment.

   ```bash
   poetry shell
   ```

# Suggesting changes

If you want to add a new feature, fix some bug, improve the documentation
or enhance the CI/CD, open a
[Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).

Make sure your PR passes the _quality assurance_
[check](https://github.com/91nunocosta/python-package/actions/workflows/check.yml).
Otherwise, the Pull Request can not merge. The check consists of 2 phases:

1. try [pre-commit](https://pre-commit.com/).

2. try [tox](https://tox.wiki/en/latest/index.html).

## Pre-commit

Pre-commit runs the linters and tests configured in
[.pre-commit-config.yaml](./.pre-commit-config.yaml).
You can check the _pre-commit_ phase locally:

1. Prepare the development environment, as described in
[**Preparing the development environment**](#preparing-the-development-environment).

2. Run pre-commit with all files.

```bash
pre-commit --all-files
```

## Tox

Tox builds the package and tests it with the python version configured in [tox.ini](./tox.ini).
You can check the _tox_ phase locally:

1. Prepare the development environment, as described in
[**Preparing the development environment**](#preparing-the-development-environment).

2. Run tox.

```bash
tox
```

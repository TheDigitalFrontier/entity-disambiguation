# ac297r-entity-disambiguation

## Development
### 1. Install Poetry (once)
We use [Poetry](https://python-poetry.org/), a Python packaging, dependency, and virtual environment manager to streamline development and use of our code. Follow the [instructions](https://python-poetry.org/docs/#installation) to install and set up Poetry. Do not install Poetry using Homebrew.

### 2. Setting up your local development environment (once)
Clone the repo and set it as your current working directory

    $ git clone git@github.com:TheDigitalFrontier/entity-disambiguation.git
    $ cd entity-disambiguation

Install dependencies and create virtual environment

    $ poetry install

Set up the new virtual environment as a Jupyter Notebook kernel. You can set the kernel name `--name ac297r` to what you want, but for consistency the suggested name is recommended.

    $ poetry run python -m ipykernel install --user --name ac297r

Install pre-commit hooks for code style. Every time you perform a `git commit`, the pre-commit hooks will run to sort dependencies and ask you to fix changes they can't apply automatically

    $ poetry run pre-commit install

### 3. Contributing code (every time)
(Optional) to use the virtual environment with these dependencies

    $ poetry shell

To use the virtual environment as your kernel in Jupyter Notebook

# TODO

Make sure you have the latest code in `master`

    $ git checkout master
    $ git pull

Create a new branch to do your work

    $ git checkout -b <your-branch-name>

After developing your code, check that tests pass

    $ poetry run pytest 

Push your branch to Github. Follow the instructions in your terminal to set the remote, if necessary

    $ git push -u origin <your-branch-name>

Go to Github and [create a new Pull Request](https://github.com/TheDigitalFrontier/entity-disambiguation/pulls) to have your branch merged into master, assuming all CI/CD build tests pass.

#### Miscellaneous notes
- When first introducing new hooks, run `poetry run pre-commit run --all-files` manually to run through and apply checks to *all* files, not just .py files.
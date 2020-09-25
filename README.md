# ac297r-entity-disambiguation

## Development
### 1. Install Poetry
We use [Poetry](https://python-poetry.org/), a Python packaging, dependency, and virtual environment manager to streamline development and use of our code. Follow the [instructions](https://python-poetry.org/docs/#installation) to install and set up Poetry.

### 2. Setting up your local development environment
Clone the repo

    $ git clone git@github.com:TheDigitalFrontier/entity-disambiguation.git
    $ cd entity-disambiguation

Install dependencies and create virtual environment

    $ poetry install

Install pre-commit hooks for code style. Every time you perform a `git commit`, the pre-commit hooks will run to sort dependencies and ask you to make necessary style changes

    $ poetry run pre-commit install

### 3. Contributing code
(Optional) to use the virtual environment with these dependencies

    $ poetry shell

Make sure you have the latest code in `master`

    $ git checkout master
    $ git pull

Create a new branch to do your work

    $ git checkout -b <your-branch-name>

After developing your code, check that tests pass

    $ poetry run pytest 

Push your branch to Github. Follow the instructions in your terminal to set the remote, if necessary

    $ git push -u origin <your-branch-name>

Go to Github and [create a new Pull Request](https://github.com/TheDigitalFrontier/entity-disambiguation/pulls) to have your branch merged into master, assuming it passes the CI/CD build tests!
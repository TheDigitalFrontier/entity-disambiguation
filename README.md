# ac297r-entity-disambiguation

## Development
### 1. Install Poetry (once)
We use [Poetry](https://python-poetry.org/), a Python packaging, dependency, and virtual environment manager to streamline development and use of our code. Follow the [instructions](https://python-poetry.org/docs/#installation) to install and set up Poetry. Do not install Poetry using Homebrew.

### 2. Setting up your local environment (once)
Clone the repo and set it as your current working directory

    $ git clone git@github.com:TheDigitalFrontier/entity-disambiguation.git
    $ cd entity-disambiguation

Install dependencies and create virtual environment

    $ poetry install

Set up the new virtual environment as a Jupyter Notebook kernel. You can set the kernel name `--name ac297r` to what you want, but for consistency the suggested name is recommended.

    $ poetry run python -m ipykernel install --user --name ac297r

Install pre-commit hooks for code style. Every time you perform a `git commit`, the pre-commit hooks will run to sort dependencies and ask you to fix changes they can't apply automatically

    $ poetry run pre-commit install

### 3. Running code (every time)
(Optional) To use the virtual environment with the specified dependencies, for instance to run a `.py` script directly in terminal

    $ poetry shell

To use the virtual environment as your kernel in Jupyter Notebook, launch `jupyter-notebook` as you normally do, then open or create a notebook, click `Kernel`, `Change kernel`, and select `ac297r` (or the kernel name you chose previously).

### 4. Managing dependencies (every time)
**Use Poetry** to manage dependencies and your virtual environment. This way other contributors can run and build on your work without having to debug or struggle with dependencies. Consistency is key.

Add or remove dependencies using Poetry. See the full documentation [here](https://python-poetry.org/docs/cli/#add). For instance, to install numpy in the virtual environment:

    $ poetry add numpy

If a package is used only for development but is not necessary to run the code, add it using the `--dev` flag so that users of the published package only install the packages they need. For instance, `pytest` is already installed as a dev dependency as only code contributors need it.

### 4. Contributing code (every time)
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
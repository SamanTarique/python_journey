# Using $ python3 -m venv

$ pyenv install 3.10.1
$ pyenv local 3.10.1
$ python3 -m venv my_env ( env with local python version )
$ source my_env/bin/activate
$ (my_env) deactivate

** this type of env setup creates a new folder in your current directory **

# Using $ pyenv virtualenv my_env

$ pyenv install 3.10.2
$ pyenv virtualenv 3.10.2 my_env
$ pyenv virtualenvs
$ cd my_proj

my_proj$ pyenv activate my_env (Recommended)
$ pyenv deactivate

my_proj$ pyenv local my_env (Not Recommended)
rm .python-version
** This type where we activate using local creates a file .python-version and whenever you comes in this dir the env will activate automatically

(my_env) my_proj$ python3 --version
>> 3.10.2

# Using conda

$ conda create --name my_env python=3.10.3
$ conda info --list
$ conda activate my_env
$ conda deactivate

# Using uv

$ curl -LsSf https://astral.sh/uv/install.sh | sh

# creates new proj dir uv_proj with few tiles like .gitignore, pyproject.toml
$ uv init uv_proj

# creates a virtual env automatically as .venv in directory
$ uv run main.py

# if you want to update the python version , update in .python-version file and simple run the main file
$ uv run main.py 

# install packages using uv
$ uv add fastapi flask






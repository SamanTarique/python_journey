import os

cwd = os.getcwd()
dir_path = os.path.join(cwd, 'newDir')

os.rmdir(dir_path)

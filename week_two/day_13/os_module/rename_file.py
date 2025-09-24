import os

cwd = os.getcwd()
cwd = os.path.join(cwd, 'hero')

os.rename(cwd, 'heroo')

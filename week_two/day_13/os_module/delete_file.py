import os

cwd = os.getcwd()
file_path = os.path.join(cwd, 'file.txt')

os.remove(file_path)

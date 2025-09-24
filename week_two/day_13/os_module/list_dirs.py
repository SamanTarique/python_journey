import os

cwd = os.getcwd()

#  parent directory
cwd = os.path.join(cwd, '../')

"""files and directories in current directory"""
print(f"{os.listdir()}")

"""files and directory in parent directory"""
print(f"{os.listdir(cwd)}")

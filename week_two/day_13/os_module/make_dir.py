import os

current_path = os.getcwd()
print(f"current working directory is -{current_path}")

"""creating a new directory"""

new_dir = os.path.join(current_path, 'newDir')
os.mkdir(new_dir)

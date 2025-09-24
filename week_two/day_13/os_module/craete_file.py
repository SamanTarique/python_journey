import os

cwd = os.getcwd()
file_path = os.path.join(cwd, 'file.txt')

with open(file_path, 'w') as file:
    file.write("Anurodh kumar")

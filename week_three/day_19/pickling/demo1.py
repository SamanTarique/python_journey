import os
import pickle

my_list = [1] * 10
# print(my_list)
# pickled_data = pickle.dumps(str(my_list))

# print(pickled_data)

# print(pickle.loads(pickled_data))


# file = open("pickled_file.txt", "ab")

# pickle.dump(my_list, file)

# file.close()

# file_content = open("pickled_file.txt", "rb")

# print(pickle.load(file_content))

# file_content.close()

current_path = os.getcwd()
file_path = os.path.join(current_path, "with_file.txt")

with open(file_path, "a+") as file:
    file.write("ninja hattori\n")

with open(file_path, "r") as file:
    file.seek(0)
    print(file.read())

import json
import os

json_object = {
    "firstname": "anurodh",
    "lastname": "kumar",
    "age": 24,
    "role": "developer",
}

file_path = os.path.join(os.getcwd(), "jsonfile.json")

with open(file_path, "a") as file:
    file.write(json.dumps(json_object, indent=4) + "\n")
    # json.dump(json_object, file, indent=4)

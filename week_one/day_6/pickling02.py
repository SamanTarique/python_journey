import pickle

d = {1: "anurodh", 2: "kumar", 3: "python", "a": "hello", "b": "world"}

db_file = open("myBinaryStreamFile", "wb")
pickle.dump(d, db_file)
db_file.close()

print("serialization done using file")

print("desearilize and reading the contents")

reading_file = open("myBinaryStreamFile", "rb")
file = pickle.load(reading_file)
reading_file.close()
print(f"Contents - {file}")

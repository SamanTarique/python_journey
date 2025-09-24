import pickle

d = {1: "anurodh", 2: "kumar", 3: "python", "a": "hello", "b": "world"}

"""Serializing the object"""
serilize_obj = pickle.dumps(d)
print(type(serilize_obj))
print(serilize_obj)

"""De-serializiig the Object"""
deserialize_obj = pickle.loads(serilize_obj)
print(type(deserialize_obj))
print(deserialize_obj)

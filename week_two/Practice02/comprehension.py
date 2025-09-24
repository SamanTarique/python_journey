"""Squares of even numbers"""
# a = [1,2,3,4,5,6,7,8]
# print([i ** 2 for i in a if i % 2 == 0])
# q = [lambda x=i: x**2 for i in a if i % 2 ==0]
# li = []
# st = set({})
# dt = {}
# for i in q:
#     li.append(i())
    # st.add(i())
    # dt.update({i: i()})
# print(li,st,dt)

"""create a set of unique vowels present in a string"""
# string = "pythoncomprehension"
# vowels = ['a','e','i','o','u']

# print(set([i for i in string if i in vowels]))

"""Given ["a", "b", "c", "d"], make a dictionary where key = index, value = element."""

# a = ["a", "b", "c", "d"]
# print({key: value for key, value in enumerate(a)})


"""From ["hello", "world", "python", "rocks"], build a dictionary mapping each word to its length."""
a=["hello", "world", "python", "rocks"]
print({value: len(value) for key, value in enumerate(a)})


"""Create a list of numbers between 1–100 that are divisible by both 3 and 5."""
print([i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0])


"""Given [[1,2,3], [4,5], [6,7,8]], flatten it into [1,2,3,4,5,6,7,8]."""
# nested = [[1,2,3], [4,5], [6,7,8]]
# print([i for sub_list in nested for i in sub_list])


"""From "programming", count how many times each character occurs (use dict comprehension)."""
# a = "programming"
# print({i: a.count(i)for i in set(a)})


"""Build a list of primes between 1–50 using a comprehension with all()."""
# print([i for i in range(1, 51)
#       if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1))
#       ])


"""From { "a": 1, "b": 5, "c": 10, "d": 15 }, create a dict with only values greater than 5."""
# d = { "a": 1, "b": 5, "c": 10, "d": 15}
# print({key: value for key, value in d.items() if value > 5})


""""the quick brown fox jumps over the lazy dog" → dict where key = word, value = frequency."""
string = "the quick brown fox jumps over the lazy dog"

# print({i: string.count(i) for i in set(string.split())})


"""From a 3x3 matrix, extract the diagonal [1,5,9]"""
# a = [[1,2,3],[4,5,6],[7,8,9]]
# print([i for sub_list in a for i in sub_list if i % 4 == 1])
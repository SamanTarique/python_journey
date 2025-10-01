"""Medium"""

"""https://edabit.com/challenge/jpW2fAzfPtop8AYfW"""

# Test.assert_equals(to_dict(["a", "b", "c"]), [{"a": 97}, {"b": 98}, {"c": 99}])
# Test.assert_equals(to_dict(["!", ".", "?"]), [{"!": 33}, {".": 46}, {"?": 63}])
# Test.assert_equals(to_dict(["^"]), [{"^": 94}])
# Test.assert_equals(to_dict([" "]), [{" ": 32}])
# Test.assert_equals(to_dict([]), [])


def to_dict(my_list):
    temp = []

    for i in my_list:
        my_dict = {}
        my_dict[i] = ord(i)
        temp.append(my_dict)

    return temp


print(to_dict(["a", "b", "c"]))

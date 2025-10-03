"""Hard"""

"""https://edabit.com/challenge/pQavNkBbdmvSMmx5x"""

from collections import Counter


def majority_vote(my_list):
    my_dict = dict.fromkeys(my_list, 0)

    for i in my_list:
        my_dict[i] += 1

    for key, values in my_dict.items():
        if values > len(my_list) // 2:
            return key
    return None


print(majority_vote(["A", "A", "B"]))
print(majority_vote(["A", "A", "A", "B", "C", "A"]))
print(majority_vote(["A", "B", "B", "A", "C", "C"]))

"""Pipeline of Generators

One generator yields numbers from 1 to 100.

Another generator takes those numbers and filters out multiples of 3.

A third generator squares the remaining numbers.
Chain them together."""

# gen1 = (i for i in range(1, 101))
# gen2 = (i for i in gen1 if i % 3 != 0)
# gen3 = (i * i for i in gen2)

# print(list(gen3))

"""Chunk Generator
Write a generator chunker(seq, size) that yields chunks of a list of length size.
Example: list(chunker([1,2,3,4,5,6,7], 3)) → [[1,2,3], [4,5,6], [7]]."""


def chunker(my_list, size):
    for i in range(0, len(my_list), size):
        yield my_list[i : i + size]


my_list = [1, 2, 3, 4, 5, 6, 7]
chunks = chunker(my_list, 3)
print(list(chunks))

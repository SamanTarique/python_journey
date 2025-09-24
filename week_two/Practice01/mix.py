"""Prime numbers
Use list comprehension to get all prime numbers from 1 to 100."""
# print([j for i in range(1, 101) for j in
#        range(2, int(i**0.5) + 1) if j % 2 != 0]
#       )
print([i for i in range(2, 101)
       if all(i % j != 0 for j in range(2, int(i**0.5) + 1))
       ])

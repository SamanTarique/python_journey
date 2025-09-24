import random

# [0.0,1.0)
print(random.random())

# [a,b]
print(random.randint(1, 10))

print(random.randrange(1, 10, 4))

print(random.choice([1, 2, 3, 4, 5, 6]))
print(random.choices([1, 2, 3, 4, 5, 6, 7, 8]))

a = [1, 2, 3]
print(random.shuffle(a))
print(a)

random.seed(10)
print(random.random())
print(random.random())


random.seed(10)
print(random.random())

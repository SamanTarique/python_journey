a = [1, 2, 3, "jgfdjs", "hsgfdh", 7.98, 7.09, (1, 2), (4, 6)]


x = filter((lambda x: isinstance(x, tuple)), a)

for i in x:
    print(i)

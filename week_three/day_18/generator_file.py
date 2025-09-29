def gen_read_line():
    with open("text_file.txt", "r") as f:
        for line in f:
            yield line


gen_exp = gen_read_line()

for i in range(10):
    print(next(gen_exp))

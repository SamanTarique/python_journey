import time


def tail():
    with open("text_file.txt", "r") as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if not line:
                # No new line yet, wait a bit
                time.sleep(0.1)
                continue
            yield line.strip()


for line in tail():
    print(f"New log: {line}")

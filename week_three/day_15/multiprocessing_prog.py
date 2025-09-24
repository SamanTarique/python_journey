import time
from multiprocessing import Process, current_process


def cpu_task(n):
    total = 0
    for i in range(n):
        total += i*i
    print(f"{current_process().name} done")


p1 = Process(target=cpu_task, args=(10000000,))
p2 = Process(target=cpu_task, args=(10000000,))

start = time.time()
p1.start()
p2.start()

p1.join()
p2.join()

print(f"Total time: {time.time() - start:.2f} seconds")

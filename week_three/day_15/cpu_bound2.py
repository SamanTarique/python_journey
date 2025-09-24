import threading
import time


def func_one():
    time.sleep(5)
    print("Inside function 1")


def func_two():
    time.sleep(3)
    print("Inside function 2")


def func_three():
    time.sleep(8)
    print("Inside function 3")


print("starting this task..........")

t1 = threading.Thread(target=func_one)
t2 = threading.Thread(target=func_two)
t3 = threading.Thread(target=func_three)

start = time.time()

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print(f"time elapsed - {time.time() - start}")
print("task ends here...................")

print(threading.enumerate())
print(threading.active_count())
print(time.perf_counter())

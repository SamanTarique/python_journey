import threading
import time


def square_sum(thread_name, num):
    count = 0
    for i in range(num):
        count += i*i
    print(f"{thread_name} is done")


n = 10000000

t1 = threading.Thread(target=square_sum, args=("Thread 1", 10000000))
t2 = threading.Thread(target=square_sum, args=("Thread 2", 10000000))

start_time = time.time()

t1.start()
t2.start()
t1.join()
t2.join()

print(f"CPU bound task finished in {time.time()-start_time:.4f}")

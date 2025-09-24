import queue
import threading
import time

q = queue.Queue()


def producer():
    for i in range(5):
        print(f"Producing {i}")
        q.put(i)
        time.sleep(0.5)


def consumer():
    for _ in range(5):
        item = q.get()
        print(f"Consumed {item}")
        q.task_done()


t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()
t1.join()
t2.join()

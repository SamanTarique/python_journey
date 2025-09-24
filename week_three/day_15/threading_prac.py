import threading

counter = 0
lock = threading.Lock()


def increment():

    for i in range(10000000):
        global counter

        with lock:
            counter += 1


t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print("counter-", counter)

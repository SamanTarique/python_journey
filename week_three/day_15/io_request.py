import threading
import time

import requests

api = 'https://api.namefake.com/'
start_thread = time.time()
start_non_thread = time.time()


def hit_api_threads(req_count):

    for i in range(req_count):
        response = requests.get(api)
        response.raise_for_status()
        name = response.json()['name']
        with open('thread_response.txt', 'a') as file:
            file.write(name + '\n')


def hit_api(req_count):

    for i in range(req_count):
        response = requests.get(api)
        response.raise_for_status()
        name = response.json()['name']
        with open('response.txt', 'a') as file:
            file.write(name + '\n')


"""**************************** THREADS ****************************"""


threads = []

print("Threads execution starts now..")

for i in range(5):
    t1 = threading.Thread(target=hit_api_threads, args=(10,))
    start_thread = time.time()
    t1.start()
    threads.append(t1)

for i in threads:
    i.join()

print("Threads execution ends now....")
print(f"Time elapsed by threading - {time.time()-start_thread:.3f}")

"""**************************** THREADS ****************************"""

"""**************************** WITHOUT THREADS ****************************"""

print("Normal Execution starts now...")
start_non_thread = time.time()
for i in range(5):
    hit_api(10)

print("Without thread execution ends now....")
print(f"Time elapsed Without thread - {time.time()-start_non_thread:.3f}")

"""**************************** WITHOUT THREADS ****************************"""

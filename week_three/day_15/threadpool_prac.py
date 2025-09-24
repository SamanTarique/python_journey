import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

api = 'https://api.namefake.com/'
names_count = 50
names = []


def fetch_names():
    response = requests.get(api)
    response.raise_for_status()
    response = response.json()['name']
    return response


with ThreadPoolExecutor(max_workers=5) as executor:
    start = time.time()
    results = [executor.submit(fetch_names) for _ in range(names_count)]

    for i in as_completed(results):
        names.append(i.result())

with open('threadpool_response.txt', 'w') as file:
    for name in names:
        file.write(name + '\n')

print(f"{time.time()-start:.3f}")

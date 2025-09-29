import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor

import requests

api = 'https://picsum.photos/200/300'


def get_images():

    cwd = os.getcwd()
    image_folder_path = os.path.join(cwd, 'images')

    for i in range(20):
        response = requests.get(api)
        response.raise_for_status()

        image_path = os.path.join(
            image_folder_path, f"{threading.current_thread().name}"
            f"_{time.time()}_{i+1}.jpg")

        with open(image_path, 'wb') as file:
            file.write(response.content)


cwd = os.getcwd()
os.makedirs(os.path.join(cwd, 'images'), exist_ok=True)

start = time.time()
print("Starting now...")
with ThreadPoolExecutor(max_workers=4) as executor:
    results = [executor.submit(get_images) for _ in range(4)]

    for i in results:
        i.result()

print(f"Ending in {time.time()-start:.3f}")

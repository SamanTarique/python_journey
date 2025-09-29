import os
import threading
import time

import requests

api = 'https://picsum.photos/200/400'


def get_images():

    cwd = os.getcwd()
    image_folder_path = os.path.join(cwd, 'images')

    for i in range(20):
        response = requests.get(api)
        response.raise_for_status()

        image_path = os.path.join(image_folder_path,
                                  f"{threading.current_thread().name}"
                                  f"_{time.time()}_{i+1}.jpg")

        with open(image_path, 'wb') as file:
            file.write(response.content)


cwd = os.getcwd()
os.makedirs(os.path.join(cwd, 'images'), exist_ok=True)

t1 = threading.Thread(target=get_images)
t2 = threading.Thread(target=get_images)
t3 = threading.Thread(target=get_images)
t4 = threading.Thread(target=get_images)

start = time.time()
print("Starting now...")
t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

print(f"Ending in {time.time()-start:.3f}")

import multiprocessing
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

num = 100000000


def cube_sum():
    sum = 0
    for i in range(100000000):
        sum += i**3
    return sum


# with multiprocessing.Pool(2) as pool:
#     start = time.time()
#     print("starting now.....")
#     # print(pool.map(cube_sum, [None, None]))
#     pool.apply(cube_sum)
#     pool.apply(cube_sum)
#     print(f"Took {time.time()-start:.3f}")

"""**********************************************************"""


with ThreadPoolExecutor(max_workers=2) as executor:
    start = time.time()
    results = [executor.submit(cube_sum) for _ in range(2)]

    for i in as_completed(results):
        print(i.result())

    print(f"{time.time()-start:.3f}")

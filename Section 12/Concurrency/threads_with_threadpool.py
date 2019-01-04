import time
from concurrent.futures import ThreadPoolExecutor


from utils.tools import ask_user, complex_calculation


start = time.time()
ask_user()
complex_calculation()
print(f'Single thread total time: {time.time() - start} seconds')

start = time.time()

with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(ask_user)

print(f'Two thread total time: {time.time() - start} seconds')
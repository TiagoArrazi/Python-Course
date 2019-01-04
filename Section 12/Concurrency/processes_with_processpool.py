import time
from concurrent.futures import ProcessPoolExecutor

from utils.tools import ask_user, complex_calculation, another_complex_calculation

start = time.time()
complex_calculation()
another_complex_calculation()
print(f'Single thread total time: {time.time() - start} seconds')

start = time.time()

with ProcessPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(another_complex_calculation)

print(f'Two processes total time: {time.time() - start}')
import time
from multiprocessing import Process

from utils.tools import ask_user, complex_calculation, another_complex_calculation

start = time.time()
complex_calculation()
another_complex_calculation()
print(f'Single thread total time: {time.time() - start} seconds')

process_complex_calculation = Process(target=complex_calculation)
process_ask_user = Process(target=another_complex_calculation())

process_complex_calculation.start()
process_ask_user.start()

start = time.time()

process_complex_calculation.join()
process_ask_user.join()

print(f'Two processes total time: {time.time() - start}')
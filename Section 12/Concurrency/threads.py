import time
from threading import Thread

from utils.tools import ask_user, complex_calculation

start = time.time()
ask_user()
complex_calculation()
print(f'Single thread total time: {time.time() - start} seconds')

thread1 = Thread(target=complex_calculation)
thread2 = Thread(target=ask_user)

start = time.time()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f'Two thread total time: {time.time() - start} seconds')
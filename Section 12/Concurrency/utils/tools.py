import time


def ask_user():
    start = time.time()
    user_input = input('Enter your name: ')
    greet = f'Hello, {user_input.capitalize()}'
    print(greet)
    print(f'ask_user(), {time.time() - start} seconds')


def complex_calculation():
    start = time.time()
    print('Started calculating...')
    var = [x ** 2 for x in range(20000000)]
    print(f'complex_calculation(list_length -> {len(var)}), {time.time() - start} seconds')


def another_complex_calculation():
    start = time.time()
    print('Started calculating another function...')
    var = [x ** 3 for x in range(10000000)]
    print(f'another_complex_calculation(list_length -> {len(var)}), {time.time() - start} seconds')
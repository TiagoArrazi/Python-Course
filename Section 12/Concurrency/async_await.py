from collections import deque
from types import coroutine

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


async def greet(g):
    print('Starting...')
    await g
    print('Terminating...')


greeter = greet(friend_upper())
greeter.send(None)

greeting = input('Input a greeting: ')
greeter.send(greeting)

greeting = input('Input a greeting: ')
greeter.send(greeting)
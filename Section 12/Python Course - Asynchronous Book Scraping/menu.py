import logging
from app import books
from os import system
from time import sleep


logger = logging.getLogger('scraping.menu')

def print_best_books():
    logger.info('Looking for the best books by rating...')
    best_books = list(filter(lambda x: x.rating == 5, books))
    sorted_best_books = sorted(best_books, key=lambda x: x.title)

    print('---5 STAR BOOKS---')
    for book in sorted_best_books:
        print(f'{book.title} - {book.rating} out of 5')


def print_cheapest_book():
    logger.info('Looking for the cheapest books...')
    cheapest = sorted(books, key=lambda x: x.price)[:10]
    print('---CHEAPEST BOOKS---')
    for book in cheapest:
        print(f'{book.title} - £{book.price:.2f}')


def book_generator():
    i = 0
    while i < len(books):
        yield books[i]
        i += 1


def get_next_book():
    logger.info('Looking for next book on the list...')
    print(next(g))


g = book_generator()

CHOICES = {
    'b': print_best_books,
    'c': print_cheapest_book,
    'n': get_next_book
}

while True:
    print('------------------')
    print('\n')
    print('b - Look at 5-star books\n')
    print('c - Look at the cheapest books\n')
    print('n - Get the next available book on the catalogue\n')
    print('q - Quit\n')
    opt = input('Welcome, please select an option \n')

    if opt.lower() in ('b', 'c', 'n'):
        system('clear')
        CHOICES[opt]()

    elif opt.lower() == 'q':
        logger.debug('Terminating program...')
        print('Quitting')
        sleep(1)
        system('clear')
        break

    else:
        system('clear')
        print('Invalid option')
        continue




from utils import book_database
from os import system
from time import sleep


while True:
    print('------------------')
    print('\n')
    print('a - Add a book\n')
    print('l - List your books\n')
    print('r - Mark a book as read\n')
    print('d - Delete a book\n')
    print('q - Quit\n')
    opt = input('Welcome, please select an option \n')

    if opt.lower() == 'a':
        system('clear')
        book_name = input('What is the name of the book? ')
        book_author = input('Who wrote it? ')
        book_database.book_db.add_book(book_name, book_author)

    elif opt.lower() == 'l':
        system('clear')
        for book in book_database.book_db.list_all():
            print(f'Book name: {book[0]}')
            print(f'Book author: {book[1]}')
            print(f'Have you read it? {book[2]}\n')

    elif opt.lower() == 'r':
        system('clear')
        book_name = input('Which book have you just read? ')
        book_database.book_db.mark_as_read(book_name)

    elif opt.lower() == 'd':
        system('clear')
        book_name = input('What is the name of the book? ')
        book_database.book_db.delete_book(book_name)
        print(f'{book_name} removed')

    elif opt.lower() == 'q':
        print('Quitting')
        sleep(1)
        system('clear')
        break

    else:
        system('clear')
        print('Invalid option')
        continue
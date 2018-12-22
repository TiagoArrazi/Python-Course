from pip._vendor.distlib.compat import raw_input
from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.BookData


# Works
def add_book():
    try:
        book_name = raw_input('Enter the name of the book: ')
        book_author = raw_input('Enter the name of the author: ')
        read = False

        db.BookData.insert_one({
            'book_name': book_name,
            'book_author': book_author,
            'read': read
        })

    except Exception as e:
        print(str(e))


# Works
def list_all():
    try:
        book_col = db.BookData.find()
        for book in book_col:
            print(f"Book: {book['book_name']}")
            print(f"Author: {book['book_author']}")
            if book['read'] is True:
                print('Already read it')
            else:
                print('Haven\'t read it yet\n')

    except Exception as e:
        print(str(e))


# Not working
def mark_as_read():
    try:
        criteria = raw_input('Enter the name of the you have just read: ')

        db.BookData.update_one(
            {"name": criteria},
            {
                '$set': {
                    'read': True
                }
            }
        )
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    list_all()

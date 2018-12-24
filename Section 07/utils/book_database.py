import sqlite3


class BookDB:

    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)

    def is_table(self, table_name):
        query = f"SELECT name from sqlite_master WHERE type='table' AND name='{table_name}';"
        cursor = self.conn.execute(query)
        result = cursor.fetchone()
        if result is None:
            return False
        else:
            return True

    def add_book(self, book_name, book_author):
        query = f"INSERT INTO book_shelf (book_name, book_author, read) values ('{book_name}', '{book_author}', 'no')"
        self.conn.execute(query)
        self.conn.execute('COMMIT')

    def list_all(self):
        query = f"SELECT * FROM book_shelf"
        cursor = self.conn.execute(query)
        result = cursor.fetchall()
        return result

    def mark_as_read(self, book_name):
        query = f"UPDATE book_shelf SET read='yes' WHERE book_name='{book_name}'"
        self.conn.execute(query)
        self.conn.execute('COMMIT')

    def delete_book(self, book_name):
        query = f"DELETE FROM book_shelf WHERE book_name='{book_name}'"
        self.conn.execute(query)
        self.conn.execute('COMMIT')


book_db = BookDB('book_db')

if not book_db.is_table('book_shelf'):
    book_db.conn.execute('CREATE TABLE book_shelf(book_name Varchar, book_author Varchar, read Varchar)')
else:
    pass


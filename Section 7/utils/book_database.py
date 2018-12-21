import sqlite3


class BookDatabase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)

    def is_table(self, table_name):
        query = f"SELECT name FROM sqlite_master WHERE type='table' and name='{table_name}';"
        cursor = self.conn.execute(query)
        result = cursor.fetchone()
        if result is None:
            return False
        else:
            return True

    def add_book(self, name, author):
        query = f"INSERT INTO book_shelf (name, author, read) values ('{name}','{author}',0)"
        cursor = self.conn.execute(query)
        return cursor

    def list_book(self):
        cursor = self.conn.execute("SELECT * FROM book_shelf")
        return cursor

    def mark_as_read(self, name):
        query = f"UPDATE book_shelf SET read=0 WHERE name='{name}'"
        cursor = self.conn.execute(query)
        return cursor

    def delete_book(self, name):
        query = f"DELETE FROM book_shelf WHERE name='{name}'"
        cursor = self.conn.execute(query)
        return cursor


if __name__ == '__main__':
    db = BookDatabase('book_db')
    if not db.is_table('book_shelf'):
        db.conn.execute('''CREATE TABLE book_shelf
                           (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                           name TEXT, 
                           author TEXT, 
                           read INTEGER)''')
    else:
        pass

    db.add_book('book_name_2', 'book_author_2')
    print(db.list_book())

import sqlite3


class BookDatabase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)

    def is_table(self, table_name):
        query = "SELECT FROM book_db WHERE type='table' and name={'" + table_name + "'};"
        cursor = self.conn.execute(query)
        result = cursor.fetchone()
        if result is None:
            return False
        else:
            return True

    def add_book(self, name, author):
        query = f"INSERT INTO book_db (name, author, read) values ('{name}','{author}',False)"
        cursor = self.conn.execute(query)
        return cursor

    def list_book(self):
        cursor = self.conn.execute("FROM book_db SELECT *")
        return cursor

    def mark_as_read(self, name):
        query = f"UPDATE book_shelf SET read=TRUE WHERE name='{name}'"
        cursor = self.conn.execute(query)
        return cursor

    def delete_book(self, name):
        query = f"DELETE FROM book_shelf WHERE name='{name}'"
        cursor = self.conn.execute(query)
        return cursor

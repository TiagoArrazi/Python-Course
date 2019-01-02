import requests

from pages.books_page import BooksPage

page_content = requests.get('http://books.toscrape.com').content
page = BooksPage(page_content)

for book in page.books:
    print(f'Title: {book.title}')
    print(f'Price(£): {book.price:.2f}')
    print(f'Rating: {book.rating}\n')

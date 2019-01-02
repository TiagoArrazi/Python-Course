import requests
from os import system
from time import sleep

from pages.books_page import BooksPage

system('clear')
books = []
print('Scraping for books...')
for i in range(50):
    page_content = requests.get(f'http://books.toscrape.com/catalogue/page-{i}.html').content
    page = BooksPage(page_content)
    books.extend(page.books)

print('Done!')
sleep(2)
system('clear')


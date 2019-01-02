import requests
from os import system
from time import sleep
import logging

from pages.books_page import BooksPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m%-%Y %H:%M:%S',
                    level=logging.INFO,
                    filename='logs.txt')

logger = logging.getLogger('scraping')

system('clear')
logger.info('Loading books list...')
print('Loading books list...')

page_content = requests.get('http://books.toscrape.com/catalogue/page-1.html').content
page = BooksPage(page_content)

books = page.books

for page_number in range(1, page.page_count):
    page_content = requests.get(f'http://books.toscrape.com/catalogue/page-{page_number + 1}.html').content
    page = BooksPage(page_content)
    books.extend(page.books)

logger.info('Done loading books list!')
print('Done loading books list!')
sleep(2)
system('clear')


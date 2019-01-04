import requests
from os import system
from time import sleep
import logging
import time
import asyncio

from pages.books_page import BooksPage
from async_tools.async_request import get_multiple_pages

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

loop = asyncio.get_event_loop()

books = page.books

urls = [f'http://books.toscrape.com/catalogue/page-{page_number + 1}.html'
        for page_number in range(page.page_count)]
start = time.time()
pages = loop.run_until_complete(get_multiple_pages(loop, *urls))
print(f'Total page requests took {time.time() - start}')

for page_content in pages:
    logger.debug('Creating BooksPage from page content')
    page = BooksPage(page_content)
    books.extend(page.books)

logger.info('Done loading books list!')
print('Done loading books list!')
sleep(2)
system('clear')


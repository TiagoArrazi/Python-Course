import re
import logging
from bs4 import BeautifulSoup


from locators.books_page_locators import BookPageLocators
from parsers.book_parser import BookParser

logger = logging.getLogger('scraping.books_page')


class BooksPage:
    def __init__(self, page):
        logger.debug('Parsing page content with BeautifulSoup HTML parser...')
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        logger.debug(f'Finding all books in the page using \'{BookPageLocators.BOOK}\'...')
        locator = BookPageLocators.BOOK
        book_tags = self.soup.select(locator)
        return [BookParser(e) for e in book_tags]

    @property
    def page_count(self):
        logger.debug('Finding all number of catalogue pages available...')
        content = self.soup.select_one(BookPageLocators.PAGER).string
        logger.info(f'Found number of catalogue pages available: {content}')
        pattern = re.compile(r'Page [\d]+ of ([\d]+)')
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        logger.debug(f'Extracted number of pages as integer: \'{pages}\'')
        return pages

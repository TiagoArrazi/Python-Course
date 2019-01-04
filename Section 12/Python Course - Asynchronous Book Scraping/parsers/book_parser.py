import re
import logging


from locators.book_locators import BookLocators


logger = logging.getLogger('scraping.book_parser')


class BookParser:

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        self.parent = parent

    def __str__(self):
        return f'Title: {self.title}, Price(£): {self.price}, Rating: {self.rating} out of 5'

    @property
    def title(self):
        logger.debug('Looking for book title...')
        locator = BookLocators.TITLE
        book_title = self.parent.select_one(locator).attrs['title']
        logger.debug(f'Found book title, \'{book_title}\'')
        return book_title

    @property
    def price(self):
        logger.debug('Looking for book price...')
        locator = BookLocators.PRICE
        pattern = re.compile(r'£(\d+\.\d+)')
        book_price = self.parent.select_one(locator).string
        float_book_price = float(pattern.match(book_price).group(1))
        logger.debug(f'Found book price, \'£{float_book_price:.2f}\'')
        return float_book_price

    @property
    def rating(self):
        logger.debug('Looking for book rating...')
        locator = BookLocators.RATING
        book_tag = self.parent.select_one(locator)
        book_rating = self.RATINGS[list(filter(lambda x: x != 'star-rating', book_tag.attrs['class']))[0]]
        logger.debug(f'Found book rating, \'{book_rating}\' out of 5')
        return book_rating

from locators.book_locators import BookLocators
import re


class BookParser:

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Book: {self.title}, Price(£): {self.price}, Rating: {self.rating}>'

    @property
    def title(self):
        locator = BookLocators.TITLE
        return self.parent.select_one(locator).attrs['title']

    @property
    def price(self):
        locator = BookLocators.PRICE
        regex = re.compile(r'£(\d+\.\d+)')
        book_price = self.parent.select_one(locator).string
        float_book_price = float(regex.match(book_price).group(1))
        return float_book_price

    @property
    def rating(self):
        locator = BookLocators.RATING
        book_tag = self.parent.select_one(locator)
        book_rating = list(filter(lambda x: x != 'star-rating', book_tag.attrs['class']))[0]
        return f'{book_rating} out of Five'

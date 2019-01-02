from locators.book_locators import BookLocators
import re


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
        locator = BookLocators.TITLE
        return self.parent.select_one(locator).attrs['title']

    @property
    def price(self):
        locator = BookLocators.PRICE
        pattern = re.compile(r'£(\d+\.\d+)')
        book_price = self.parent.select_one(locator).string
        float_book_price = float(pattern.match(book_price).group(1))
        return float_book_price

    @property
    def rating(self):
        locator = BookLocators.RATING
        book_tag = self.parent.select_one(locator)
        book_rating = list(filter(lambda x: x != 'star-rating', book_tag.attrs['class']))[0]
        return self.RATINGS[book_rating]

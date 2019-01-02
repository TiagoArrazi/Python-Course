import re
from bs4 import BeautifulSoup


from locators.books_page_locators import BookPageLocators
from parsers.book import BookParser


class BooksPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        locator = BookPageLocators.BOOK
        book_tags = self.soup.select(locator)
        return [BookParser(e) for e in book_tags]

    @property
    def page_count(self):
        content = self.soup.select_one(BookPageLocators.PAGER.string)
        pattern = re.compile(r'Page [\d]+ of ([\d]+)')
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        return pages

import re
import middle_html 

from class_html_locators import ParsedItemLocators
from bs4 import BeautifulSoup


class ParsedItem:

    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def name(self):  # CSS Selector
        locator = ParsedItemLocators.NAME_LOCATOR
        item_link = self.soup.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name

    @property
    def link(self):
        locator = ParsedItemLocators.LINK_LOCATOR
        item_link = self.soup.select_one(locator).attrs['href']
        return item_link

    @property
    def price(self):
        locator = ParsedItemLocators.PRICE_LOCATOR
        regex = re.compile(r'£(\d+\.\d+)')
        item_price = self.soup.select_one(locator).string
        float_item_price = float(regex.match(item_price).group(1))
        return float_item_price

    @property
    def rating(self):
        locator = ParsedItemLocators.RATING_LOCATOR
        item_link = self.soup.select_one(locator)
        item_rating = list(filter(lambda x: x != 'star-rating', item_link.attrs['class']))[0]

        rating_dict = {
            'One': '1 Star',
            'Two': '2 Stars',
            'Three': '3 Stars',
            'Four': '4 Stars',
            'Five': '5 Stars'
        }

        return rating_dict[item_rating]


item_1 = ParsedItem(middle_html.ITEM_HTML_1)
item_2 = ParsedItem(middle_html.ITEM_HTML_2)

print(f'Item_1 name: "{item_1.name}"')
print(f'Item_1 relative link: "{item_1.link}"')
print(f'Item_1 price(£): {item_1.price}')
print(f'Item_1 rating: {item_1.rating}')

print('\r')

print(f'Item_2 name: "{item_2.name}"')
print(f'Item_2 relative link: "{item_2.link}"')
print(f'Item_2 price(£): {item_2.price}')
print(f'Item_2 rating: {item_2.rating}')

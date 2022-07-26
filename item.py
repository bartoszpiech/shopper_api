from bs4 import BeautifulSoup
import requests
from requests.structures import CaseInsensitiveDict
from header import *

# TODO add photo atribute
class Item:
    def __init__(self, link):
        source = requests.get(link, headers = header).text
        soup = BeautifulSoup(source, 'lxml')
        self.link = link
        self.sizes = []
        self.sizes_available = []
        self.name = soup.find('h1', class_='product-detail-info__header-name').text.capitalize()
        self.description = soup.find('div', class_='product-detail-description').p.text
        sizes_ul = soup.find('ul', class_='product-detail-size-selector__size-list')
        self.price = float(soup.find('span', class_='price-current__amount').text.replace(',','.').replace(' PLN',''))
        self.old_price = self.price
        if soup.find('span', class_='price-old__amount'):
            self.old_price = float(soup.find('span', class_='price-old__amount').text.replace(',','.').replace(' PLN',''))
        for li in sizes_ul:
            stock = li['data-qa-action']
            size = li.span.text
            self.sizes.append(size)
            if li['data-qa-action'] == 'size-in-stock':
                self.sizes_available.append(size)

    def __repr__(self):
        return (
                f'name: {self.name}\n'
                f'link: {self.link}\n'
                f'description: {self.description}\n'
                f'sizes: {self.sizes}\n'
                f'available sizes: {self.sizes_available}\n'
                f'old price: {self.old_price}\n'
                f'price: {self.price}'
                )
    def __iter__(self):
        yield 'name', self.name
        yield 'link', self.link
        yield 'description', self.description
        yield 'sizes', self.sizes
        yield 'available sizes', self.sizes_available
        yield 'old price', self.old_price
        yield'price', self.price

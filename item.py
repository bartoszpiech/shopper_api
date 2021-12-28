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
        self.name = soup.find('h1', class_='product-detail-info__name').text.capitalize()
        self.description = soup.find('div', class_='product-detail-description').p.text
        sizes_ul = soup.find('ul', class_='product-detail-size-selector__size-list')
        prices = soup.find('div', class_='product-detail-info__price').text.replace(',','.').split('PLN')
        self.old_price = float(prices[0])
        self.price = self.old_price
        if len(prices) > 2:
            self.price = float(prices[1])
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

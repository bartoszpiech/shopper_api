#!/usr/bin/python

from bs4 import BeautifulSoup
import requests
from requests.structures import CaseInsensitiveDict
from item import *

link = 'https://www.zara.com/pl/pl/d%C5%82uga-kurtka-koszulowa-w-krat%C4%99-ze-wstawkami-z-%C5%82%C4%85czonych-tkanin-p09004187.html?v1=130401652&v2=2033356'

source = requests.get(link, headers = header).text
soup = BeautifulSoup(source, 'lxml')

sizes = []
sizes_available = []
ul = soup.find('ul', class_='product-detail-size-selector__size-list')
for li in ul:
    stock = li['data-qa-action']
    size = li.span.text
    sizes.append(size)
    if li['data-qa-action'] == 'size-in-stock':
        sizes_available.append(size)


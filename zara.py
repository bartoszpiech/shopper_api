#!/usr/bin/python

from bs4 import BeautifulSoup
import requests
from requests.structures import CaseInsensitiveDict

link = 'https://www.zara.com/pl/pl/d%C5%82uga-kurtka-koszulowa-w-krat%C4%99-ze-wstawkami-z-%C5%82%C4%85czonych-tkanin-p09004187.html?v1=130401652&v2=2033356'

headers = CaseInsensitiveDict()
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'

source = requests.get(link, headers = headers).text

soup = BeautifulSoup(source, 'lxml')

sizes = soup.find('ul', class_='product-detail-size-selector__size-list')

size_list = []
for li in sizes:
    stock = li['data-qa-action']
    size = li.span.text
    size_list.append((size, stock))

print(size_list)

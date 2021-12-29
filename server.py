from flask import Flask
from item import *

app = Flask(__name__)

@app.route('/item/<path:link>')
def scrapper(link):
    item = Item(link)
    return dict(item)

# Zara shopper app

## Old version
Python web-app that tracks items on the zara website. It was built originally using Python, Discord bot and perhaps Selenium web module. It used crontab to run the script every "x" minutes. The bot was hosted on Raspberry PI and was sending notifications to my discord server.

## New version
It will use BeautifulSoup module to scrap the Zara website, then I'll build the web API to handle all the operations. On top of that I'll build the website for users to add items that they like, delete bought items, etc.

## TODO
- [x] Build web scraper using BeautifulSoup,
- [x] Make Item class that collects all the data from Zara website,
- [x] Create flask server,
- [ ] Add color scraper for items that have multiple color options,
- [ ] Convert price scraping to use class attributes instead of primitive string slicing,
- [ ] Create cron/etc/Flask-crontab,
- [ ] Create Notification server that sends info to email / discord bot / element bot,
- [ ] Make automatic script that uses user data and sends available items to cart, fills user fields and waits for CC info to be added,
- [ ] Create UI using probably some Javascript web framework,
- [ ] Extend the app to be able to track multiple other websites (Reserved, Nike, etc.),
- [ ] Maybe react native app or something that will send notifications directly into user phones.

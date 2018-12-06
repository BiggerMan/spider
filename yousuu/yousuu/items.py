# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YousuuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()       # name of the book list
    author = scrapy.Field()     # author
    count = scrapy.Field()      # count of the books in the list
    votes = scrapy.Field()      # how many people like it
    follows = scrapy.Field()    # how many people follows it

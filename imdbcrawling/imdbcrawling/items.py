# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbcrawlingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    actor_name = scrapy.Field()
    actor_photo = scrapy.Field()
    actor_traits = scrapy.Field()
    pass
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewHouse(scrapy.Item):
    # define the fields for your item here like:
    province = scrapy.Field()
    city = scrapy.Field()
    name = scrapy.Field()
    rooms = scrapy.Field()
    area = scrapy.Field()
    address = scrapy.Field()
    district = scrapy.Field()
    sale = scrapy.Field()
    price = scrapy.Field()
    origin_url = scrapy.Field()


class EsfHouse(scrapy.Item):
    # define the fields for your item here like:
    province = scrapy.Field()
    city = scrapy.Field()
    name = scrapy.Field()
    rooms = scrapy.Field()
    area = scrapy.Field()
    floor = scrapy.Field()
    year = scrapy.Field()
    toward = scrapy.Field()
    address = scrapy.Field()
    district = scrapy.Field()
    price = scrapy.Field()
    unit = scrapy.Field()
    origin_url = scrapy.Field()
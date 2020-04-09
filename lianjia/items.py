# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 标题
    price = scrapy.Field()  # 价格
    unitPrice = scrapy.Field()  #平方价格
    community = scrapy.Field()  #小区
    region = scrapy.Field()  # 地区
    houseType = scrapy.Field()  #户型
    floor = scrapy.Field()  # 楼层
    area = scrapy.Field()  # 面积
    towards = scrapy.Field()  # 朝向
    decoration = scrapy.Field()  #装修情况
    focus = scrapy.Field()  # 关注人数
    link = scrapy.Field() #详情链接

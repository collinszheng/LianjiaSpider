# -*- coding: utf-8 -*-
import scrapy
from lianjia.items import LianjiaItem
import re
import time

class ScrapyspiderSpider(scrapy.Spider):
    name = 'scrapyspider'
    #allowed_domains = ['sh.lianjia.com/ershoufang']
    start_urls = []
    base_urls = 'http://sh.lianjia.com/ershoufang/'
    city_list = [
        'pudong','minhang','baoshan','xuhui',
        'putuo','yangpu','changning','songjiang',
        'jiading','huangpu','jingan','hongkou',
        'qingpu','fengxian','jinshan'
    ]
    for city in city_list:
        url = base_urls + city + '/pg1'
        start_urls.append(url)


    def parse(self, response):
        for index in range(1, 101):
            str_index = str(index)
            url = re.sub(r'(\d+?)',str_index,response.url,1)
            yield scrapy.Request(url, callback=self.get_link)

    def get_link(self, response):
        item = LianjiaItem()
        house_list = response.xpath('//div[@class="info clear"]/div[@class="title"]/a')
        for house in house_list:
            item['link'] = house.xpath('./@href').extract_first()
            yield scrapy.Request(item['link'],callback=self.parse_item,meta={'key':item})

    def parse_item(self, response):
        item = response.meta['key']
        time.sleep(2)
        try:
            item['title'] = response.xpath('//h1/text()').extract_first()
            item['price'] = response.xpath('//span[@class="total"]/text()').extract_first()
            item['unitPrice'] = response.xpath('//span[@class="unitPriceValue"]/text()').extract_first()
            item['community'] = response.css('.communityName a::text').extract_first()
            item['region'] = response.xpath('//div[@class="areaName"]/span[@class="info"]//text()').extract_first()
            item['houseType'] = response.xpath('//div[@class="content"]//ul/li[1]/text()').extract_first()
            item['floor'] = response.xpath('//div[@class="content"]//ul/li[2]/text()').extract_first()
            item['area'] = response.xpath('//div[@class="content"]//ul/li[3]/text()').extract_first()
            item['towards'] = response.xpath('//div[@class="content"]//ul/li[7]/text()').extract_first()
            item['decoration'] = response.xpath('//div[@class="content"]//ul/li[9]/text()').extract_first()
            item['focus'] = response.xpath('//span[@id="favCount"]/text()').extract_first()
        except:
            pass
        yield item
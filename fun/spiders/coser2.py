# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.loader import ItemLoader, Identity
from fun.items import CoserItem


class CoserSpider(scrapy.Spider):
    name = "coser2"
    allowed_domains = ["bcy.net"]
    start_urls = (
        'http://bcy.net/coser/detail/9495/130440',
    )

    def parse(self, response):
        l = ItemLoader(item=CoserItem(), response=response)
        l.add_xpath('name', "//h1[@class='js-post-title']/text()")
        l.add_xpath('info', "//div[@class='post__info']/div[@class='post__type post__info-group']/span/text()")
        urls = l.get_xpath('//img[@class="detail_std detail_clickable"]/@src')
        urls = [url.replace('/w650', '') for url in urls]
        l.add_value('image_urls', urls)
        l.add_value('url', response.url)
        return l.load_item()

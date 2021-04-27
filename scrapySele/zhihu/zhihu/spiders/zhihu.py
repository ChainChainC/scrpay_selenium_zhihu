import scrapy
from ..items import ZhihuItem
from selenium import webdriver
import time


class zhihuSpider(scrapy.Spider):
    name = 'zhihu'

    def start_requests(self):
        url = 'https://www.zhihu.com/'
        yield scrapy.Request(
            url=url,
            callback=self.parse_first
        )
        # yield scrapy.Request(
        #     url='https://www.baidu.com/',
        #     callback=self.parse_baidu
        # )

    def parse_first(self, response):
        title = response.xpath('//ul[@class="Tabs AppHeader-Tabs"]/li/a/text()').extract()
        item = ZhihuItem()
        item['title'] = title
        print('!!!!!', title)
        yield item

    def parse_baidu(self, response):
        title = response.xpath('//span[@class="btn_wr s_btn_wr bg"]/input').extract()
        print('!!!!!', title, '!!!!!!!!!')
import scrapy


class BaiduspiderSpider(scrapy.Spider):
    name = 'baiduSpider'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com/s?wd=hello']

    def parse(self, response):
        print(response.text)

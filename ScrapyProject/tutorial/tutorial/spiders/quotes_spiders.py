import scrapy

class QutoesSpider(scrapy.Spider):
    name = "qutoes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        # print(response.text)
        for quote in response.css('div.quote'):
            yield{
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            # 第一种方式创建Request对象
            # next_page = response.urljoin(next_page)
            # yield scrapy.Request(url=next_page, callback=self.parse)
            # 第二种方式创建Request对象
            yield response.follow(next_page, callback=self.parses)

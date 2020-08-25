import scrapy


class AlphaspiderSpider(scrapy.Spider):
    name = 'alphaSpider'
    allowed_domains = ['alphacoders.com']
    kw = input("请输入图片关键字：")
    start_urls = ['https://wall.alphacoders.com/search.php?search={}'.format(kw)]

    def parse(self, response):
        # print(response.text)
        imgs = response.xpath('//div[@class="boxgrid"]/a/img/@data-src').getall()
        for img in imgs:
            print(img)
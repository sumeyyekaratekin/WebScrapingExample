import scrapy

class BestsellerSpider(scrapy.Spider):
    name = 'bestseller'
    allowed_domains = ['www.idefix.com']
    start_urls = ['https://www.idefix.com/CokSatanlar/Kitap']

    def parse(self, response):
        products = response.xpath("//div[@class='product-info']")
        for product in products:
            yield{
                 "Kitap Adı" : product.xpath(".//div[@class='box-title']//a[@title]/text()").get(),
                 "Yazar " : product.xpath(".//a[@class='who']/text()").get(),
                 "Yayınevi " : product.xpath(".//a[@class='who2 alternate']/text()").get(),
                 "Fiyat" : product.xpath(".//span[@class='price price']/text()").get()
       }
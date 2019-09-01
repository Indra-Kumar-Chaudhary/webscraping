import scrapy 
from ..items import AmazonItem

class AmazonSpider(scrapy.Spider):
    name ='amazon'
    start_urls=[
        'https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&fst=as%3Aoff&qid=1567221965&rnid=1250225011&ref=lp_283155_nr_p_n_publication_date_0',
    ]

    def parse(self,response):
        items = AmazonItem()

        product_name = response.css('span.a-text-normal::text').extract()
        product_price = response.css('span.a-price-whole::text').extract()

        items['product_name'] = product_name
        items['product_price'] = product_price

        yield items 
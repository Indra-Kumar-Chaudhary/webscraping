import scrapy 

class QuotesSpider(scrapy.Spider):
    name='quotes'
    start_urls=[
        'https://quotes.toscrape.com/'
    ]
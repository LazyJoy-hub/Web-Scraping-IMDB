import scrapy
from ..items import ImdbcrawlingItem

class Crawl(scrapy.Spider):
    name = 'imdb'
    start_urls=[
        'https://www.imdb.com/list/ls050745379/'
    ]
    def parse(self, response):
        items = ImdbcrawlingItem()
        actor_name = response.css('.lister-item-header a::text').extract()
        actor_photo = response.css('#main img::attr(src)').extract()
        actor_traits = response.css('.text-small+ p::text').extract()


        items['actor_name'] =actor_name
        items['actor_photo']=actor_photo
        items['actor_traits']=actor_traits

        yield items
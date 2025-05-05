# Run with
#
# scrapy runspider craigslist-scraper-exercise.py  -o -:csv > out.csv 2> TRACE

# A very bare minimum spider

from scrapy.spiders import Spider
from scrapy import Request

class MySpider(Spider):
    name = 'CL scraper'
    allowed_domains = ['craigslist.org']
    start_urls = [ "https://pittsburgh.craigslist.org/search/apa" ]

    custom_settings = {
       'DOWNLOADER_CLIENT_TLS_METHOD' : 'TLSv1.2',
    }

    def parse(self, response):
        rows = response.xpath("//div[@class='result-info']")
        items = []
        for row in rows:
            item = {}
            item['title'] = row.xpath("./h3/a/text()").extract()
            item['price'] = row.xpath("./span/span[@class='result-price']/text()").extract()
            item['size'] = row.xpath("./span/span[@class='housing']/text()").extract()
            item['nbrhood'] = row.xpath("./span/span[@class='result-hood']/text()").extract()
            items.append(item)
        return items

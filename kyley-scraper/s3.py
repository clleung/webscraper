# Run with
#
# scrapy runspider s3.py  -o -:csv > out.csv 2> TRACE

# A very bare minimum spider

from scrapy.spiders import Spider
from scrapy import Request

class S1(Spider):
    name = 'CL scraper'
    # allowed_domains = ['craigslist.org']
    start_urls = [ "https://www.andrew.cmu.edu/user/sraja/multi/main.html" ]

    # custom_settings = {
    #    'DOWNLOADER_CLIENT_TLS_METHOD' : 'TLSv1.2',
    # }

    def parse(self, response):
        rows = response.xpath("//ul/li")
        items = []
        for row in rows:
            item = {}
            item['name'] = row.xpath("./a/text()").extract()
            item['url'] = row.xpath("./a/@href").extract()
            items.append(item)
        return items

    def parse(self, response):
        row = response
        item = {}
        item['first'] = row.xpath("//ul/li[@class='first']/text()").extract()
        item['last'] = row.xpath("//ul/li[@class='last']/text()").extract()
        return item

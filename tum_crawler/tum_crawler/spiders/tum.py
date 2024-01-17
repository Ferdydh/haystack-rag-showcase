from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import extruct
import os


path = "/Users/ferdydh/Code/haystack-rag-showcase/tum_data"

class TUMCrawler(CrawlSpider):
    name = 'tum'
    allowed_domains = ['www.cit.tum.de']
    start_urls = ['https://www.cit.tum.de/']
    rules = (
        Rule(LinkExtractor(), callback='parse_html', follow=True),
    )

    def parse_html(self, response):
        data = {
            'url': response.url,
            'text': response.text,
        }
        
        print("called")

        # Save HTML content to a file
        filename = f"{path}/{response.url.replace('/', '_').replace(':', '_')}.html"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(response.text)

        return data
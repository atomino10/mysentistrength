
import scrapy
from scrapy.http import Request
from scrapy.item import Item, Field
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings
file_name = "links.csv"
#file_name_output = "my_file_without_dupes.csv"
URL = "https://ytbmp3.club/?url=https%3A%2F%2Fwww.youtube.com%2Fplaylist%3Flist%3DPLzhUH3AElIOwXH-HMz09HT65W6syRLpD_%26app%3Ddesktop"


class skroutzItem(Item):
    link = Field()


class MySpider(scrapy.Spider):
  name = "skroutz"
  allowed_domains = ["www.skroutz.gr"]



  def start_requests(self):
      for i in range(1):
        yield Request(URL, callback=self.parse)
      self.settings=get_project_settings()
      
        
  def parse(self, response):
      urlss = response.css('#results')
      nikos=urlss.css('.d-sm-block')

      
      for urls in nikos:        
        items['link']  = urls.xpath('@a').extract()
        yield items


#scrapy runspider amazon_reviews_scraping/amazon_reviews_scraping/spiders/amazon_reviews.py -o reviews.csv
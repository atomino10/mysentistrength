
import scrapy
from scrapy.http import Request
from scrapy.item import Item, Field
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings
#file_name = "reviews.csv"
#file_name_output = "my_file_without_dupes.csv"
URL = "https://iraklis-press24.gr/2021/01/28/megali-anatropi-kai-prokrisi-stoys-16-t/?%d"


class skroutzItem(Item):
    link = Field()


class MySpider(scrapy.Spider):
  name = "skroutz"
  allowed_domains = ["https://iraklis-press24.gr"]



  def start_requests(self):
      for i in range(36800):
        yield Request(URL%i, callback=self.parse)
      self.settings=get_project_settings()
      
        
  def parse(self, response):
      print('\n')


#scrapy runspider amazon_reviews_scraping/amazon_reviews_scraping/spiders/apicount.py
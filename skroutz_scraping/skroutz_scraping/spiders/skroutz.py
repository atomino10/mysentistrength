
import scrapy
import pandas as pd
from scrapy.http import Request
from scrapy.item import Item, Field
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings
file_name = "reviews.csv"
#file_name_output = "my_file_without_dupes.csv"
URL = "https://www.skroutz.gr/c/12/television.html?order_by=pricevat&order_dir=asc&page=%d"


class skroutzItem(Item):
    link = Field()


class MySpider(scrapy.Spider):
  name = "skroutz"
  allowed_domains = ["www.skroutz.gr"]



  def start_requests(self):
      for i in range(1):
        yield Request(URL % i, callback=self.parse)
      self.settings=get_project_settings()
      
        
  def parse(self, response):
      urlss = response.css('#sku-list')
      nikos=urlss.css('.js-sku-link')
      if not urlss:
        raise CloseSpider('No more pages')
      items=skroutzItem()
      items['link']=[]
      data=[]
      for urls in nikos:        
        items['link']  = urls.xpath('@href').extract()
        data.append(items['link'])
      pd.DataFrame(data).to_csv('links.csv',header=['link'],index=False)
        #yield items


#scrapy runspider amazon_reviews_scraping/amazon_reviews_scraping/spiders/amazon_reviews.py -o links.csv
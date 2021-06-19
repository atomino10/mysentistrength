# -*- coding: utf-8 -*-
 
# Importing Scrapy Library

import pandas as pd
import scrapy
from scrapy.utils.project import get_project_settings

# Creating a new class to implement Spide
class AmazonReviewsSpider(scrapy.Spider):
 
    file_name = "links.csv"

    # Spider name
    name = 'amazon_reviews'
 
    # Domain names to scrape
    allowed_domains = ['skroutz.gr']
    
    # Base URL for the MacBook air reviews
    #myBaseUrl = "https://www.skroutz.gr/s/20060269/Apple-iPhone-11-64GB-Black.html?from=sku_color_variations#reviews"
    myBaseUrl="https://www.skroutz.gr/"
    start_urls=[]
 
    df = pd.read_csv(file_name, sep="\t or ,")
    df.drop_duplicates(subset=None, inplace=True)
    df=df['link'].tolist()
    print(df)
    # Creating list of urls to be scraped by appending page number a the end of base url
    for i in range(1,len(df)):
        start_urls.append(myBaseUrl+df[i])

        
    # Defining a Scrapy parser
    def parse(self, response):
            topic = response.css('#nav')

            #collecting topic
            top=topic.css('h2')

            title=response.css('#sku-details')
            titlee=title.css('h1')

            data = response.css('#sku_reviews_list')
            


            # Collecting product star ratings
            star_rating = data.css('.actual-rating')
 
            # Collecting user reviews
            comments = data.css('.review-body')

            #vote = data.css('.review-rate')
            count = 0

            # Combining the results
            for review in star_rating:
                yield{'stars': ''.join(review.xpath('.//text()').extract()),
                      'comment': ''.join(comments[count].xpath(".//text()").extract()),
                      #'vote': ''.join(vote[count].xpath("//div[@class='review-rate']/text()").extract()),
                      'topic': ''.join(top.xpath(".//text()").extract()),
                      'title': ''.join(titlee.xpath(".//text()").extract())
                     }                                   
                count=count+1
            

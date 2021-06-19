# mysentistrength
Python implementation of sentistrength algorithm


mysenti.py is the code, reviews.csv are the reviews (2800), stars.csv are the stars of every review, in folder finallexformysenti there are the lexicons and in folder dataset there are a .csv with results from crawlers (dirtyreviews), a .csv with those results cleared (reviewstars) and a .csv with results(finalgreekmysenti).


Inside folder skroutz_scraping and subfolder spiders there are the two crawlers, amazon_reviews.py and amazon_reviews22.py.

Run with command 
</br>
scrapy runspider amazon_reviews_scraping/amazon_reviews_scraping/spiders/amazon_reviews.py -o links.csv</br>
and</br>
scrapy runspider amazon_reviews_scraping/amazon_reviews_scraping/spiders/amazon_reviews22.py -o dirtyreviews.csv</br>
FROM THE FOLDER amazon_reviews_scraping

There is function clearfiles() inside mysenti.py that makes reviewstars.csv that is suitable for mysentistrength and function splitfiles() that makes reviews.csv and stars.csv. Note that if there is not a dirtyreviews.csv inside the folder, clearfiles() does not run.

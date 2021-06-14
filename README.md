# mysentistrength
Python implementation of sentistrength algorithm


mysenti.py is the code, reviews.csv are the reviews (2800), stars.csv are the stars of every review and in folder there are the lexicons and a .csv with results
(also in xls because of some encoding issues)


Inside folder skroutz_scraping and subfolder spiders there are the two crawlers, skroutz.py and skroutzmaincrawl.py.

Run with command 
scrapy runspider skroutz.py
and
scrapy runspider skroutzmaincrawl.py -o dirtyreviews.csv

After this files goes to main folder and mysenti.py gets is as input automatically. There is a function clearfiles() inside mysenti.py that makes the .csv suitable for mysentistrength. Note that if there is not a dirtyreviews.csv inside the folder, clearfiles() does not run.

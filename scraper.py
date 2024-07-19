import logging
import os
os.environ["SCRAPERWIKI_DATABASE_NAME"] = "sqlite:///data.sqlite"
import scraperwiki
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s:%(message)s')

feed_url="https://www.orange.nsw.gov.au/category/das-on-exhibition/feed/"

def parse_feed():
    feed = scraperwiki.scrape(feed_url)
    page=BeautifulSoup(feed, "xml")
    items=page.findAll('item')
    for item in items:
        title=item.title
        logging.info(f"Item titled {title}")

if __name__ == "__main__":
    parse_feed()

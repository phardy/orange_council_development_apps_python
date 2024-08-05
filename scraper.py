import logging
import os
import urllib
os.environ["SCRAPERWIKI_DATABASE_NAME"] = "sqlite:///data.sqlite"
import scraperwiki
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s:%(message)s')

def parse_feed():
    feed_url="https://www.orange.nsw.gov.au/category/das-on-exhibition/feed/"
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0"
    }
    #feed = scraperwiki.scrape(feed_url, '', user_agent)
    req = urllib.request.Request(url=feed_url,
                                 headers=headers)
    fh = urllib.request.urlopen(req)
    # page=BeautifulSoup(fh, "xml")
    page=BeautifulSoup(fh)
    items=page.findAll('item')
    for item in items:
        title=item.title
        logging.info(f"Item titled {title}")

if __name__ == "__main__":
    parse_feed()

import scrapy
import time
from scrapy import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

from app.log.log import lprint
from database_pipeline import get_mongoDB, get_mongo_collection_name

class GlobalForestBot (scrapy.Spider):
    name = "GlobalForestBot"
    start_urls = [
        'https://www.globalforestwatch.org/blog/climate/'
    ]

    def __init__(self):
        lprint("GlobalForest is connecting to database", 1)
        self.db = get_mongoDB()

        # Setting up Selenium
        chromeOptions = Options()
        chromeOptions.add_argument('--headless')
        chromeOptions.add_argument('--no-sandbox')
        chromeOptions.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(executable_path="app/Bots/bots/chromedriver",options=chromeOptions)

    def parse(self, response):

        # Getting page to crawl on selenium
        self.driver.get("https://www.globalforestwatch.org/blog/climate/")

        source_code = self.driver.page_source
        selector = Selector(text=source_code)

        # Getting all articles
        cards = selector.css("div.css-1a95uzy.e1oc1uuc0")

        for card in cards :
            item = {
                "_id": card.css("h3.notranslate.css-9eej5g.e1oc1uuc4::text").get(),
                "title" :card.css("h3.notranslate.css-9eej5g.e1oc1uuc4::text").get(),
                "author" : None,
                "category" : card.css("button.css-fl6z7r.eine78n2::text").get(),
                "link" : "https://www.globalforestwatch.org" + card.css("div.css-1a95uzy.e1oc1uuc0 a::attr(href)").get(),
                "cover_image": card.css("div.css-ddv62a.e15twzda0 img::attr(src)").get(),
                "website":"globalforest",
                "treated":False
            }

            article_to_parse = card.css("h3.notranslate.css-9eej5g.e1oc1uuc4::text").get()

            if article_to_parse is not None:
                yield response.follow(article_to_parse, callback=self.parse_article,  meta={'data': item})

    def parse_article (self,response):

        item = response.meta.get("data")

        lprint ("ADDING ARTICLE TO DATABASE :"+str(item),1)
        self.db.add_one_data(get_mongo_collection_name(), item)
        
        yield item
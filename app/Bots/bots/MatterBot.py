import scrapy
import time
from scrapy import Selector
from selenium import webdriver
import selenium
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from app.log.log import lprint
from database_pipeline import get_mongoDB, get_mongo_collection_name


class MatterBot (scrapy.Spider):
    name = "MatterBot"
    start_urls = [
        'https://youmatter.world/en/planet/articles/'
    ]

    def __init__(self):
        lprint("MatterBot IS CONNECTING TO DATABSE", 1)
        self.db = get_mongoDB()

    def parse(self, response):

        # Setting up Selenium
        chromeOptions = Options()
        chromeOptions.add_argument('--headless')
        chromeOptions.add_argument('--no-sandbox')
        chromeOptions.add_argument('--disable-dev-shm-usage')
        
        driver = webdriver.Chrome(
            executable_path="app/Bots/bots/chromedriver", options=chromeOptions)

        # Getting page to crawl on selenium
        driver.get("https://youmatter.world/en/planet/articles/'")

        # CLicking to accept cookies
        driver.find_element_by_css_selector('#wt-cli-accept-all-btn').click()

        # Generate all articles
        while True:
            try:
                time.sleep(2)
                driver.find_element_by_css_selector(
                    "button.col--center-main.btn.btn--border.btn--highlight-color.js-more").click()
            except:
                break

        # Getting all the articles links on the page
        source_code = driver.page_source
        selector = Selector(text=source_code)
        links = selector.css("a.card.card--classique")

        for link in links:
            item = {
                "_id": link.css("a div.card__content h3::text").get(),
                "title": link.css("a div.card__content h3::text").get(),
                "author": link.css("a div.card__content h4::text").get(),
                "category": link.css("a div.card__content footer h4::text").get(),
                "link": link.css("a::attr(href)").get(),
                "cover_image": link.css("a div.card__figure img::attr(src)").get(),
                "website": "youmatter",
                "treated" : False
            }

            article_to_parse = link.css("a::attr(href)").get()

            if article_to_parse is not None:
                yield response.follow(article_to_parse, callback=self.parse_article, meta={'data': item})

    def parse_article(self, response):
        """
        Getting all the text.
        """
        item = response.meta.get("data")

        article = BeautifulSoup(response.css(
            "div.article__content").get(), 'lxml')

        item["text"] = article.get_text()

        lprint("ADDING ARTICLE TO DATABASE : "+str(item), 1)
        get_mongoDB().add_one_data(get_mongo_collection_name(), item)

        yield item

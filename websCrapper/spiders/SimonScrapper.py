import requests
import scrapy as crap
from websCrapper.items import Tweet, User


# Email = SimonTheScrapper@gmail.com
# Password = MotherScrapper420
url = "https://twitter.com/login"
payload = { 'session[username_or_email]': 'SimonTheScrapper@gmail.com', 
            'session[password]': 'MotherScrapper420'}
r = requests.post(url, data=payload)


class simonsCrapper(crap.Spider):
    name = "simonscrapper"
    start_urls = [
            'https://twitter.com/search?f=tweets&vertical=news&q=%23Weather&src=tyah',
        ]


    
    def parse(self, html_page):

        page = crap.Selector(text=html_page)

        ### for text only tweets
        self = page.xpath('//li[@data-item-type="tweet"]/div')
        for item in self:
            yield item
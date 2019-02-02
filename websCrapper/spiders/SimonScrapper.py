import requests
import scrapy as crap
from websCrapper.items import Tweet, User


class simonsCrapper(crap.Spider):
    name = "simonscrapper"
    allowed_domains = ['twitter.com']
    start_urls = [
        'https://twitter.com/search?f=tweets&vertical=news&q=%23weather&src=typd&lang=en-gb'
        ]

    def parse(self, html_page):
        page = crap.Selector(text=html_page)

        for item in page.xpath('//li[@data-item-type="tweet"]/div'):
            yield {
                     'text' : item.xpath('.//div[@class="js-tweet-text-container"]/p//text()').get()
                }

    """ # Email = SimonTheScrapper@gmail.com
        # Password = MotherScrapper420
        def start_requests(self):
            return [crap.FormRequest("https://twitter.com/login",
                                        formdata={'user': 'SimonTheScrapper@gmail.com', 'pass': 'MotherScrapper420'},
                                        callback=self.logged_in)]

        def logged_in(self, response):
            # here you would extract links to follow and return Requests for
            # each of them, with another callback
            pass 

    
        def parse(self, html_page):

            page = crap.Selector(text=html_page)

            ### for text only tweets
            self = page.xpath('//li[@data-item-type="tweet"]/div')
            for item in self:
                yield item """
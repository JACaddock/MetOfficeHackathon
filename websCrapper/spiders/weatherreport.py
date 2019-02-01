import scrapy as crap


class weatherReport(crap.Spider):
    name = "weatherreport"
    start_urls = [
            'https://twitter.com/search?f=tweets&vertical=news&q=%23Weather&src=tyah',
        ]

    def parse(self, response):
        for quote in response.css('div'):
            yield {
                quote.css('span.text::text').get()         
            }

        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, callback=self.parse)
import scrapy


class testCrap(scrapy.Spider):
    name = "quotes"


    def start_requests(self):
        urls = [
            'http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/xml/3840?res=3hourly&key=c32ec598-3acd-408d-a867-0404bfb2e2b3'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)


        """next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

            #!next_page = response.urljoin(next_page)
            #!yield crap.Request(next_page, callback=self.parse)
        """





#* scrapy runspider testcrap.py -o quotes.json


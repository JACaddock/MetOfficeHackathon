from bs4 import BeautifulSoup
import request

# Email = SimonTheScrapper@gmail.com
# Password = MotherScrapper420
def start_requests(self):
    return [BeautifulSoup.FormRequest("https://twitter.com/login",
                                formdata={'user': 'SimonTheScrapper@gmail.com', 'pass': 'MotherScrapper420'},
                                callback=self.logged_in)]

def logged_in(self, response):
    # here you would extract links to follow and return Requests for
    # each of them, with another callback
    pass 


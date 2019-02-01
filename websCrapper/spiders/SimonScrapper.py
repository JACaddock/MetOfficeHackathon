import requests
import logging
from datetime import datetime
import scrapy as crap
from scrapy.spiders import CrawlSpider, Rule
from websCrapper.items import Tweet, User


logger = logging.getLogger(__name__)


# Email = SimonTheScrapper@gmail.com
# Password = MotherScrapper420
url = "https://twitter.com/login"
payload = { 'session[username_or_email]': 'SimonTheScrapper@gmail.com', 
            'session[password]': 'MotherScrapper420'}
r = requests.post(url, data=payload)


class simonsCrapper(CrawlSpider):
    name = "simonscrapper"
    start_urls = [
            'https://twitter.com/search?f=tweets&vertical=news&q=%23Weather&src=tyah',
        ]


    
    def parse(self, html_page):

        page = crap.Selector(text=html_page)

        ### for text only tweets
        items = page.xpath('//li[@data-item-type="tweet"]/div')
        for item in self.parse_tweet_item(items):
            yield item


    def parse_tweet_item(self, items):
        for item in items:
            tweet = Tweet()

            tweet['usernameTweet'] = item.xpath('.//span[@class="username u-dir u-textTruncate"]/b/text()').extract()[0]

            ID = item.xpath('.//@data-tweet-id').extract()
            if not ID:
                continue
            tweet['ID'] = ID[0]

            ### get text content
            tweet['text'] = ' '.join(
                item.xpath('.//div[@class="js-tweet-text-container"]/p//text()').extract()).replace(' # ',
                                                                                                    '#').replace(
                ' @ ', '@')
            if tweet['text'] == '':
                # If there is not text, we ignore the tweet
                continue

            ### get meta data
            tweet['url'] = item.xpath('.//@data-permalink-path').extract()[0]

            nbr_retweet = item.css('span.ProfileTweet-action--retweet > span.ProfileTweet-actionCount').xpath(
                '@data-tweet-stat-count').extract()
            if nbr_retweet:
                tweet['nbr_retweet'] = int(nbr_retweet[0])
            else:
                tweet['nbr_retweet'] = 0

            nbr_favorite = item.css('span.ProfileTweet-action--favorite > span.ProfileTweet-actionCount').xpath(
                '@data-tweet-stat-count').extract()
            if nbr_favorite:
                tweet['nbr_favorite'] = int(nbr_favorite[0])
            else:
                tweet['nbr_favorite'] = 0

            nbr_reply = item.css('span.ProfileTweet-action--reply > span.ProfileTweet-actionCount').xpath(
                '@data-tweet-stat-count').extract()
            if nbr_reply:
                tweet['nbr_reply'] = int(nbr_reply[0])
            else:
                tweet['nbr_reply'] = 0

            tweet['datetime'] = datetime.fromtimestamp(int(
                item.xpath('.//div[@class="stream-item-header"]/small[@class="time"]/a/span/@data-time').extract()[
                    0])).strftime('%Y-%m-%d %H:%M:%S')

            ### get photo
            has_cards = item.xpath('.//@data-card-type').extract()
            if has_cards and has_cards[0] == 'photo':
                tweet['has_image'] = True
                tweet['images'] = item.xpath('.//*/div/@data-image-url').extract()
            elif has_cards:
                logger.debug('Not handle "data-card-type":\n%s' % item.xpath('.').extract()[0])

            ### get animated_gif
            has_cards = item.xpath('.//@data-card2-type').extract()
            if has_cards:
                if has_cards[0] == 'animated_gif':
                    tweet['has_video'] = True
                    tweet['videos'] = item.xpath('.//*/source/@video-src').extract()
                elif has_cards[0] == 'player':
                    tweet['has_media'] = True
                    tweet['medias'] = item.xpath('.//*/div/@data-card-url').extract()
                elif has_cards[0] == 'summary_large_image':
                    tweet['has_media'] = True
                    tweet['medias'] = item.xpath('.//*/div/@data-card-url').extract()
                elif has_cards[0] == 'amplify':
                    tweet['has_media'] = True
                    tweet['medias'] = item.xpath('.//*/div/@data-card-url').extract()
                elif has_cards[0] == 'summary':
                    tweet['has_media'] = True
                    tweet['medias'] = item.xpath('.//*/div/@data-card-url').extract()
                elif has_cards[0] == '__entity_video':
                    pass  # TODO
                    # tweet['has_media'] = True
                    # tweet['medias'] = item.xpath('.//*/div/@data-src').extract()
                else:  # there are many other types of card2 !!!!
                    logger.debug('Not handle "data-card2-type":\n%s' % item.xpath('.').extract()[0])

            is_reply = item.xpath('.//div[@class="ReplyingToContextBelowAuthor"]').extract()
            tweet['is_reply'] = is_reply != []

            is_retweet = item.xpath('.//span[@class="js-retweet-text"]').extract()
            tweet['is_retweet'] = is_retweet != []

            tweet['user_id'] = item.xpath('.//@data-user-id').extract()[0]
            yield tweet
import incapsula

import pdb
import scrapy

from scrapy.crawler import CrawlerProcess

import lxml.html
from lxml.cssselect import CSSSelector


from scrapy_splash import SplashRequest


#
# session =  incapsula.IncapSession()
# response = session.get('https://www.whoscored.com/Regions/206/Tournaments/4/Spain-La-Liga')
# pdb.set_trace()


class MySpider(scrapy.Spider):
	name = 'players'
	start_urls = [
		'https://www.whoscored.com/Regions/206/Tournaments/4/Spain-La-Liga'
	]
	custom_settings = {
		'DOWNLOADER_MIDDLEWARES': {
		    'scrapy_splash.SplashCookiesMiddleware': 723,
    		'scrapy_splash.SplashMiddleware': 725,
    		'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
			'incapsula.IncapsulaMiddleware': 900
		},
		'SPLASH_URL':'http://localhost:8050',
		'SPIDER_MIDDLWARES':{
			'scrapy_splash.SplashDeduplicateArgsMiddleware': 100
		},
		'DUPEFILTER_CLASS' : 'scrapy_splash.SplashAwareDupeFilter',
		'HTTPCACHE_STORAGE' : 'scrapy_splash.SplashAwareFSCacheStorage'
	}

	def start_requests(self):
		for url in self.start_urls:
			yield SplashRequest(url, self.parse, args={'wait':0.5})


	def parse(self,response):
		results = open('results.json','w')
		for team in response.css('tbody.standings > tr > td > a.team-link'):
			name = team.css('::text').extract()[0]
			results.write(name)
			yield {
				'team': name
			}
		results.close()


process = CrawlerProcess({
	'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(MySpider)
process.start()

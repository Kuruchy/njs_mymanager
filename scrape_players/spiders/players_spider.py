import pdb
import scrapy

import base64

from scrapy.crawler import CrawlerProcess
from scrapy_splash import SplashRequest


class MySpider(scrapy.Spider):
	name = 'players'
	start_urls = [
		'https://www.whoscored.com/Regions/206/Tournaments/4/Spain-La-Liga'
	]

	def start_requests(self):
		splash_args = {
			'html': 1,
			'png': 1,
			'width': 600,
			'render_all': 1,
			'wait': 0.5
		}
		for url in self.start_urls:
			yield SplashRequest(url, self.parse, endpoint='render.json', args=splash_args)


	def parse(self,response):
		png_bytes = base64.b64decode(response.data['png'])
		image = open('screenshot.png','wb')
		image.write(png_bytes)
		image.close()
		results = open('results.json','w')
		for team in response.css('tbody.standings > tr > td > a.team-link'):
			name = team.css('::text').extract()[0]
			results.write(name)
			yield {
				'team': name
			}
		results.close()


# process = CrawlerProcess({
# 	'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
# })
#
# process.crawl(MySpider)
# process.start()

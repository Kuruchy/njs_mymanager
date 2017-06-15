import pdb
import scrapy

import base64

from scrapy.crawler import CrawlerProcess
from scrapy_splash import SplashRequest

import sys

reload(sys)

sys.setdefaultencoding('utf8')


class Marca(scrapy.Spider):
	name = 'marcaligafantastica'
	start_urls = [
		'http://www.laligafantasymarca.com/puntos?Season=2016&Round=38&Mode='
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
		for player in response.css(self.settings.get('MARCA')['player_selector']):
			# pdb.set_trace()
			name = player.css('.name > a::text').extract_first()
			points = player.css('.points::text').extract_first()
			yield {
				'name': name,
				'points': points
			}
		# results.close()

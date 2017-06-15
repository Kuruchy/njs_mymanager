import pdb
import scrapy

import base64

from scrapy.crawler import CrawlerProcess
from scrapy_splash import SplashRequest

import sys

reload(sys)

sys.setdefaultencoding('utf8')


class Transfermarkt(scrapy.Spider):
	name = 'transfermarkt'
	start_urls = [
		'https://www.transfermarkt.com/laliga/startseite/wettbewerb/ES1'
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

	def parse_team(self,response):
		for player in response.css(self.settings.get('TRANSFERMARKT')['player_selector']):
			name = player.css('::text').extract_first()
			yield {
				'player': name
			}

	def parse(self,response):
		splash_args = {
			'html': 1,
			'png': 1,
			'width': 600,
			'render_all': 1,
			'wait': 0.5
		}
		# png_bytes = base64.b64decode(response.data['png'])
		# image = open('screenshot.png','wb')
		# image.write(png_bytes)
		# image.close()
		# results = open('results.json','w')
		for team in response.css(self.settings.get('TRANSFERMARKT')['team_selector']):
			name = team.css('::text').extract_first()
			link = team.css('::attr(href)').extract_first()
			# results.write(name)
			# yield {
			# 	'team': name,
			# 	'link': link
			# }
			yield SplashRequest('https://www.transfermarkt.com'+link, self.parse_team, endpoint='render.json', args=splash_args)
		# results.close()

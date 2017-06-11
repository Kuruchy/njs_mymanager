import pdb
import scrapy

import base64

from scrapy.crawler import CrawlerProcess
from scrapy_splash import SplashRequest


class Whoscored(scrapy.Spider):
	name = 'whoscored'
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

	def parse_team(self,response):
		png_bytes = base64.b64decode(response.data['png'])
		image = open('screen_team.png','wb')
		image.write(png_bytes)
		image.close()
		results = open('results_player.json','w')
		for player in response.css(self.settings.get('WHOSCORED')['player_selector']):
			name = team.css('::text').extract_first()
			results.write(name)
			yield {
				'player': name
			}

		results.close()

	def parse(self,response):
		splash_args = {
			'html': 1,
			'png': 1,
			'width': 600,
			'render_all': 1,
			'wait': 0.5
		}
		png_bytes = base64.b64decode(response.data['png'])
		image = open('screenshot.png','wb')
		image.write(png_bytes)
		image.close()
		results = open('results.json','w')
		for team in response.css(self.settings.get('WHOSCORED')['team_selector']):
			name = team.css('::text').extract_first()
			link = team.css('::attr(href)').extract_first()
			results.write(name)
			# yield {
			# 	'team': name,
			# 	'link': link
			# }
			next_page = link
			if next_page is not None:
				next_page = response.urljoin(next_page)
				yield SplashRequest(next_page, self.parse_team, endpoint="render.json", args=splash_args)
		results.close()

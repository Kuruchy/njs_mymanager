import incapsula

import pdb
import scrapy
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
			'incapsula.IncapsulaMiddleware': 900
		}
	}
	def parse(self,response):
		for team in response.css('tbody.standings > tr > td > a.team-link'):
			yield {
				'team': team.css('innerText')
			}

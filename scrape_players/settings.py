# -*- coding: utf-8 -*-

# Scrapy settings for scrape_players project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

import incapsula

MARCA = {
	'name': 'marca',
	'base_url': 'http://www.laligafantasymarca.com/puntos?Season=2016&Round=38&Mode=',
	'player_selector': '.player'
}

COMUNIAZO = {
	'name': 'comuniazo',
	'player_selector': '#jugadores > tbody > tr'
}

WHOSCORED = {
	'name': 'WHOSCORED',
	'base_url': 'https://www.whoscored.com',
	'team_url': '/Regions/206/Tournaments/4/Spain-La-Liga',
	'team_selector': 'tbody.standings > tr > td > a.team-link',
	'player_selector': 'tbody#player-table-statistics-body > tr > td.pn > a.player-link'
}
TRANSFERMARKT = {
	'name' : 'TRANSFERMARKT',
	'base_url': '',
	'team_url': '',
	'team_selector': 'div#yw1 > table > tbody > tr > td.hauptlink.hide-for-small > a.vereinprofil_tooltip',
	'player_selector': 'span.hide-for-small > a.spielprofil_tooltip'
}



BOT_NAME = 'scrape_players'

SPIDER_MODULES = ['scrape_players.spiders']
NEWSPIDER_MODULE = 'scrape_players.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrape_players (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

COOKIES_ENABLED = False

DOWNLOAD_DELAY = 3


DOWNLOADER_MIDDLEWARES = {
	'scrapy_splash.SplashCookiesMiddleware': 723,
	'scrapy_splash.SplashMiddleware': 725,
	'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
	'incapsula.IncapsulaMiddleware': 900
}

SPLASH_URL = 'http://localhost:8050'

SPIDER_MIDDLWARES = {
	'scrapy_splash.SplashDeduplicateArgsMiddleware': 100
}

DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

USER_AGENT =  'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'



# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scrape_players.middlewares.ScrapePlayersSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'scrape_players.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'scrape_players.pipelines.ScrapePlayersPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

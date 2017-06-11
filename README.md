# njs_mymanager
Nodejs admin for My Manager App

How to run:
```
git clone

npm install

node index.js
```

Pages protected by incapsula (whoscored) can't be accessed with normal request package.

Tested and not worked:
- cloudscraper
- casperjs : too complicated


Also tried with python package:
- managed to access the webpage with incapsula session, but when using scrapy it didnt work (403 response)
- second time I tested a normal session.get, it didnt work

Whoscored seems to be well protected.

Follow these guidelines to jump protection
https://doc.scrapy.org/en/latest/topics/practices.html#avoiding-getting-banned

10-06-2017
With python I managed to get the HTML without getting blocked, but since it includes javascript that fills the HTML I need a webserver to execute the js. Using now splash.

https://github.com/scrapy-plugins/scrapy-splash

http://splash.readthedocs.io/en/latest/install.html

```
$ docker run -p 8050:8050 scrapinghub/splash

$ scrapy crawl <name_of_spider>
```

Now successfully getting the names of the teams

```
$ scrapy crawl whoscored
```

It seems like you can follow the links of each of the teams, but the result is only html, not executed javascript. I'm not sure if I'm doing the
```
yield SplashRequest(next_page, self.parse_team, endpoint="render.json", args=splash_args)
```
correctly 

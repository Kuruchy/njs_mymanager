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

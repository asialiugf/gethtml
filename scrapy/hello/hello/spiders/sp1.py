import sys
import chardet
import importlib
import scrapy
from scrapy_splash import SplashRequest
importlib.reload(sys)
#sys.setdefaultencoding('utf-8')

class MySpider(scrapy.Spider):
    name = "hh"
    start_urls = ['http://www.gzzbw.cn/trade/bulletin/?id=45398',]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        print("--------------------------------------------------")
        chardet.detect(response.body)
        decodeData = response.body.encode('UTF-8')
        #response.body.decode('gbk')
        #decodeData = response.body.decode("gbk")
        #print(decodeData)
        print(response.body)
        #gbkContent = response.body.decode(chardet.detect(response.body)['encoding'])
        #utf8Content = gbkContent.encode('utf-8')
        #print (utf8Content)
        print("--------------------------------------------------")
        # response.body is a result of render.html call; it
        # contains HTML processed by a browser.
        # ...

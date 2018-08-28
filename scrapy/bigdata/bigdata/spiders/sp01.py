import sys
import chardet
import importlib
import scrapy
from scrapy_splash import SplashRequest
importlib.reload(sys)
#sys.setdefaultencoding('utf-8')

class MySpider(scrapy.Spider):
    name = "sp01"
    start_urls = ['http://zw.hainan.gov.cn/2017/jydt.php?Class=315&Deep=2&year=0&month=0&key=&page=1']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        print("--------------------------------------------------")
        #chardet.detect(response.body)
        #decodeData = response.body.encode('UTF-8')
        #response.body.decode('gbk')
        #decodeData = response.body.decode("gbk")
        #print(decodeData)
        #print(response.body)
        #print(response.body.decode('UTF-8'))
        mm = response.xpath('//div[@class="BeltBar BeltBar2"]//dd')  # ok!!
        for kk in mm:
            print(kk.extract())
            t0 = kk.xpath('a/text()')[0].extract()
            print( t0 )
            print("----------------")
            yield {
                'text': kk.xpath('a/text()')[0].extract(),
                'author': kk.xpath('a/@href')[0].extract(),
                'tags': "333",
            }

        print(mm.extract())
        print(mm[0].extract())
        print(mm[1].extract())
        print(mm[2].extract())
        print(mm[10].extract())
        aaa = mm[0].xpath('a/text()')[0]
        print(aaa.extract())
        bbb = mm[0].xpath('a/@href')[0].extract()
        print (bbb)
        #gbkContent = response.body.decode(chardet.detect(response.body)['encoding'])
        #utf8Content = gbkContent.encode('utf-8')
        #print (utf8Content)
        print("--------------------------------------------------")
        # response.body is a result of render.html call; it
        # contains HTML processed by a browser.
        # ...
        '''
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': ''.join(quote.css('div.tags a.tag::text').extract()),
            }
        '''


    def my_parse(self,response):
        mm = response.xpath('//div[@class="BeltBar BeltBar2"]//dd')  # ok!!

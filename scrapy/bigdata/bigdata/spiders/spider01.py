import scrapy
import time

class uQthotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://www.gzzbw.cn/trade/bulletin/?id=45399',
            'http://www.gzzbw.cn/trade/bulletin/?id=45398',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            #time.sleep(5)

    def parse(self, response):
        print("kkkkkkkkkkkkkkkk000000000000000000000000000")
        #print(response.body)

        #mm = response.xpath('//div[@class="BeltBar BeltBar2"]//dd')  # ok!!
        #mm = response.xpath('//div[@class="container-fluid"]/div[@class="row"]/div[@class="col-xs-12"][1] \
        #                    /div/div[@class="row"][2]/div[@class="col-xs-9"]/div[@id="bulletin_title"]/p/span')
        mm = response.xpath('//div[@id="bulletin_title"]/p/span/text()')
        print(mm)
        print(mm.extract())

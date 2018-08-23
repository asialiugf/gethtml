import scrapy


class QuotesSpider(scrapy.Spider):
    name = "hainan"
    desc = "http://zw.hainan.gov.cn/2017/jydt.php?Class=315&Deep=2"
    start_urls = [
        #'http://zzcg.ccgp.gov.cn/zbgg/index.jhtml',
        'http://zw.hainan.gov.cn/2017/jydt.php?Class=315&Deep=2',
    ]

    def parse(self, response):
        print(response)
        mm = response.css('.contentSubject')
        #print(mm.extract())
        print("kkkkkkkkkkkkkkkk000000000000000000000000000")

        #print(response.xpath('//div[@class="contentSubject fw accelem"]'))
        #mm = response.xpath('//div[contains(@class,"BeltBar BeltBar2")]') # ok!!
        mm = response.xpath('//div[@class="BeltBar BeltBar2"]//dd')  # ok!!
        '''
        mm = response.xpath('//div[contains(@class,"BeltBar BeltBar2") \
                               and contains(@class,"") \
                               and contains(@class,"accelem")]')
        '''
        print(mm.extract())

        print(response.xpath('.//div[@class="contentSubject fw accelem"]/div[@class="BeltBar BeltBar2"]/dl[1]/dd[@class="accbg"][1]/a[@class="leaidx"]'))

        print("0000000000000000000000000000000kkkkkkkkkkkkkkkk000000000000000000000000000")
        '''
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        '''

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
        print(mm[0].extract())
        print(mm[1].extract())
        print(mm[2].extract())
        print(mm[3].extract())
        print(mm[4].extract())


        print("0000000000000000000000000000000kkkkkkkkkkkkkkkk000000000000000000000000000")

        
    def parse_detail(self, response):
        print(response.body)

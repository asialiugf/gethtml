import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://zzcg.ccgp.gov.cn/zbgg/index.jhtml',
    ]

    def parse(self, response):
        print(response)
        mm = response.css('.Title01')
        print("kkkkkkkkkkkkkkkk000000000000000000000000000")
        print(mm)
        print(mm.extract())
        aa = mm.css('.h2')
        aa = mm.xpath('//h2/text()')[0]
        print(aa.extract())
        print("0000000000000000000000000000000kkkkkkkkkkkkkkkk000000000000000000000000000")
        mm = response.css('W870 Right WhiteBg')
        #mm = response.xpath('//div[class='W870 Right WhiteBg']')
        mm = response.xpath('//div[contains(@class,"W870") \
                               and contains(@class,"Right") \
                               and contains(@class,"WhiteBg")]//h2/text()')[0]
        print(mm.extract())
        print("0000000000000000000000000000000kkkkkkkkkkkkkkkk000000000000000000000000000")
        '''
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        '''

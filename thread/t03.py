# -*- coding: utf-8 -*-
import scrapy

class StackOverFlowSpider(scrapy.Spider):
    name = "stackoverflow" #你在项目中跑蜘蛛的时候，要用到它的名字
    start_urls = ['https://stackoverflow.com/questions?sort=votes']
    
    #parse是解析函数
    def parse(self,response):
        for question in response.xpath('//div[@class="question-summary"]'):
            title = question.xpath('.//div[@class="summary"]/h3/a/text()').extract_first()
            links = response.urljoin(question.xpath('.//div[@class="summary"]/h3/a/@href').extract_first())
            content = question.xpath('.//div[@class="excerpt"]/text()').extract_first().strip()
            votes = question.xpath('.//span[@class="vote-count-post high-scored-post"]/strong/text()').extract_first()
            #votes = question.xpath('.//strong/text()').extract_first()
            answers = question.xpath('.//div[@class="status answered-accepted"]/strong/text()').extract_first()

            yield{
                'title':title,
                'links':links,
                'content':content,
                'votes': votes,
                'answers':answers
            }

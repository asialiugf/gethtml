import requests
import ssl
from lxml import etree


#ssl._create_default_https_context = ssl._create_unverified_context

session = requests.Session()
URL = 'http://zzcg.ccgp.gov.cn/zbgg/index.jhtml'
req = session.get(URL)
req.encoding = 'utf8'

r = req.content
print(r)



# 将request.content 转化为 Element
html = etree.HTML(req.content) 
items = html.xpath('//div[class="Title01"]')
#name = items.encode('gb2312', 'ignore').decode('gb2312')
#items = html.xpath('//ol/li/div[@class="item"]')
print(items) 
print(html) 

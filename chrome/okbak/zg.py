# 导入selenium的浏览器驱动接口
from selenium import webdriver

# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys

# 导入chrome选项
from selenium.webdriver.chrome.options import Options
# 创建chrome浏览器驱动，无头模式（超爽）
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("http://zzcg.ccgp.gov.cn/zbgg/index.jhtml")
mm = driver.find_element_by_css_selector("[class='List2 Top8']")
element = driver.find_element_by_xpath('//div[@class="List2 Top8"]/ul//li')
#driver.findElement(By.xpath("(//ul[@class='dropdown-menu inner selectpicker']/li)[last()]/a/span[@class='text']")).click()
#driver.findElement(By.xpath("(//div[@class='List2 Top8']/ul//li)[last()]")).click()
#xx = driver.find_elements_by_xpath("(//div[@class='List2 Top8']/ul//li)[last()]")  # ok!!
#driver.find_elements_by_xpath("(//div[@class='List2 Top8']/ul//li)[last()]/a[contains(text(),'Re-Submit')]").click()
#driver.find_element_by_xpath("(//div[@class='List2 Top8']/ul//li)[last()]/a[contains(text(),'Re-Submit')]").click()
#mm = driver.find_element_by_xpath("(//div[@class='List2 Top8']/ul//li)[last()]/a").click()
#mm = driver.find_element_by_xpath("(//div[@class='List2 Top8']/ul//li)[last()]")
mm = driver.find_elements_by_xpath("(//div[@class='List2 Top8']/ul//li)")
url = mm[5].find_element_by_xpath('.//a[@href]')
print( "333333333333333333")
#print(url)
print(url.text)
yy = url.get_attribute("href")
print(url.get_attribute("href"))
driver.get(yy)
ttime = driver.find_element_by_xpath("(//div[@class='TxtCenter Padding10'])")
print(ttime.text)

print(driver.title)

print( "888888888888888888")

print(driver.title)

print(len(mm))
#for lii in mm:
for i in range(len(mm)):
    link = mm[i-1].find_element_by_xpath('.//a[@href]')
    url = link.get_attribute("href")
    print(url)
    driver.get(url)
    tti = driver.find_element_by_xpath("(//div[@class='TxtCenter Padding10'])")
    print(tti.text)
    #link.click()

links = mm.find_elements_by_tag_name("a")
for link in links:
    #if not "_blank" in link.get_attribute("target") and ("google" in link.et_attribute("href") or not "http" in link.get_attribute("href")):  
    xx = link.click()
    print(xx)
    driver.back()

print(links)
#print(xx)

li=driver.find_elements_by_xpath('.//div[class="List2 Top8"]/ul//li')
print(li)

print ('*'*10)

#List<WebElement> webElements = driver.findElements(By.xpath("//div[@class='List2 Top8']/ul/li"));
# time.sleep(3)

# 获取页面名为wrapper的id标签的文本内容
#data = driver.find_element_by_id("wrapper").text
#print(data)
print(driver.title)
driver.save_screenshot("baidu.png")
driver.quit()

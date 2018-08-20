# 导入selenium的浏览器驱动接口
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)

# 加载百度页面
driver.get("http://zzcg.ccgp.gov.cn/zbgg/index.jhtml")
time.sleep(3)

#ul = driver.find_element_by_xpath('//*[@id="primary_menu"]/ul')
# ul = driver.find_element_by_xpath('//*[@id="primary_menu"]/ul')
ul = driver.find_elements_by_class_name("PaddingLR15")

xxs = driver.find_elements_by_css_selector("span.Right")
#xxs = driver.find_elements_by_css_selector("span.Right").click()
pp = xxs.find_elements(By.xpath("//a")).click()

print(pp.title)
#lis = ul.find_elements_by_xpath('li')
#print(len(lis))    # 有多少个li
#print(lis[-1].text)  # 最后一个li

print(driver.title)

driver.quit()

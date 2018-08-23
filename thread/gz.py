from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)

#driver.implicitly_wait(10)
driver.get("http://www.gzzbw.cn/trade/?category=affiche")
time.sleep(5)
mm = driver.find_element_by_css_selector("[class='div_title text_view']")
#xx = driver.find_element_by_css_selector("[class='div_title text_view']/a//span")
print(mm.text)
print(driver.page_source)
print(driver.title)
driver.quit()

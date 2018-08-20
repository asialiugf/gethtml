# 导入selenium的浏览器驱动接口
from selenium import webdriver
import time

# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys

# 导入chrome选项
from selenium.webdriver.chrome.options import Options
# 创建chrome浏览器驱动，无头模式（超爽）
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.implicitly_wait(10)
driver.get("http://www.gzzbw.cn/trade/?category=affiche")
time.sleep(5)
mm = driver.find_element_by_css_selector("[class='div_title text_view']")
#xx = driver.find_element_by_css_selector("[class='div_title text_view']/a//span")
print(mm.text)
print(driver.page_source)
print(driver.title)
driver.quit()


# coding=utf-8
from selenium import webdriver
 
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
 
driver.find_element_by_id("kw").send_keys("Selenium2")
driver.find_element_by_id("su").click()

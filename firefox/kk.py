#! /usr/bin/env python3
# coding=utf-8
'''
Created on 2016-8-16
@author: Jennifer
Project:使用Firefox浏览器
'''
from selenium import webdriver 

driver = webdriver.Firefox()
#driver.get('http://www.baidu.com')
driver.get('http://www.gzzbw.cn/trade/?category=affiche')
#driver.find_element_by_id('kw').send_keys('Selenium')
#driver.find_element_by_id('su').click()
print(driver.title)

driver.quit()

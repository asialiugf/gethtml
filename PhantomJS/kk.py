
"""基本流程"""
from selenium import webdriver
 
#要想调用键盘操作需要引入keys包
from selenium.webdriver.common.keys import Keys
 
#调用环境变量指定的PhantomJS浏览器创建浏览器对象
driver = webdriver.PhantomJS()
#如果没有在环境变量指定PhantomJS位置
#driver = webdriver.PhantomJS(executable_path="F:\phantomjs\phantomjs-2.1.1-windows\bin")
 
#get方法会一直等到页面被完全加载，然后才会继续程序
#通常测试会在这里选择time.sleep(2)
driver.get("http://www.baidu.com")
 
'''具体的操作，仿人为上网'''
 
#关闭当前网页，如果只有一个页面，会关闭浏览器
#driver.close()
 
#关闭浏览器
driver.quit()

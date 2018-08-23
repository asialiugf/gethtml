import urllib.request
from multiprocessing.dummy import Pool as ThreadPool 

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from functools import wraps
  
def fn_timer(function):
  @wraps(function)
  def function_timer(*args, **kwargs):
    t0 = time.time()
    result = function(*args, **kwargs)
    t1 = time.time()
    print ("Total time running %s: %s seconds" %
        (function.func_name, str(t1-t0))
        )
    return result
  return function_timer
 
urls = [
    'https://www.python.org/',
    'https://www.python.org/community/awards/',
    # etc.. 
    ]

'''
print('----------------')
driver.get('https://www.python.org/community/awards/')
print(driver.title)
driver.get('https://www.python.org/')
print(driver.title)
print('----------------')
'''

def gethtml(url):
    prefs = {"profile.managed_default_content_settings.images":2}
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    time.sleep(5)
    mm = driver.find_element_by_css_selector("[class='div_title text_view']")
    #xx = driver.find_element_by_css_selector("[class='div_title text_view']/a//span")
    print(mm.text)
    #print(driver.page_source)
    print(driver.title)
    driver.quit()

def gethtml1(url):
    prefs = {"profile.managed_default_content_settings.images":2}
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    print(driver.title)
    driver.quit()
    #driver.close()



myurls = [ 
    'http://www.gzzbw.cn/trade/?category=affiche',
] 


#gethtml("http://www.gzzbw.cn/trade/?category=affiche")

pool = ThreadPool(4) 
#results = pool.map(urllib.request.urlopen, urls)
#results = pool.map(gethtml, myurls)
#gethtml1('https://www.python.org/community/awards/')
results = pool.map(gethtml1, urls)
results = pool.map(gethtml, myurls)
pool.close() 
pool.join() 




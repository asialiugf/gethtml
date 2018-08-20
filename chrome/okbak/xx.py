#coding = utf-8
#sudo apt-get install python3-openpyxl
 
 
from openpyxl import workbook
from openpyxl import load_workbook
 
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
 
def getAllData(url):
    global book     # 全局工作表对象
    PCBH = []      # 普查編號
    SuoSH = []     # 索書號
    CunJuan = ['','','','','','','','','','']   # 存卷
    TMZZ = []      # 題名著者
    BanBen = []    # 版本
    CeShu = []     # 册（件）数    
    DanWei = []    # 单位
 
    page_number = 14910  # 页数初始为1
 
    while page_number <= 65914:
        # print("-----------打印第",page_number,"页")
        try:
            link = driver.find_element_by_link_text(str(page_number)) 
        except NoSuchElementException:
    	    print ("solve all page")
    
        link.click()
 
        # 获取源代码
        soup = BeautifulSoup(urlopen(driver.current_url),"html.parser")
        # print(driver.current_url)
        # 获取各参数值，并且添加到相应的列表中
 
        for link in soup.find_all(attrs={"data-field":"PUCHABIANHAO"}):
            # print(link.get_text)
            PCBH.append(link.get_text())
 
        for link in soup.find_all(attrs={"data-field":"SUOSHUHAO"}):
            # print(link.get_text)
            SuoSH.append(link.get_text())
 
        for link in soup.find_all(attrs={"data-field":"TIMING"}):
            # print(link.get_text)
            TMZZ.append(link.get_text())
 
        for link in soup.find_all(attrs={"data-field":"BANBEN"}):
            # print(link.get_text)
            BanBen.append(link.get_text())
 
        for link in soup.find_all(attrs={"data-field":"CESHU"}):
            # print(link.get_text)
            CeShu.append(link.get_text())
 
        for link in soup.find_all(attrs={"data-field":"DANWEI"}):
            # print(link.get_text)
            DanWei.append(link.get_text())
 
        # 对存卷这一参数做特殊筛选处理
        count = 0   # 记录循环次数,即统计item数量 
        for tag in soup.find_all(attrs={"class":"item"}):
            title = tag.find_all(attrs={"class":"ot"})
            i = 0  
            for n in title:
                text = n.get_text()
                text = text.replace('\n','')
                if i == 0: # 查找 第一个ot
                    # print('')
                    pass
                elif i == 1: # 查找 第二个ot,即查找存卷是否存在,存在则添加到列表中
                    # print(link.get_text)
                    CunJuan.insert(count,text)              
                i = i + 1
            count = count + 1       
 
        for i in range(10):
            book.append([PCBH[i],SuoSH[i],TMZZ[i],BanBen[i],CeShu[i],DanWei[i],CunJuan[i]])
 
        PCBH.clear()
        SuoSH.clear()
        TMZZ.clear()
        BanBen.clear()
        CeShu.clear()
        DanWei.clear()        
        CunJuan.clear()
        CunJuan = ['','','','','','','','','','']
 
        if page_number % 10 == 0:
            wb.save('getGJPC0614.xlsx')
            print(time.strftime('%m-%d %H:%M:%S', time.localtime(time.time())), "---已向Excle中存入",page_number,"页数据---")
        page_number = page_number + 1
         
 
if __name__ == '__main__':
 
    driver = webdriver.Chrome()
    url = 'XXX'
    driver.get(url)
    #  创建Excel表并写入数据  
    wb = workbook.Workbook()  # 创建Excel对象  
    book = wb.active  # 获取当前正在操作的表对象  
    # 往表中写入标题行,以列表形式写入！  
    book.append(['普查編號', '索書號', '題名著者', '版本', '册（件）数', '单位','存卷'])
 
    getAllData(url)
 
    driver.quit()

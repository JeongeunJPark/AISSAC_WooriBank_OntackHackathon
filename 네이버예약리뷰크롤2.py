url = 'https://booking.naver.com/review/bizes/215255?filterId=all&expandId=false'


from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
import pandas as pd
import random
browser = webdriver.Chrome('C:/Users/WJ/Desktop/youngman/chromedriver.exe')
browser.implicitly_wait(3)
n = 10
num = range(1,n,1)


browser.get(url)
sc = []
ti = []
tex = []
ob = []

for i in num:
    time.sleep(random.randint(1,2))
    try:
        element = browser.find_element_by_class_name('btn_cls')
        webdriver.ActionChains(browser). \
            move_to_element(element).click(element).perform()

        time.sleep(random.randint(1,3))
        print(i)
    except:
        pass
    sss = browser.find_elements_by_class_name('score')
    te = browser.find_elements_by_class_name("review")
    tim = browser.find_elements_by_class_name('date')
    obje = browser.find_elements_by_class_name('contents_tit')
    sss = sss[6:]
    for g in sss:
        sc.append(g.text)
    for gg in te:
        tex.append(gg.text)
    for ggg in tim:
        ti.append(ggg.text)
    for gggg in obje:
        ob.append(gggg.text)
    browser.find_element_by_class_name('btn_nxt').click()
    i +=1


sales= {'rev':tex,'score':sc,'date':ti,'buy':ob}
print(sales)
df = pd.DataFrame.from_dict(sales)
df.to_excel("C:\\Users\\WJ\\Desktop\\youngman\\롯데랜드_네이버예매리뷰.xlsx")
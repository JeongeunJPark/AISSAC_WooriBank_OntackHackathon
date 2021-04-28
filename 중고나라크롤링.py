url = 'https://cafe.naver.com/ArticleList.nhn?search.clubid=10050146&search.menuid=749&search.boardtype=L'

from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
import pandas as pd
import random
browser = webdriver.Chrome('C:/Users/WJ/Desktop/youngman/chromedriver.exe')
browser.implicitly_wait(5)
browser.get(url)
browser.switch_to.frame('cafe_main')
# ki = browser.find_elements_by_class_name('inner_list')

# print(ki.text)
# for k in ki:
#     print(k.find_element_by_tag_name('a').get_attribute())
ti =  browser.find_elements_by_tag_name("a")
for t in ti:
    print(t.text)
   # for ttt in tt:
   #     print(ttt.text)


for t in ti:
   print(type(t))
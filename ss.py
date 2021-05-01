
url = 'https://m.cafe.naver.com/ca-fe/web/cafes/10050146/menus/749'


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


prev_height = browser.execute_script("return document.body.scrollHeight")

# 웹페이지 맨 아래까지 무한 스크롤

num = range(500)


for i in num:
    while True:
        # 스크롤을 화면 가장 아래로 내린다
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        # 페이지 로딩 대기
        time.sleep(2)

        # 현재 문서 높이를 가져와서 저장
        curr_height = browser.execute_script("return document.body.scrollHeight")

        if (curr_height == prev_height):
            browser.find_element_by_class_name('u_cbox_btn_more').click()
            break
        else:
            prev_height = browser.execute_script("return document.body.scrollHeight")


ti = []
tex = []
da = []



#
# for j in num:
#     browser.find_element_by_class_name('u_cbox_btn_more').click()


sss = browser.find_elements_by_class_name('ellip')
te = browser.find_elements_by_class_name("tit")
tim = browser.find_elements_by_class_name('time')
# for g in sss:
#     tex.append(g.text)
#     print(g.text)
#     print('ellip')
a = 0
for gg in te:
    print(a)
    if a % 2 == 1:
        ti.append(gg.text)
    print(gg.text)
    print('tit')
    a += 1


for ggg in tim:
    da.append(ggg.text)
    print(ggg.text)


# sale= {'title':ti[0:(len(ti)-1)],'date':da}
sales = {'title':ti[0:(len(ti)-1)],'date':da}
print(sales)

print(len(ti))
print(len(da))

df = pd.DataFrame.from_dict(sales)

df.to_excel("C:\\Users\\WJ\\Desktop\\youngman\\중고나라_탭_크롤링_100.xlsx")
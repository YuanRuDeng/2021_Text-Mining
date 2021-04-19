import requests 
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
keyword = "新竹"

#避免廣告出現
options = Options()
options.add_argument("--disable-notifications")

#開啟瀏覽器
chrome = webdriver.Chrome()
chrome.get("https://www.dcard.tw/search/posts?query="+keyword)
time.sleep(5)

#選取 不含內文
# KeyWordJustInTitle = chrome.find_element_by_class_name('euTDLF')
# KeyWordJustInTitle.click()
time.sleep(1)

LatestButton = chrome.find_element_by_class_name('jquRcw')
LatestButton.click()
RelativityButton = chrome.find_element_by_class_name('ipyeMe')
RelativityButton.click()

#點選 第一篇文章
FirstArticleTitle = chrome.find_element_by_class_name('tgn9uw-3')
FirstArticleTitle.click()
time.sleep(1)

title=[]
df = pd.DataFrame()
for i in range(500):
    print(i)
    #讀取當下的網頁代碼，並擷取此時的文章標題
    soup = BeautifulSoup(chrome.page_source, "html.parser")
    soup1=soup.find('div',class_="phqjxq-0 fQNVmg")
    title.append(soup1.text)
    #點選 下一篇文章
    NextArticle = chrome.find_element_by_class_name('llPrcG')
    NextArticle.click()
    
    time.sleep(1)
    

import csv

with open('Hsinchu','w', newline='',encoding="utf-8") as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(title)





# sc-1932jlp-0 cqaWIE
# button = driver.find_element_by_class_name(“sc-1vu9ktn-1 LMgkp”)
# button.click()
 
# options = Options()
# options.add_argument("--disable-notifications")
 
# driver = webdriver.Chrome()
# url = 'https://www.dcard.tw/search?query=北歐&forum=house'
# driver.get('https://www.dcard.tw/search/posts?query=理工&forum=job')


# content=requests.get(url)
# # content.add_header('User-Agent', random.choice(my_headers))

# print(content.status_code)
# soup2=BeautifulSoup(content.text,"html.parser")


# soup2_list=soup2.findAll('a',class_="tgn9uw-3 cUGTXH")

# dftitle = pd.DataFrame()
# title2=[]
# for i in soup2_list:
#     title2.append(i.text)
#     dftitle = dftitle.append(title2,ignore_index=True)
# print(title2)




# SCROLL_PAUSE_TIME = 5

# # Get scroll height
# last_height = driver.execute_script("return document.body.scrollHeight")

# while True:
#     # Scroll down to bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#     # Wait to load page
#     time.sleep(SCROLL_PAUSE_TIME)
#     #class="sc-1thlyn3-1 jvJfSN"
    
#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height
# driver = webdriver.Chrome()
# url = 'https://www.dcard.tw/search?query=北歐&forum=house'
# driver.get('https://www.dcard.tw/search/posts?query=理工&forum=job')
# soup=BeautifulSoup(driver.page_source,"html.parser")
# #不知為啥都找不到，可以試試用xthml
# # driver.find_element_by_css_selector('input.sc-ccmip9 hNukmr').click()
# soup_list=soup.findAll('a',class_="tgn9uw-3 cUGTXH")
# time.sleep(10)
# dftitle = pd.DataFrame()
# title=[]
# for i in soup_list:
#     title.append(i.text)
#     # print(title)
# dftitle = dftitle.append(title,ignore_index=True)   

# for x in range(1, 5):
#     ##可能要用累加(?)
#     if(x<5):
#         driver.execute_script("window.scrollTo(0,(document.body.scrollHeight/2.5))")
    
#     else:
#         driver.execute_script("window.scrollTo(0,(document.body.scrollHeight))")
    
    
#     print(x)
#     # print(driver.page_source)
#     time.sleep(10)
#     soup=BeautifulSoup(driver.page_source,"html.parser")


#     soup_list=soup.findAll('a',class_="tgn9uw-3 cUGTXH")
#     # print(len(soup_list))

    
#     title=[]
#     for i in soup_list:
#         title.append(i.text)
#         # print(title)
#     dftitle = dftitle.append(title,ignore_index=True)  
  

# print( dftitle)
# #匯出  
# dftitle.to_excel('cow.xlsx')
# js="var action=document.documentElement.scrollTop=10000"
# chrome.execute_script(js)
# time.sleep(3)
# #將滾動條拖到最頂部
# js="var action=document.documentElement.scrollTop=0"
# chrome.execute_script(js)
# time.sleep(3)

# print("拖動成功")


# content=chrome.get(url)
# content.add_header('User-Agent', random.choice(my_headers))

# print(content.status_code)


# soup=BeautifulSoup(driver.page_source,"html.parser")


# soup_list=soup.findAll('a',class_="tgn9uw-3 cUGTXH")

# dftitle = pd.DataFrame()
# title=[]
# for i in soup_list:
#     title.append(i.text)
#     dftitle = dftitle.append(title,ignore_index=True)
# print(title)

# dftitle.to_excel('Dcard2.xlsx')

#  'https://www.dcard.tw/search/posts?query=58 
# 'https://www.dcard.tw/search?query=台大&forum=house'

# def Crawl(ID):
#     link = 'https://www.dcard.tw/_api/posts/' + str(ID)
#     requ = requests.get(link)
#     rejs = requ.json()
#     return(print(
#         pd.DataFrame(
#         data=
#         [{'ID':rejs['id'],
#           'title':rejs['title'],
#           'content':rejs['content'],
#           'excerpt':rejs['excerpt'],
#           'createdAt':rejs['createdAt'],
#           'updatedAt':rejs['updatedAt'],
#           'commentCount':rejs['commentCount'],
#           'forumName':rejs['forumName'],
#           'forumAlias':rejs['forumAlias'],
#           'gender':rejs['gender'],
#           'likeCount':rejs['likeCount'],
#           'reactions':rejs['reactions'],
#           'topics':rejs['topics']}],
#         columns=['ID','title','content','excerpt','createdAt','updatedAt','commentCount','forumName','forumAlias','gender','likeCount','reactions','topics']))
#     )


# url = 'https://www.dcard.tw/_api/posts?popular=true&limit=100'
# resq = requests.get(url)
# rejs = resq.json()
# df = pd.DataFrame()
# df =df.append(Crawl(235780859))
# for i in range(len(rejs)):
#     df = df.append(Crawl(rejs[i]['id']),ignore_index=True)


# 將資料存到桌面
# print(Crawl(235780859))
# print(df.shape)
# df.to_excel('Dcard4.xlsx')


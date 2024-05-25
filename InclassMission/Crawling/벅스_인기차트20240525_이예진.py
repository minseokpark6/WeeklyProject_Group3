from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])

driver = webdriver.Chrome(options=chrome_options)

import numpy as np 
import pandas as pd

url= 'https://music.bugs.co.kr/chart'
driver.get(url)

#html 다운로드 및 bs4 로 읽기 
from bs4 import BeautifulSoup

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
# # print(soup)

# songs = soup.select("tbody > tr")
# # print(len(songs))
# # print(songs[0])
# # print(soup.select('tr')[1:])

# songs = soup.select('tr')[1:]
# song = songs[0]
# title = song.select('a')
# # print(title[2].text) #supernova 

# #방법 2 
# title = song.select("th > p > a")
# # print(title[0].text) # supernova

# #방법 3 
# title = song.select("p.title > a")
# print(title[0].text) #supernova 

# #가수 찾기 
# singer = song.select("p.artist > a ")
# print(singer[0].text) # aespa

#앨범 찾기 
# songs = soup.select('tr')[1:]
# # print(songs[0])
# song = songs[0]
# album = song.select("td.left > a ")
# # print(album[0])
# print(album[0].text)

#벅스 top100 
from bs4 import BeautifulSoup

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

song_list = []
rank = 1

songs = soup.select('tbody > tr')[:100]
# print(songs[0])

for song in songs:
    title = song.select('th > .title > a')[0].text
    singer = song.select('td > .artist > a')[0].text
    album = song.select("td.left > a ")[0].text
    rank_num = f"{rank}위"
    data = ['Bugs!', rank_num, title, singer, album]
    song_list.append(data)
    rank += 1 
print(song_list)

df = pd.DataFrame(song_list, columns=['서비스업체', '순위', '곡', '제목', '앨범'])

df.to_excel('./05_Webcrawling/WebCrawling_Selenium/Bugs_rank_20240525_이예진.xlsx', index=False)


# 출력
time.sleep(100)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=chrome_options)

import numpy as np 
import pandas as pd

url = 'https://music.bugs.co.kr/chart'
driver.get(url)

# # HTML 다운로드 및 bs4 로 읽기 
html = driver.page_source
soup= BeautifulSoup(html, 'html.parser')

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

df.to_excel('./벅스_뮤직.xlsx', index=False)

print(df)

driver.quit()


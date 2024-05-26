from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import numpy as np
import pandas as pd

# 브라우저 옵션 설정 
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=chrome_options)

# 크롤링 할 사이트 주소 (벅스 뮤직 차트)
url = 'https://music.bugs.co.kr/chart'
driver.get(url)


# HTML 다운로드 및 bs4 로 읽기
from bs4 import BeautifulSoup
html = driver.page_source

soup= BeautifulSoup(html, 'html.parser')

# 필요한 데이터만 가져오기
# 변수 초기화
song_data = []
songs = soup.select('tbody > tr')[:100]
# [1:] 으로 해보니 102개 찍힘 -> 그래서 [:100]으로 함

# 확인용 변수 
# song = songs[0]

# 개수 확인
# print(len(songs))

# 곡 확인용
# title = song.select('p.title > a')[0].text
# print(title)

# 가수 확인용
# singer = song.select('p.artist > a')[0].text
# print(singer)

# 앨범 확인용
# album = song.select('td.left > a')[0].text
# print(album)

# 확인 완료

# for 반복문으로 해당 데이터들 가져오기
for idx, song in enumerate(songs, 1):
    title = song.select('p.title > a')[0].text
    singer = song.select('p.artist > a')[0].text
    album = song.select('td.left > a')[0].text
    print(f'{idx}위: {title}, {singer}, {album}')
    song_data.append(['bugs', idx, title, singer, album])

# 엑셀 파일로 저장
df = pd.DataFrame(song_data, columns=['서비스업체', '순위', '곡명', '가수', '앨범'])
print(df)

df.to_excel('./bugs_rank_20240523.xlsx', index=False)
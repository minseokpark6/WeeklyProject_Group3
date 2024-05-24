from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np 

# 브라우저 옵션 설정
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=chrome_options)

# 원하는 웹페이지로 이동
url = "https://music.bugs.co.kr/chart"
driver.get(url)

# HTML 다운로드 및 bs4로 읽기 
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Top 100 chart 내 정보 가져오기
songs = soup.select('tr')[1:]
data = []
rank = 0

# 출력
for song in songs:
    titles = song.select('p.title > a')
    artists = song.select('p.artist > a')
    albums = song.select('a.album')
    
    if titles and artists and albums:
        title = titles[0].text
        artist = artists[0].text
        album = albums[0].text
            
        rank += 1
        print(f'{rank}위: {title}, {artist}')
        song_list = ['Bugs', rank, title, artist, album]
        data.append(song_list)

# 데이터프레임 변환 및 엑셀파일 출력
Bugs_Top100_chart = pd.DataFrame(data, columns=['서비스업체', '순위', '곡명', '가수', '앨범명'])
Bugs_Top100_chart.to_excel('./BugsTop100Chart_240524.xlsx', index=False)

# 창 닫기
driver.quit()

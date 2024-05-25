from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=chrome_options)

url = 'https://music.bugs.co.kr/chart'
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

songs = soup.select('table.byChart > tbody > tr')
song_data = []
rank = 1

for song in songs:
    title = song.select_one('p.title > a').text.strip()  # 곡 제목
    singer = song.select_one('p.artist > a').text.strip()  # 가수 이름
    song_data.append(['Bugs', rank, title, singer])
    rank += 1


df = pd.DataFrame(song_data, columns=['서비스업체', '순위', '곡 명', '가수'])

print(df)
df.to_excel('./bugs_rank_20240525.xlsx', index=False)

driver.quit()

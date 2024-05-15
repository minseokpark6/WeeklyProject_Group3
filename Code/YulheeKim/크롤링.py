from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Chrome 옵션 설정
chrome_options = Options()
chrome_options.add_argument('--headless')  # 브라우저를 화면에 띄우지 않음
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# ChromeDriver 자동 다운로드 및 설정
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# 크롤링할 URL 설정 (예시로 TripAdvisor의 호텔 리뷰 페이지)
url = "https://www.tripadvisor.com/Hotel_Review-g60763-d1234567-Reviews-Hotel_Name-New_York_City_New_York.html"

# 웹 페이지 열기
driver.get(url)

# 페이지 로딩을 기다림
time.sleep(5)  # 필요한 경우 더 길게 설정

# 리뷰 요소를 찾음 (실제 사이트의 HTML 구조에 따라 조정 필요)
reviews = driver.find_elements(By.CLASS_NAME, 'review-container')

# 리뷰를 순회하며 텍스트를 추출
for review in reviews:
    review_text = review.find_element(By.CLASS_NAME, 'partial_entry').text
    print(review_text)

# 브라우저 종료
driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Chrome 옵션 설정
chrome_options = Options()
chrome_options.add_argument('--headless')  # 브라우저를 화면에 띄우지 않음
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# ChromeDriver 자동 다운로드 및 설정
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# 크롤링할 URL 설정 (예시로 TripAdvisor의 호텔 리뷰 페이지)
url = "https://www.tripadvisor.com/Hotel_Review-g60763-d1234567-Reviews-Hotel_Name-New_York_City_New_York.html"

# 웹 페이지 열기
driver.get(url)

# 페이지 로딩을 기다림
time.sleep(5)  # 필요한 경우 더 길게 설정

# 리뷰 요소를 찾음 (실제 사이트의 HTML 구조에 따라 조정 필요)
reviews = driver.find_elements(By.CLASS_NAME, 'review-container')

# 리뷰를 순회하며 텍스트를 추출
for review in reviews:
    try:
        review_text = review.find_element(By.CLASS_NAME, 'partial_entry').text
        print(review_text)
    except Exception as e:
        print(f"Error extracting review: {e}")

# 브라우저 종료
driver.quit()

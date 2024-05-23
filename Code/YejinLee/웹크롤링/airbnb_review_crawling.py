from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
#브라우저를 자동화한 후 >> browser window 창 유지 
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
#excludeSwitches : 불필요한 로깅 메시지 >> 브라우저에서 제외 

# driver = webdriver.Chrome(options=chrome_options)

import time
import pandas as pd 
from selenium.common.exceptions import NoSuchElementException

def get_airbnb_reviews(url):
    # Chrome 웹드라이버 초기화
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)  # 페이지가 로드될 때까지 충분한 시간 대기

    try:
        # 리뷰 요소들을 찾기 위해 클래스 이름 사용
        reviews = driver.find_elements(By.XPATH, '/html/body/div[9]/div/div/section/div/div/div[2]/div/div[3]/div/div/div/div/div/div/section/div/div[2]/div/section/div[4]/div/div[1]/div[2]/div[1]/div/span/span')
        
        # 리뷰 정보 저장할 리스트 초기화
        review_list = []
        
        # # 각 리뷰 요소에서 텍스트 가져와서 리스트에 저장
        # for review in reviews:
        #     review_text = review.text
        review_list.append(reviews)
        
        return review_list

    finally:
        # 작업 완료 후 웹드라이버 종료
        driver.quit()

# 예시 URL
url = "https://www.airbnb.com/rooms/24524189/reviews?adults=1&category_tag=Tag%3A8851&children=0&enable_m3_private_room=true&infants=0&pets=0&search_mode=flex_destinations_search&check_in=2024-05-29&check_out=2024-06-03&source_impression_id=p3_1715518174_V2A3pp71ULfuUlJt&previous_page_section_name=1000&federated_search_id=49613615-985c-45be-ad2e-531a99a77d1a"

# 함수 호출하여 리뷰 가져오기
reviews = get_airbnb_reviews(url)

# 가져온 리뷰 출력
for idx, review in enumerate(reviews, start=1):
    print(f"리뷰 {idx}: {review}")
    

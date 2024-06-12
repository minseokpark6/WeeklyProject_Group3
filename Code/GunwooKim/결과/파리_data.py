import numpy as np
import pandas as pd
import matplotlib as mpl
from matplotlib import font_manager
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode

# URL에 쿼리 파라미터를 추가하는 함수
def modify_url(url, params):
    url_parts = list(urlparse(url))
    query = dict(parse_qs(url_parts[4]))
    query.update(params)
    url_parts[4] = urlencode(query, doseq=True)
    return urlunparse(url_parts)

# 글꼴 경로 지정
font_path = "./malgun.ttf"  # 윈도우에 설치된 맑은 고딕 폰트 경로

# 폰트 이름 얻어오기
font_name = font_manager.FontProperties(fname=font_path).get_name()

# matplotlib의 rc(run command) 기능을 이용하여 글꼴 설정
mpl.rc('font', family=font_name)

# 유니코드에서 음수 부호 설정
mpl.rc('axes', unicode_minus=False)

path = './파리_data/listings.csv'

raw = pd.read_csv(path)
df = raw.copy()

df = df[['id', 'host_id','host_is_superhost',
        'host_total_listings_count','neighbourhood_cleansed','room_type','accommodates','bathrooms','bedrooms',
        'beds','amenities','price','minimum_nights','maximum_nights','number_of_reviews', 'number_of_reviews_l30d', 'review_scores_rating', 'review_scores_accuracy', 
        'review_scores_cleanliness', 'review_scores_checkin', 'review_scores_communication', 
        'review_scores_location', 'review_scores_value', 'reviews_per_month','listing_url','property_type','number_of_reviews_ltm','has_availability','last_review']]

df = df.rename(columns= {
    'id': '숙소_id',
    'host_id': '호스트_id',
    'host_is_superhost': '슈퍼호스트',
    'host_total_listings_count': '숙소_수',
    'neighbourhood_cleansed': '숙소_지역',
    'room_type': '숙소_유형',
    'accommodates': '수용_인원수',
    'bathrooms': '욕실수',
    'bedrooms': '침실수',
    'beds': '침대수',
    'amenities': '편의시설',
    'price': '숙소_가격',
    'minimum_nights': '최소_숙박일',
    'maximum_nights': '최대_숙박일',
    'number_of_reviews': '리뷰수',
    'number_of_reviews_l30d': '30일_리뷰수',
    'review_scores_rating': '리뷰점수',
    'review_scores_accuracy': '숙소_정확성_리뷰점수',
    'review_scores_cleanliness': '숙소_청결도_리뷰점수',
    'review_scores_checkin': '숙소_체크인_리뷰점수',
    'review_scores_communication': '숙소_소통_리뷰점수',
    'review_scores_location': '숙소_위치_리뷰점수',
    'review_scores_value': '숙소_가격_리뷰점수',
    'reviews_per_month': '평균_리뷰수',
    'listing_url':'url',
    'property_type':'숙소_특징',
    'number_of_reviews_ltm':'12개월_리뷰수',
    'has_availability':'예약가능여부',
    'last_review':'마지막_리뷰'
})
df['위도'] = raw['latitude']
df['경도'] = raw['longitude']

# 슈퍼호스트, 리뷰수 결측치 제거
df = df[~df['슈퍼호스트'].isnull()]
df = df[df['리뷰수'] > 2]

# 숙소가격 null값 제거
df = df[~df['숙소_가격'].isnull()]

# 가격 앞 통화기호 제거
df['숙소_가격'] = df['숙소_가격'].replace('[\$,]', '', regex=True).astype(float)

# 유형 제거 
df = df[(df['숙소_유형'] == 'Entire home/apt') | (df['숙소_유형'] == 'Private room')]

# 12개월 리뷰수 0 개 제거
df = df[df['12개월_리뷰수'] != 0]

# 욕실수, 침실수, 침대수 null값 제거
df = df.dropna(subset=['욕실수', '침실수', '침대수'])

# 리뷰 null값 제거
df = df.dropna(subset=['숙소_정확성_리뷰점수', '숙소_청결도_리뷰점수', '숙소_체크인_리뷰점수', '숙소_소통_리뷰점수', '숙소_위치_리뷰점수', '숙소_가격_리뷰점수'])

# 예약 가능여부 f 버리기
df = df.dropna(subset='예약가능여부')

df_guest_prefer = df[(df['리뷰점수'] >= 4.9) & (df['리뷰수'] >= 5) & (df['슈퍼호스트'] == 't')]
df_non_guest_prefer = df[(df['슈퍼호스트'] == 'f') & (df['리뷰수'] >= 5)].sort_values('리뷰점수', ascending=True).head(len(df_guest_prefer))

# CSV 파일 로드
df_metro = pd.read_csv('./파리_data/paris_stations.csv', delimiter=';')

# 'Coordonnées géographiques' 열을 공백으로 분리하여 새로운 열로 추가
df_metro[['위도', '경도']] = df_metro['Coordonnées géographiques'].str.replace(',', '').str.split(expand=True)

# 위도와 경도 데이터 타입을 float으로 변환
df_metro['위도'] = df_metro['위도'].astype(float)
df_metro['경도'] = df_metro['경도'].astype(float)

# 필요없는 'Coordonnées géographiques' 열 제거
df_metro.drop('Coordonnées géographiques', axis=1, inplace=True)

df_metro = df_metro.rename(columns= {
    'Identifiant station':'역_id',
    'Nom de la station' : '역이름',
    'Capacité de la station' : '역수용인원'
})

df_metro = df_metro[df_metro['역수용인원'] != 0]

df_metro['역 이름 앞부분'] = df_metro['역이름'].apply(lambda x: x.split(' - ')[0])

# '역 이름 앞부분'으로 그룹화하고, 각 그룹

# '역 이름 앞부분'으로 그룹화하고, 각 그룹의 위도와 경도 평균을 계산
station_groups = df_metro.groupby('역 이름 앞부분').agg({
    '위도': 'mean',
    '경도': 'mean'
}).reset_index()

# 새로운 DataFrame 생성
df_station = station_groups.rename(columns={
    '역 이름 앞부분': '역이름'
})

df_station_check = pd.read_csv('./파리_data/Paris_Metro_Stations.csv')

# 데이터를 반환하는 함수
# >>런던_map.py에 데이터 넘겨줘야해서.
def get_guest_prefer_data():
    return df_guest_prefer[['위도', '경도']]

def get_non_guest_prefer_data():
    return df_non_guest_prefer[['위도', '경도']]

def get_station_check_data():
    return df_station_check[['위도', '경도', '역이름']]
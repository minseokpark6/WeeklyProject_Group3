import streamlit as st
import folium
from folium.plugins import MarkerCluster
from folium import FeatureGroup, LayerControl, GeoJson
from streamlit_folium import st_folium
import pandas as pd
import json

import 런던_data

# 사용자 데이터 로드
df_guest_prefer = 런던_data.get_guest_prefer_data()
df_non_guest_prefer = 런던_data.get_non_guest_prefer_data()
df_station = 런던_data.get_station_data()

def create_london_map():
    # 런던 중심부의 위도와 경도
    london_latitude = 51.5074
    london_longitude = -0.1278

    # 런던 지도 생성
    map_london = folium.Map(location=[london_latitude, london_longitude], zoom_start=12, width='100%', height='500px')

    # 랜드마크 위치 데이터
    landmarks = {
        "런던 아이": (51.5033, -0.1196),
        "타워 브리지": (51.5055, -0.0754),
        "버킹엄 궁전": (51.5014, -0.1419),
        "대영 박물관": (51.5194, -0.1270),
        "테이트 모던": (51.5076, -0.0994),
        "세인트 폴 대성당": (51.5138, -0.0984),
        "웨스트민스터 사원": (51.4993, -0.1273),
        "피카딜리 서커스": (51.5101, -0.1342),
        "하이드 파크": (51.5073, -0.1657),
        "캠든 마켓": (51.5416, -0.1469),
        "빅벤": (51.5007, -0.1246),
        "내셔널 갤러리": (51.5089, -0.1283),
        "자연사 박물관": (51.4967, -0.1764),
        "타워 오브 런던": (51.5081, -0.0759),
        "코벤트 가든": (51.5115, -0.1234),
        "리젠트 파크": (51.5313, -0.1569),
        "셔드": (51.5045, -0.0865),
        "킹스 크로스 세인트 판크라스": (51.5308, -0.1238)
    }

    # 런던 경계 데이터 로드 및 추가
    london_boundary_geojson_path = './런던_data/London_boundary.geojson'
    try:
        with open(london_boundary_geojson_path, 'r', encoding='utf-8') as f:
            london_boundary_geojson = json.load(f)
    except FileNotFoundError:
        st.error("런던 경계 파일을 찾을 수 없습니다.")
        st.stop()

    GeoJson(
        london_boundary_geojson,
        name='London Boundary',
        style_function=lambda x: {
            'fillColor': 'blue',
            'color': 'blue',
            'weight': 2,
            'fillOpacity': 0.1
        }
    ).add_to(map_london)

    # 랜드마크에 마커 추가
    for landmark, (lat, lng) in landmarks.items():
        folium.Marker(
            location=[lat, lng],
            icon=folium.Icon(icon='star', prefix='fa', color='blue'),
            popup=landmark
        ).add_to(map_london)

    # 클러스터 객체 생성 및 사용자 데이터 위치 표시
    marker_cluster = MarkerCluster().add_to(map_london)
    for idx, row in df_guest_prefer.iterrows():
        folium.Marker(
            location=[row['위도'], row['경도']],
            icon=folium.Icon(color='green', icon='info-sign'),
            popup='Guest Prefer'
        ).add_to(marker_cluster)

    for idx, row in df_non_guest_prefer.iterrows():
        folium.Marker(
            location=[row['위도'], row['경도']],
            icon=folium.Icon(color='red', icon='info-sign'),
            popup='Non-Guest Prefer'
        ).add_to(marker_cluster)

    # 지하철 레이어 추가
    subway_layer = FeatureGroup(name='Subway Stations', show=False)
    for idx, row in df_station.iterrows():
        folium.Marker(
            location=[row['위도'], row['경도']],
            icon=folium.Icon(icon='subway', prefix='fa', color='black'),
            popup=f"{row['역이름']} Station"
        ).add_to(subway_layer)
    subway_layer.add_to(map_london)

    # 레이어 컨트롤 추가
    LayerControl().add_to(map_london)

    # Streamlit을 통해 folium 지도를 표시
    st.title('런던 지도')
    st_folium(map_london)
  

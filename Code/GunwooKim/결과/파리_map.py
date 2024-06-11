import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from folium import FeatureGroup, LayerControl, GeoJson
from shapely.geometry import shape
import streamlit.components.v1 as components
import json
import 파리_data

# 사용자 데이터 로드
df_guest_prefer = 파리_data.get_guest_prefer_data()
df_non_guest_prefer = 파리_data.get_non_guest_prefer_data()
df_station_check = 파리_data.get_station_check_data()

def create_paris_map():
    try:
        # 파리 중심부의 위도와 경도
        paris_latitude = 48.8566
        paris_longitude = 2.3522

        # 파리 지도 생성
        map_paris = folium.Map(location=[paris_latitude, paris_longitude], zoom_start=12)

        # 랜드마크 위치 데이터
        landmarks = {
            "에펠탑": (48.8584, 2.2945),
            "루브르 박물관": (48.8606, 2.3376),
            "노트르담 대성당": (48.8529, 2.3500),
            "개선문": (48.8738, 2.2950),
            "가르니에 궁전": (48.8719, 2.3316),
            "사크레쾨르 대성당": (48.8867, 2.3431),
            "생트 샤펠": (48.8554, 2.3450),
            "알렉산드르 3세 다리": (48.8639, 2.3136),
            "마레 지구": (48.8575, 2.3588),
            "몽마르트": (48.8867, 2.3431),
            "팡테옹": (48.8463, 2.3460),
            "룩셈부르크 정원": (48.8462, 2.3371),
            "오르세 미술관": (48.8600, 2.3257),
            "샹젤리제 거리": (48.8696, 2.3079),
            "레 장발리드": (48.8565, 2.3126),
            "콩코르드 광장": (48.8656, 2.3211),
            "퐁피두 센터": (48.8606, 2.3522),
            "라 데팡스": (48.8900, 2.2400),
            "갤러리 라파예트": (48.8738, 2.3320),
            "그레뱅 박물관": (48.8718, 2.3422)
        }

        # 파리 경계 데이터 로드
        paris_boundary_geojson_path = './파리_data/paris.geojson'
        try:
            with open(paris_boundary_geojson_path, 'r', encoding='utf-8') as f:
                paris_boundary = json.load(f)
        except FileNotFoundError:
            st.error("파리 경계 파일을 찾을 수 없습니다.")
            return None

        # Shapely geometry 객체 생성
        try:
            paris_area = shape(paris_boundary['features'][0]['geometry'])
        except KeyError:
            st.error("파리 경계 데이터의 형식이 올바르지 않습니다.")
            return None

        # 마커 클러스터 생성
        marker_cluster = MarkerCluster().add_to(map_paris)

        # 각 랜드마크에 대한 마커 추가
        for landmark, (lat, lng) in landmarks.items():
            folium.Marker(
                location=[lat, lng],
                icon=folium.Icon(icon='star', color='blue'),
                popup=landmark
            ).add_to(map_paris)

        # 지하철 레이어 생성
        subway_layer = FeatureGroup(name='Subway Stations', show=False)

        # df_station_check 데이터를 이용해 지하철역 위치에 마커 추가
        for idx, row in df_station_check.iterrows():
            if pd.notna(row['위도']) and pd.notna(row['경도']):
                folium.Marker(
                    location=[row['위도'], row['경도']],
                    icon=folium.Icon(icon='train', prefix='fa', color='cadetblue'),
                    popup=f"{row['역이름']} Station"
                ).add_to(subway_layer)

        # 지하철 레이어를 지도에 추가
        subway_layer.add_to(map_paris)

        # 파리 경계 레이어 추가
        GeoJson(
            paris_boundary,
            name='Paris Boundary',
            style_function=lambda x: {
                'fillColor': 'blue',
                'color': 'blue',
                'weight': 2,
                'fillOpacity': 0.1
            }
        ).add_to(map_paris)

        # df_guest_prefer의 위치 표시 (클러스터에 추가)
        for idx, row in df_guest_prefer.iterrows():
            folium.Marker(
                location=[row['위도'], row['경도']],
                icon=folium.Icon(color='green', icon='info-sign'),
                popup='Guest Prefer'
            ).add_to(marker_cluster)

        # df_non_guest_prefer의 위치 표시 (클러스터에 추가)
        for idx, row in df_non_guest_prefer.iterrows():
            folium.Marker(
                location=[row['위도'], row['경도']],
                icon=folium.Icon(color='red', icon='info-sign'),
                popup='Non-Guest Prefer'
            ).add_to(marker_cluster)

        # 트램 레이어
        tram_layer = FeatureGroup(name='Tram Stops')
        tram_geojson_path = './파리_data/paris_tram.geojson'
        try:
            with open(tram_geojson_path, 'r', encoding='utf-8') as f:
                tram_geojson = json.load(f)
            GeoJson(tram_geojson, name='Tram Stops').add_to(tram_layer)
            tram_layer.add_to(map_paris)
        except FileNotFoundError:
            st.error("트램 데이터 파일을 찾을 수 없습니다.")
        except json.JSONDecodeError:
            st.error("트램 데이터 파일을 읽을 수 없습니다.")

        # 레이어 컨트롤 추가
        LayerControl().add_to(map_paris)

        return map_paris
    except Exception as e:
        st.error(f"지도를 생성하는 중 오류가 발생했습니다: {e}")
        return None

if __name__ == "__main__":
    create_paris_map()

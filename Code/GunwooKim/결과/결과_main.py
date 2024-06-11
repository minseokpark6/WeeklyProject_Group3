import streamlit as st
import folium
from streamlit_folium import folium_static
from 런던_map import create_london_map
from 파리_map import create_paris_map

# 페이지 설정
st.set_page_config(layout="wide")

# 사용자 정의 CSS를 사용하여 탭 텍스트 크기 및 타이틀 색상 변경
st.markdown("""
    <style>
    .stTabs [role="tab"] {
        font-size: 24px;
        font-weight: bold;
    }
    .css-10trblm {
        color: #FF5A5F;
    }
    </style>
    """, unsafe_allow_html=True)

# 타이틀
st.markdown("<h1 style='color: #FF5A5F;'>Airbnb 숙소 분석</h1>", unsafe_allow_html=True)

# 탭 생성
tabs = st.tabs(["런던", "파리"])

with tabs[0]:
    # 사이드바 내용 (런던)
    st.sidebar.header("런던 사이드바")
    # 예: 런던 데이터에 관련된 입력 요소들
    london_option = st.sidebar.selectbox("런던 옵션", ["옵션 1", "옵션 2", "옵션 3"])

    # 런던 지도 생성 및 렌더링
    london_map = create_london_map()
    if london_map is not None:
        folium_static(london_map, width=1200, height=600)
    else:
        st.error("런던 지도를 생성하는 데 실패했습니다.")

with tabs[1]:
    # 사이드바 내용 (파리)
    st.sidebar.header("파리 사이드바")
    # 예: 파리 데이터에 관련된 입력 요소들
    paris_option = st.sidebar.selectbox("파리 옵션", ["옵션 A", "옵션 B", "옵션 C"])

    # 파리 지도 생성 및 렌더링
    paris_map = create_paris_map()
    if paris_map is not None:
        folium_static(paris_map, width=1200, height=600)
    else:
        st.error("파리 지도를 생성하는 데 실패했습니다.")
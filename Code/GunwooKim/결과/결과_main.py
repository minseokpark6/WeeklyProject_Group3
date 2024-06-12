import streamlit as st
import folium
from streamlit_folium import folium_static
from 런던_map import create_london_map
from 파리_map import create_paris_map
from 런던_sidebar import apply_sidebar_styles as apply_london_sidebar_styles, initialize_sidebar_state as initialize_london_sidebar_state, render_sidebar as render_london_sidebar
from 파리_sidebar import apply_sidebar_styles as apply_paris_sidebar_styles, initialize_sidebar_state as initialize_paris_sidebar_state, render_sidebar as render_paris_sidebar

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

# 초기 상태 설정
if 'tab' not in st.session_state:
    st.session_state['tab'] = "런던"

# 탭 생성
tabs = st.tabs(["런던", "파리"])

# 탭 렌더링
for i, tab_name in enumerate(["런던", "파리"]):
    with tabs[i]:
        if tab_name == "런던":
            st.session_state['tab'] = tab_name
            
            apply_london_sidebar_styles()
            initialize_london_sidebar_state()
            render_london_sidebar(key='london_sidebar_button')
            
            # 런던 지도 생성 및 렌더링
            london_map = create_london_map()
            if london_map is not None:
                folium_static(london_map, width=1200, height=600)
            else:
                st.error("런던 지도를 생성하는 데 실패했습니다.")
                
        elif tab_name == "파리":
            st.session_state['tab'] = tab_name
            
            apply_paris_sidebar_styles()
            initialize_paris_sidebar_state()
            render_paris_sidebar(key='paris_sidebar_button')
            
            # 파리 지도 생성 및 렌더링
            paris_map = create_paris_map()
            if paris_map is not None:
                folium_static(paris_map, width=1200, height=600)
            else:
                st.error("파리 지도를 생성하는 데 실패했습니다.")
    
    
    

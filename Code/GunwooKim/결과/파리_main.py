import streamlit as st
from 파리_map import create_paris_map

import 파리_sidebar

# 페이지 설정
# st.set_page_config(layout="wide")

def main():
    # 사이드바 스타일 적용
    파리_sidebar.apply_sidebar_styles()

    # 사이드바 상태 초기화
    파리_sidebar.initialize_sidebar_state()

    # 사이드바 렌더링
    파리_sidebar.render_sidebar()

    # 메인 화면 내용
    create_paris_map()  # 파리 맵 생성 함수 호출

if __name__ == "__main__":
    main()


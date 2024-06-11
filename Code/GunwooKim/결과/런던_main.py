import streamlit as st
from 런던_map import create_london_map

import 런던_sidebar

def main():
    # 사이드바 스타일 적용
    런던_sidebar.apply_sidebar_styles()

    # 사이드바 상태 초기화
    런던_sidebar.initialize_sidebar_state()

    # 사이드바 렌더링
    런던_sidebar.render_sidebar()

    # 메인 화면 내용
    create_london_map()  # 런던 맵 생성 함수 호출
    st.write("여기에 메인 화면 내용을 추가하세요.")

if __name__ == "__main__":
    main()

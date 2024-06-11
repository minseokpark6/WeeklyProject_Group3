import streamlit as st

def apply_sidebar_styles():
    # 사이드바를 오른쪽에 배치하기 위해 CSS 스타일 적용
    st.markdown(
        """
        <style>
        .css-1d391kg {display: none}
        .css-18e3th9 {flex-direction: row-reverse;}
        </style>
        """,
        unsafe_allow_html=True
    )

def initialize_sidebar_state():
    # 사이드바 숨기기/보이기 기능 초기화
    if 'sidebar_state' not in st.session_state:
        st.session_state.sidebar_state = 'visible'

def toggle_sidebar():
    # 사이드바 숨기기/보이기 토글
    if st.session_state.sidebar_state == 'visible':
        st.session_state.sidebar_state = 'hidden'
    else:
        st.session_state.sidebar_state = 'visible'

def render_sidebar():
    # 사이드바 토글 버튼
    st.sidebar.button('사이드바 숨기기/보이기', on_click=toggle_sidebar)

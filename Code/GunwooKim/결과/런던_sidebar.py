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
    # 사이드바 초기화 함수 (필요 시 구현)
    pass

def render_sidebar(key=None):
    # 런던 데이터 텍스트 굵게 표시하고 h3 크기로 설정
    st.sidebar.markdown("## **런던 데이터**")
    
    # 각각의 이미지와 텍스트 추가
    st.sidebar.markdown("**숙소 유형별 숙소 수**")
    st.sidebar.image("./런던_data/img/런던_숙소유형별_숙소수.png", use_column_width=True)
    
    st.sidebar.markdown("**게스트 선호 숙소 여부에 따른 숙소 가격**")
    st.sidebar.image("./런던_data/img/런던_게스트선호숙소여부에 따른 숙소가격.png", use_column_width=True)
    
    st.sidebar.markdown("**런던_역500m안 숙소 수**")
    st.sidebar.image("./런던_data/img/런던_역500m.png", use_column_width=True)
    
    st.sidebar.markdown("**런던_랜드마크1km안 숙소 수**")
    st.sidebar.image("./런던_data/img/런던_랜드마크1km.png", use_column_width=True)
    
    st.sidebar.markdown("**게스트 선호여부에 따른 리뷰점수 비교**")
    st.sidebar.image("./런던_data/img/게스트 선호여부에 따른 리뷰점수 비교.png", use_column_width=True)
    
    st.sidebar.markdown("**게스트선호여부에따른 침실수 욕실수 침대수**")
    st.sidebar.image("./런던_data/img/게스트선호여부에따른 침실수 욕실수 침대수.png", use_column_width=True)
    
    st.sidebar.markdown("**게스트선호여부별 호스트 신원**")
    st.sidebar.image("./런던_data/img/게스트선호여부별 호스트 신원.png", use_column_width=True)
    
    st.sidebar.markdown("**게스트 선호 여부별 프로필 사진**")
    st.sidebar.image("./런던_data/img/게스트 선호 여부별 프로필 사진.png", use_column_width=True)
    
    st.sidebar.markdown("**게스트 선호에 따른 답변 평균시간**")
    st.sidebar.image("./런던_data/img/게스트 선호에 따른 답변 평균시간.png", use_column_width=True)
    
    st.sidebar.markdown("**게스트 선호에 따른 숙소가격분포**")
    st.sidebar.image("./런던_data/img/게스트 선호에 따른 숙소가격분포.png", use_column_width=True)
    
    st.sidebar.markdown("**게스트 선호 여부별 수용인원수 분포밀도**")
    st.sidebar.image("./런던_data/img/게스트 선호 여부별 수용인원수 분포밀도.png", use_column_width=True)
    
    st.sidebar.markdown("**게스트선호 여부별편의시설 개수 분포밀도**")
    st.sidebar.image("./런던_data/img/게스트선호 여부별편의시설 개수 분포밀도.png", use_column_width=True)
    
    st.sidebar.markdown("**게스트선호인 숙소 단어 빈도수**")
    st.sidebar.image("./런던_data/img/게스트선호인 숙소 단어 빈도수.png", use_column_width=True)
    
    st.sidebar.markdown("**게스트선호가 아닌 숙소 단어빈도수**")
    st.sidebar.image("./런던_data/img/게스트선호가 아닌 숙소 단어빈도수 .png", use_column_width=True)
    
    st.sidebar.markdown("**단어빈도수 막대그래프**")
    st.sidebar.image("./런던_data/img/단어빈도수 막대그래프.png", use_column_width=True)
    
    st.sidebar.markdown("**게스트선호숙소인 긍정 빈도수**")
    st.sidebar.image("./런던_data/img/게스트선호숙소인 긍정 빈도수.png", use_column_width=True)
    
    st.sidebar.markdown("**게스트선호숙소인 부정빈도수**")
    st.sidebar.image("./런던_data/img/게스트선호숙소인 부정빈도수.png", use_column_width=True)
    
    st.sidebar.markdown("**게스트선호가 아닌 숙소 긍정단어 빈도수**")
    st.sidebar.image("./런던_data/img/게스트선호가 아닌 숙소 긍정단어 빈도수.png", use_column_width=True)
    
    st.sidebar.markdown("**게스트선호가 아닌 숙소 부정단어 빈도수**")
    st.sidebar.image("./런던_data/img/게스트선호가 아닌 숙소 부정단어 빈도수.png", use_column_width=True)
    
    st.sidebar.markdown("**게스트선호숙소여부 긍부정별 빈도수 막대그래프**")
    st.sidebar.image("./런던_data/img/게스트선호숙소여부 긍부정별 빈도수 막대그래프.png", use_column_width=True)
    
    # HTML 링크 추가
    st.sidebar.markdown("**토픽 분석 결과**")
    st.sidebar.markdown(
    """
    <a href="file:///C:/Users/rladn/Desktop/mulcam/주간프로젝트/code/런던_data/결과_html/게스트선호인%20숙소의%20전체%20토픽.html" target="_blank">게스트선호인 숙소의 전체 토픽</a><br>
    <a href="./런던_data/결과_html/게스트 선호 숙소인 긍정단어 토픽모델링.html" target="_blank">게스트 선호 숙소인 긍정단어 토픽모델링</a><br>
    <a href="./런던_data/결과_html/게스트 선호 숙소인 부정단어 토픽모델링.html" target="_blank">게스트 선호 숙소인 부정단어 토픽모델링</a><br>
    <a href="./런던_data/결과_html/게스트 선호가 아닌 숙소의 긍정단어 토픽모델링.html" target="_blank">게스트 선호가 아닌 숙소의 긍정단어 토픽모델링</a><br>
    <a href="./런던_data/결과_html/게스트 선호가 아닌 숙소의 부정단어 토픽모델링.html" target="_blank">게스트 선호가 아닌 숙소의 부정단어 토픽모델링</a>
    """,
    unsafe_allow_html=True
    )


# 메인 함수
def main():
    apply_sidebar_styles()
    initialize_sidebar_state()
    render_sidebar()

if __name__ == "__main__":
    main()

import streamlit as st
# 데이터 프레임 가져오는 라이브러리
import pandas as pd
# 사진을 가져오는 라이브러리
from PIL import Image
from streamlit.proto.Audio_pb2 import Audio

def main():

    img=Image.open('data/image_01.jpg')
    df=pd.read_csv('data/players01.csv')
    
    # 사이드 바 만들기
    st.title('최고몸값의 축구선수')
    st.header('내가 좋아하는 선수 찾기')
    select_1=st.sidebar.selectbox('선수 찾기',
    ['Total 선수','Position 선수 선택하기','Team 선수 선택하기'])
    
    
    # 'Total'별 선수 페이지 만들기
    if select_1 == 'Total 선수':
        if st.checkbox('최고의 몸값 선수 보기'):
            st.subheader('Kylian Mbappé')
            st.image(img)
    # 유튜브 영상 넣는것   <iframe width="560" height="315" src="https://www.youtube.com/embed/QTu_pO8eMxc?start=53" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            st.text('음바페 하이라이트 링크 : https://www.youtube.com/watch?v=QTu_pO8eMxc')
            st.dataframe(df.iloc[:1,1:11])  
    # 데이터 프레임이 맞는지 확인차원 
         # st.dataframe(df)      
        
        # st.selectbox('최고 몸값 찾기',['.','정렬2'])







if __name__ == '__main__':
    main()
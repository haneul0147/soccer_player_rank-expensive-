from numpy import imag
import streamlit as st
# 데이터 프레임 가져오는 라이브러리
import pandas as pd
# 사진을 가져오는 라이브러리
from PIL import Image
from streamlit.proto.Audio_pb2 import Audio


from position import run_postiton_app


# 해야할것들 : 영상 넣기 , 배경화면 넣기
def main():

    img1=Image.open('data/image_01.jpg')
    img3=Image.open('data/image_03.jpg')
    img4=Image.open('data/image_04.jpg')
    img5=Image.open('data/image_05.jpg')
    img6=Image.open('data/image_06.jpg')
    df=pd.read_csv('data/players01.csv')
    
    # 사이드 바 만들기
   
    choice=st.sidebar.radio('',
    ['Home','Rank','Position 선수 선택하기','Team 선수 선택하기'])
    
    # 'Total'별 선수 페이지 만들기
    if choice == 'Home':
        st.title('who is expensives ransom??')
        st.image(img3,width=300)
        
        
    if choice == 'Rank':  
        st.title('최고의 주가를 가지고 있는 선수들')
         
        if st.checkbox('가장 몸값높은 선수 TOP5 보기'):
            st.write('1위 : 킬리안 음바페 ( 한화: 약 1575억)')
            st.image(img1,width=350,use_column_width=20)
            st.write('2위 : 엘링 홀란드 ( 한화: 약 1574억)')  
            st.image(img4,width=350) 
            st.write('3위 : 해리 케인( 한화: 약 1569억)')
            st.image(img5,width=350) 
            st.write('4위 : 모하메드 살라')
            st.write('공동 5위 : 로멜루 루카쿠,케빈 더 데브라이너,네이마르')
            st.dataframe(df.iloc[:8,1:11])
        if  st.checkbox('현재 최고의 몸값 선수 프로필 보기'):
            st.subheader('Kylian Mbappé Lottin(킬리안 음바페)')
            st.image(img1)

            st.write('''출생년도:1998년12월20일생 
            \n국적: France  키: 178CM
            \n 포지션: 스트라이커(ST)
            \n 키: 178CM''')
            st.write('소속 팀(team) :Paris Saint-Germain Football Club ')
            st.image(img6,width=180) 
            
            # 유튜브 영상 넣는것   <iframe width="560" height="315" src="https://www.youtube.com/embed/QTu_pO8eMxc?start=53" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>         
            st.dataframe(df.iloc[:1,1:11]) 
            st.text('음바페 하이라이트 링크 : https://www.youtube.com/watch?v=QTu_pO8eMxc')
    elif choice == 'Position 선수 선택하기':
        run_postiton_app()

            
           
            
        
    # # 데이터 프레임이 맞는지 확인차원 
    #      # st.dataframe(df)      
        
    #     # st.selectbox('최고 몸값 찾기',['.','정렬2'])







if __name__ == '__main__':
    main()
from numpy import imag
import streamlit as st
# 데이터 프레임 가져오는 라이브러리
import pandas as pd
# 사진을 가져오는 라이브러리
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit.elements.selectbox import SelectboxMixin
from streamlit.proto.Audio_pb2 import Audio
from Team import run_team
from country import run_country
from position import run_postiton_app
img43=Image.open('data/image_43.jpg') # 프리미어 리그 로고
st.set_page_config(page_title='Expensive player Top 500',
page_icon=img43,layout='wide',initial_sidebar_state='collapsed')

# 해야할것들 : 영상 넣기 , 배경화면 넣기
def main():
    

    
    img1=Image.open('data/image_01.jpg') # 음바페 사진 
    img3=Image.open('data/image_03.jpg') # 리그 사진들 
    img4=Image.open('data/image_04.jpg') # 홀란드 
    img5=Image.open('data/image_05.jpg') # 케인
    img6=Image.open('data/image_06.jpg') # 파리 
    img41=Image.open('data/image_41.jpg') #단상
    img42=Image.open('data/image_42.jpg') #손흥민
   
    # 몸값에 대한 데이터 가져오기
    df=pd.read_csv('data/players01.csv',index_col=0)
    df_name=df['Name'] 
    # 사이드 바 만들기
   
    choice=st.sidebar.radio('',
    ['Home','Rank','Position 선수 선택하기','Team별 선수보기','나라별 선수보기'])
    
    # 'Total'별 선수 페이지 만들기
    
    
    if choice == 'Home':
              
        st.title('축구선수 몸값 TOP500')
        st.image(img3,width=600)
        
        names =st.text_input('원하는 선수를 입력하세요')
        # if names == df['Name']:
        st.dataframe(df.loc[df['Name'] == names,])
        

        # st.error('선수이름이 맞지 않습니다.')
        #     st.write("선수 이름이 맞지않아요")     
        st.write('선수 이름 정보(높은 몸값 순으로 정렬)')
        st.write(df['Name'].values)
        
        
    elif choice == 'Rank':  
        # st.image(img41,width=480)
        st.title('최고 몸값 선수들의 순위 보기')             
        if  st.checkbox('현재 최고 몸값 선수'):
            st.subheader('Kylian Mbappé Lottin(킬리안 음바페)')
            st.video('https://youtu.be/E0CnctfxUyI?t=9',format='video/mp4')
            st.write('''출생년도:1998년12월20일생 
            \n국적: France  키: 178CM
            \n 포지션: 스트라이커(ST)
            \n 키: 178CM''')
            st.write('소속 팀(team) :Paris Saint-Germain Football Club ')
            st.image(img6,width=180)      
            st.dataframe(df.iloc[:1,:11]) 
            
        if st.checkbox('가장 몸값높은 선수 TOP5 보기'):
            st.write('1위 : 킬리안 음바페 ( 한화: 약1,930억)')
            st.image(img1,width=350,use_column_width=20)
            st.write('2위 : 엘링 홀란드 ( 한화: 약 1,809억)')  
            st.image(img4,width=350) 
            st.write('3위 : 해리 케인( 한화: 약 1,447억억)')
            st.image(img5,width=350) 
            st.write('4위 : 모하메드 살라')
            st.write('공동 5위 : 로멜루 루카쿠,케빈 더 데브라이너,네이마르')
            st.dataframe(df.iloc[:8,:11])
        
        
        if  st.checkbox('한국 선수 보기'):  
            st.subheader('손흥민(Son heung min)')
            st.video('https://youtu.be/OXlTN6sH6Ag',format='video/mp4')
            st.write('몸값 기준 15위')
            st.write('소속팀: 토트넘 홋스퍼 FC')
            st.write('76.5000유로 (데이터기준 한화 약 1,025억) ')
            st.write('ps: 2021-11-26일자 기준 세계 몸값 6위// 850£ 한화(약 1140억원)')
            st.dataframe(df.loc[df['Country']== 'Korea, South',])
    elif choice == 'Position 선수 선택하기':
        # 포지션 파일에 함수 
        run_postiton_app()
    
    elif choice == 'Team별 선수보기':
        run_team()
    
    elif choice == '나라별 선수보기':
        run_country()

   




if  __name__ == '__main__':
    main()

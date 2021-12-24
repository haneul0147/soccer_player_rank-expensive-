from os import write
from numpy import imag
import streamlit as st
# 데이터 프레임 가져오는 라이브러리
import pandas as pd
# 사진을 가져오는 라이브러리
from PIL import Image
import seaborn as sns
from streamlit.elements.selectbox import SelectboxMixin
from streamlit.proto.Audio_pb2 import Audio
from streamlit.proto.Checkbox_pb2 import Checkbox
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
    img45=Image.open('data/image_45.jpg') #리그 선수 
   
   



    # 몸값에 대한 데이터 가져오기
    df=pd.read_csv('data/players01.csv',index_col=0)
    df_name=df['Name'] 
    # 사이드 바 만들기
    frist=st.text_input('"hello"을 입력해주세요')
    if frist=='hello':
        choice=st.sidebar.radio('',
        ['목차','Search','Position 선수 선택하기','선수보기','Rank'])
        st.write('please settings dark mode / 다크모드로 이용 부탁드립니다.')
        # 'Total'별 선수 페이지 만들기
        
        if choice == '목차':
            st.title('Welcome')
            st.subheader('Who is your favorite football player?')
            if st.button('Start'):            
                st.balloons()
                st.title('BEST player worth TOP500!!')
                st.video('https://youtu.be/M5JyZLR68gU?t=10',start_time=13,format='video/mp4')
            
        elif choice == 'Rank': 
            choice2=st.sidebar.selectbox('선수보기',
                ['최고 몸값 선수들의 순위 보기','가장 몸값높은 선수 TOP5 보기','한국 선수 보기'])                  
            st.title('최고 몸값 선수들의 순위 보기')             
            if choice2 == '최고 몸값 선수들의 순위 보기':
                    
                if  st.checkbox('현재 최고 몸값 선수'):
                    st.subheader('Kylian Mbappé Lottin(킬리안 음바페)(한화: 약1,930억)')
                    st.image(img1,width=700)
                    st.dataframe(df.iloc[:1,:11]) 
                    st.write('''출생년도:1998년12월20일생 
                    \n국적: France  키: 178CM
                    \n 포지션: 스트라이커(ST)
                    \n 키: 178CM''')
                    st.write('소속 팀(team) :Paris Saint-Germain Football Club ')
                    st.image(img6,width=180)
                    st.video('https://youtu.be/E0CnctfxUyI?t=9',format='video/mp4')      
                
            
            if choice2 == '가장 몸값높은 선수 TOP5 보기':
                if st.checkbox('가장 몸값높은 선수 TOP5 보기'):
                    col1, col2 = st.columns(2)
                    col2.subheader('1위 : 킬리안 음바페 ( 한화: 약1,930억)')
                    col1.image(img1,width=500,use_column_width=20)
                    # st.subheader('1위 : 킬리안 음바페 ( 한화: 약1,930억)')
                    # st.image(img1,width=350,use_column_width=20)
                    col1, col2 = st.columns(2)
                    col2.subheader('2위 : 엘링 홀란드 ( 한화: 약 1,809억)')  
                    col1.image(img4,width=500)
                    # st.subheader('2위 : 엘링 홀란드 ( 한화: 약 1,809억)')  
                    # st.image(img4,width=350) 
                    col1, col2 = st.columns(2)
                    col2.subheader('3위 : 해리 케인( 한화: 약 1,447억억)') 
                    col1.image(img5,width=500) 
                    # st.subheader('3위 : 해리 케인( 한화: 약 1,447억억)')
                    # st.image(img5,width=350) 
                    st.write('4위 : 모하메드 살라')
                    st.write('공동 5위 : 로멜루 루카쿠,케빈 더 데브라이너,네이마르')
                    st.dataframe(df.iloc[:8,:11])
            
        
            if choice2 == '한국 선수 보기':
                if  st.sidebar.button('여기를 눌러주세요'): 
                    
                    col1, col2 = st.columns(2)
                    col2.title('손흥민(Son heung min)🤸🏻') 
                    col1.image(img42,width=500) 
                    # st.title('손흥민(Son heung min)🤸🏻')
                    # st.image(img42,width=500)
                    st.subheader('몸값 기준 15위')
                    st.write('소속팀: 토트넘 홋스퍼 FC')
                    st.write('76.5000유로 (데이터기준 한화 약 1,025억) ')
                    st.write('ps: 2021-11-26일자 기준 세계 몸값 6위// 850£ 한화(약 1140억원)')
                    st.dataframe(df.loc[df['Country']== 'Korea, South',])
                    st.video('https://youtu.be/OXlTN6sH6Ag',format='video/mp4')




        elif choice == 'Search':
                
            # st.title('축구선수 몸값 TOP500')
        
            st.title('축구선수 몸값 TOP500') 
            st.image(img45,width=900)
            
            names =st.text_input('원하는 선수를 입력하면 정보를 알려줍니다.')
            # if names == df['Name']:
            st.dataframe(df.loc[df['Name'] == names,])
            

            # st.error('선수이름이 맞지 않습니다.')
            #     st.write("선수 이름이 맞지않아요")     
        
            st.write('선수 이름 정보(높은 몸값 순으로 정렬)')
            
            
            col1, col2 = st.columns(2)
            col1.dataframe(df['Name'].values,width=600,height=400)
            if col2.checkbox('유명한 선수이름 몇개 보기'):
                col2.subheader('Lionel Messi')
                col2.subheader('Cristiano Ronaldo')
                col2.subheader('Heung-min Son')
                col2.subheader('Neymar')
                col2.subheader('Paul Pogba')
            
        
        elif choice == 'Position 선수 선택하기':
            # 포지션 파일에 함수 
            run_postiton_app()
        
        elif choice == '선수보기':
            choice3=st.sidebar.selectbox('',['선택','Team별 선수보기','나라별 선수보기'])  
        
            if choice3 == 'Team별 선수보기':
                run_team()        
            if choice3 == '나라별 선수보기':
                run_country()
    elif frist!= 'hello' and len(frist)>1 :
        st.error('다시 입력해주세요')
        
        
    
if  __name__ == '__main__':
    main()

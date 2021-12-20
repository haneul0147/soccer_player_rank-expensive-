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

    img1=Image.open('data/image_01.jpg') # 음바페 사진 
    img3=Image.open('data/image_03.jpg') # 리그 사진들 
    img4=Image.open('data/image_04.jpg') # 홀란드 
    img5=Image.open('data/image_05.jpg') # 케인
    img6=Image.open('data/image_06.jpg') # 파리 
    img41=Image.open('data/image_41.jpg') #단상
    img42=Image.open('data/image_42.jpg') #손흥민
    # 몸값에 대한 데이터 가져오기
    df=pd.read_csv('data/players01.csv',index_col=0)
    
    # 사이드 바 만들기
   
    choice=st.sidebar.radio('',
    ['Home','Rank','Position 선수 선택하기'])
    
    # 'Total'별 선수 페이지 만들기
    if choice == 'Home':
        st.title('축구선수 몸값 TOP500')
        st.image(img3,width=600)
        
        names =st.text_input('원하는 선수를 입력하세요')
        if names :
            st.dataframe(df.loc[df['Name'] == names,])        
        st.write('선수 이름 정보')
        st.write(df['Name'].values)

        
        
    if choice == 'Rank':  
        st.image(img41,width=480)
        st.title('최고 몸값의  선수 찾기')
         
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
            st.dataframe(df.iloc[:1,:11]) 
            st.text('음바페 하이라이트 링크 : https://www.youtube.com/watch?v=QTu_pO8eMxc')
        if st.checkbox('한국 선수 보기'):
            st.image(img42)
            st.subheader('손흥민')
            st.write('몸값 기준 15위')
            st.write('소속팀: 토트넘 홋스퍼 FC')
            st.write('76.5000유로 (데이터기준 한화 약 1,025억) ')
            st.write('ps: 2021-11-26일자 기준 세계 몸값 6위// 850£ 한화(약 1140억원)')
            st.dataframe(df.loc[df['Country']== 'Korea, South',])
    elif choice == 'Position 선수 선택하기':
        # 포지션 파일에 함수 
        run_postiton_app()

    elif choice == 'Team 선수 선택하기':
        pass  
           
            
        
    # # 데이터 프레임이 맞는지 확인차원 
    #      # st.dataframe(df)      
        
    #     # st.selectbox('최고 몸값 찾기',['.','정렬2'])







if __name__ == '__main__':
    main()
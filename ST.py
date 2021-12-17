import streamlit as st 
import pandas as pd 
from PIL import Image
def run_ST():
    # 각 이미지 가져오기
    img7=Image.open('data/image_07.jpg') # 레반도프 스키
    img8=Image.open('data/image_08.jpg') # 카림 아데예미
    img1=Image.open('data/image_01.jpg') # 킬리안 음바페
    img9=Image.open('data/image_09.jpg') # 파울로 디발라
    img10=Image.open('data/image_10.jpg') # 주앙 펠리스 
    img11=Image.open('data/image_11.jpg') # 토마스 뮐러
    img12=Image.open('data/image_12.jpg') #비니시우스 주니오르
    img13=Image.open('data/image_13.jpg')#잭 그릴리쉬 
    img14=Image.open('data/image_14.jpg')#에베르통 소아레스
    img15=Image.open('data/image_15.jpg')#살라
    img16=Image.open('data/image_16.jpg')# 테테
    # 데이터 프레임 가져오기
    df=pd.read_csv('data/players01.csv')
    # 중앙 공격수의 데이터를 가져오기 한 것 
    cf=df.loc[df['Position']=='Centre-Forward',]
    cf_mat=cf.sort_values('Matches',ascending=False)
    cf_goals=cf.sort_values('Goals',ascending=False)
    cf_value=cf.sort_values('Markey Value In Millions(£)',ascending=False)
    # 세컨 공격수의 데이터를 가져오기 한 것
    ss=df.loc[df['Position']=='Second Striker',]
    ss_goals=ss.sort_values('Goals',ascending=False)
    ss_value=ss.sort_values('Markey Value In Millions(£)',ascending=False)    
    ss_mat=ss.sort_values('Matches',ascending=False)
    # 왼쪽 윙어 데이터 가져오기 한것
    lw=df.loc[df['Position']=='Left Winger',]
    lw_goals=lw.sort_values('Goals',ascending=False)
    lw_value=lw.sort_values('Markey Value In Millions(£)',ascending=False)    
    lw_mat=lw.sort_values('Matches',ascending=False)
    # 오른쪽 윙어 데이터 가져오기 한것
    rw=df.loc[df['Position']=='Right Winger',]
    rw_goals=rw.sort_values('Goals',ascending=False)
    rw_value=rw.sort_values('Markey Value In Millions(£)',ascending=False)    
    rw_mat=rw.sort_values('Matches',ascending=False)
    
    
    
    choice_fw=st.radio('포지션 선택',['원하는 포지션을 선택하세요','Centre-Forward(중앙 공격수)',
        'Second Striker(세컨드 스트라이커)','Left Winger(왼쪽 윙어)','Right Winger(오른쪽 윙어)'])
   
   
    # 중앙 공격수 선택
    if choice_fw =='Centre-Forward(중앙 공격수)':
        choice_fw2=st.selectbox('선택',['선택','득점률 가장 높은 공격수','가장 몸값이 비싼 선수','가장 많은 경기를 뛴 선수'])
        # 중앙 공격수 중 득점률이 높은 공격수
        if choice_fw2=='득점률 가장 높은 공격수':
            st.write('1위 ! Robert Lewandowski(로베르트 레반도프스키)')
            st.write('소속팀:FC 바이에른 뮌헨')
            st.image(img7,width=450)
            st.dataframe(cf_goals.iloc[:3,[1,8,5,2]])
        # 중앙 공격수 중 가장 몸값이 비싼 선수
        if choice_fw2=='가장 몸값이 비싼 선수' :
            st.write('1위 ! Kylian Mbappé(킬리안 음바페)')
            st.write('소속팀:파리 생 제르망')
            st.image(img1,width=450)               
            st.dataframe(cf_value.iloc[:3,[1,4,6,3]])
        # 중앙 공격수 중 가장 경기를많이 뛴 선수
        if choice_fw2=='가장 많은 경기를 뛴 선수':
            st.write('1위 ! Karim Adeyemi(카림 아데예미)')
            st.write('소속팀:FC 레드불 잘츠부르크')
            st.image(img8,width=450)                
            st.dataframe(cf_mat.iloc[:3,1:9])
    
    
    # 세컨드 스트라이커 선택
    if choice_fw =='Second Striker(세컨드 스트라이커)' :
        choice_fw2=st.selectbox('선택',['선택','득점률 가장 높은 공격수','가장 몸값이 비싼 선수','가장 많은 경기를 뛴 선수'])
        # 세컨드 스트라이크 중 득점률이 높은 공격수
        if choice_fw2=='득점률 가장 높은 공격수':
            st.write('1위 ! Paulo Dybala(파울로 디발라)')
            st.write('소속팀:유벤투스 FC')
            st.image(img9,width=450)
            st.dataframe(ss_goals.iloc[:3,[1,8,5,2]]) 
        # 세컨드 스트라이크 중 가장 몸값이 비싼 선수
        if choice_fw2=='가장 몸값이 비싼 선수' :
            st.write('1위 ! João Félix(주앙 펠릭스)')
            st.write('소속팀:아틀레티코 마드리드')
            st.image(img10,width=450)               
            st.dataframe(ss_value.iloc[:3,[1,4,6,3]])
        # 세컨드 스트라이크 중 가장 경기를 많이 뛴 선수
        if choice_fw2=='가장 많은 경기를 뛴 선수' :
            st.write('1위 ! Thomas Müller(토마스 뮐러)')
            st.write('소속팀:FC 바이에른 뮌헨')
            st.image(img11,width=450)               
            st.dataframe(ss_mat.iloc[:3,1:9])
   
   
    # Left winger  왼쪽 윙어 선택
    if choice_fw =='Left Winger(왼쪽 윙어)' :
        choice_fw2=st.selectbox('선택',['선택','득점률 가장 높은 공격수','가장 몸값이 비싼 선수','가장 많은 경기를 뛴 선수'])
        # 왼쪽 윙어 중 득점률이 높은 공격수 
        if choice_fw2=='득점률 가장 높은 공격수':
            st.write('1위 ! Vinícius Júnior(비니시우스 주니오르)')
            st.write('소속팀:레알마드리드 CF')
            st.image(img12,width=450)
            st.dataframe(ss_goals.iloc[:3,[1,8,5,2]]) 
        # 왼쪽 윙어 중 가장 몸값이 비싼 선수
        if choice_fw2=='가장 몸값이 비싼 선수' :
            st.write('1위 ! Jack Grealish(잭 그릴리시)')
            st.write('소속팀:맨처스터 시티 FC')
            st.image(img13,width=450)               
            st.dataframe(ss_value.iloc[:3,[1,4,6,3]])
        # 왼쪽 윙어 중 가장 경기를 많이 뛴 선수
        if choice_fw2=='가장 많은 경기를 뛴 선수' :
            st.write('1위 ! Everton Soares(에베르통 소아레스)')
            st.write('소속팀:SL 벤피카')
            st.image(img14,width=450)               
            st.dataframe(ss_mat.iloc[:3,1:9])

     # Right winger  오른쪽 윙어 선택
    if choice_fw =='Right Winger(오른쪽 윙어)' :
        choice_fw2=st.selectbox('선택',['선택','득점률 가장 높은 공격수','가장 몸값이 비싼 선수','가장 많은 경기를 뛴 선수'])
        # 오른쪽 윙어 중 득점률이 높은 공격수 
        if choice_fw2=='득점률 가장 높은 공격수':
            st.write('1위 ! Mohamed Salah(모하메드 살라)')
            st.write('소속팀:리버풀 FC')
            st.image(img15,width=450)
            st.dataframe(rw_goals.iloc[:3,[1,8,5,2]]) 
        # 왼쪽 윙어 중 가장 몸값이 비싼 선수
        if choice_fw2=='가장 몸값이 비싼 선수' :
            st.write('1위 ! Mohamed Salah(모하메드 살라)')
            st.write('소속팀:리버풀 FC')
            st.image(img15,width=450)               
            st.dataframe(rw_value.iloc[:3,[1,4,6,3]])
        # 오른쪽 윙어 중 가장 경기를 많이 뛴 선수
        if choice_fw2=='가장 많은 경기를 뛴 선수' :
            st.write('1위 ! Tetê (마테우스 카르도주 레무스 마르칭스)')
            st.write('소속팀:FC 샤흐타르 도네츠크')
            st.image(img16,width=450)               
            st.dataframe(rw_mat.iloc[:3,1:9])
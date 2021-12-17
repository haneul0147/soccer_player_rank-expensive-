import streamlit as st 
import pandas as pd 
from PIL import Image
def run_strlike():

    img7=Image.open('data/image_07.jpg')
    img8=Image.open('data/image_08.jpg')
    img1=Image.open('data/image_01.jpg')
    df=pd.read_csv('data/players01.csv')
    cf=df.loc[df['Position']=='Centre-Forward',]
    cf_mat=cf.sort_values('Matches',ascending=False)
    cf_goals=cf.sort_values('Goals',ascending=False)
    cf_value=cf.sort_values('Markey Value In Millions(£)',ascending=False)
    choice_fw=st.radio('포지션 선택',['선택','Centre-Forward(중앙 공격수)',
        'Second Striker(세컨드 스트라이커)','Left Winger(왼쪽 윙어)','Right Winger(오른쪽 윙어)'])
    # 중앙 공격수 선택
    if choice_fw =='Centre-Forward(중앙 공격수)':
        choice_fw2=st.selectbox('선택',['선택','득점률 가장 높은 공격수','가장 몸값이 비싼 선수','가장 많은 경기를 뛴 선수'])
        # 중앙 공격수 중 득점률이 높은 공격수
        if choice_fw2=='득점률 가장 높은 공격수':
            st.write('1위 ! Robert Lewandowski')
            st.write('소속팀:FC 바이에른 뮌헨')
            st.image(img7,width=400)
            st.dataframe(cf_goals.iloc[:3,1:9]) 
        # 중앙 공격수 중 가장 몸값이 비싼 선수
        if choice_fw2=='가장 몸값이 비싼 선수' :
            st.write('1위 ! Kylian Mbappé')
            st.write('소속팀:파리 생 제르망')
            st.image(img1,width=400)               
            st.dataframe(cf_value.iloc[:3,1:9])
        # 중앙 공격수 중 가장 경기를많이 뛴 선수
        if choice_fw2=='가장 많은 경기를 뛴 선수':
            st.write('1위 ! Karim Adeyemi')
            st.write('소속팀:FC 레드불 잘츠부르크')
            st.image(img8,width=400)                
            st.dataframe(cf_mat.iloc[:3,1:9])
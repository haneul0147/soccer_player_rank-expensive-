import streamlit as st 
import pandas as pd 
from PIL import Image



def run_gk():
    # 데이터 프레임 가져오기
    df=pd.read_csv('data/players01.csv')
    # 골키퍼 의 데이터를 가져오기 한 것 
    gk=df.loc[df['Position']=='Goalkeeper',]
    gk_mat=gk.sort_values('Matches',ascending=False)
    gk_value=gk.sort_values('Markey Value In Millions(£)',ascending=False)
    
    # 이미지 가져오기
    img39=Image.open('data/image_39.jpg') # 일란 메실러
    img40=Image.open('data/image_40.jpg') # 얀 오블라크

    
    selcted_gk=st.selectbox('선택',['선택','가장 많은 경기를 뛴 선수',
    '가장 몸값이 비싼 선수'] )
    
    if selcted_gk == '가장 많은 경기를 뛴 선수':
        st.write('1위 ! Illan Meslier(일란 메실러)')
        st.write('소속팀:리즈 유나이티드FC')
        st.image(img39,width=450)
        st.dataframe(gk_mat.iloc[:3,[1,7,4,6]]) 

    elif selcted_gk == '가장 몸값이 비싼 선수':
        st.write('1위 ! Jan Oblak(얀 오블라크)')
        st.write('소속팀:아틀레티코 마드리드 (AT)')
        st.image(img40,width=450)
        st.dataframe(gk_value.iloc[:3,[1,4,6,5]]) 
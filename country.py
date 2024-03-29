from re import S
from numpy import arange
import streamlit as st 
import pandas as pd 
from PIL import Image
# import matplotlib.pyplot as plt
import seaborn as sns
# import plotly.express as px
# import plotly.figure_factory as ff
import numpy as np
img46=Image.open('data/image_46.jpg') #세계 지도

df=pd.read_csv('data/players01.csv',index_col=0)
def run_country():
    st.title('나라 별 선수 보기')
    st.image(img46,width=600)
    if st.checkbox('나라별 선수 찾기'):
        choice=st.selectbox('몸 값이 높은 순으로 나열됩니다.',df['Country'].unique())
        st.dataframe(df[df['Country']==choice]) 
        df2=df[df['Country']==choice]
        chart1=df2['Position']
        chart1=chart1.value_counts()
        
        chart2=df2['Goals']
        chart2=chart2.value_counts()
       
        means=df2['Matches']
        means=means.mean()
        
        # 골 평균         
        means2=df2['Goals']
        means2=means2.mean()

        # 포지션 코드
        position=df2['Position'].value_counts()
        position=position.index[0]
        if st.button('국가 별 포지션당 선수 수 보기'):
            chart_data = pd.DataFrame(chart1)
            st.bar_chart(chart_data,height=350,use_container_width=True)
            st.subheader(choice+'팀의 가장 많은 포지션은'+position+'입니다')
        
        if st.button('국가 별 골 갯수 보기'):
            chart_data = pd.DataFrame(chart2)
            st.bar_chart(chart_data,height=350,use_container_width=True)
            st.subheader(choice+'의팀 평균 골 갯수는'+str(round(means2,1)) + '개 입니다.')

     
        
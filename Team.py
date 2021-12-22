
import streamlit as st 
import pandas as pd 
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
df=pd.read_csv('data/players01.csv',index_col=0)
img44=Image.open('data/image_44.jpg') # 리그사진
def run_team():  
    if st.checkbox('Click here') :
        st.title('Team 별로 선수 보기')        
        
        
        st.subheader('원하는 팀을 선택하세요')   
        choice=st.selectbox('몸 값이 높은 순으로 나열됩니다.',df['Club'].unique())
        
        st.dataframe(df[df['Club']==choice]) 
        df2=df[df['Club']==choice]
        
        chart1=df2['Matches']
        chart1=chart1.value_counts()
        
        chart2=df2['Goals']
        chart2=chart2.value_counts()
        
        
        # 경기 평균
        means=df2['Matches']
        means=means.mean()
        
        # 골 평균 
        
        means2=df2['Goals']
        
        means2=means2.mean()
       
        
        

        if st.checkbox('팀 선수 경기 그래프보기'):
           
            chart_data = pd.DataFrame(chart1)
            st.bar_chart(chart_data,use_container_width=True)
           
            st.subheader(choice+'의 팀 평균 경기수는'+str(round(means,1)) + '게임 입니다.')
            
        elif st.checkbox('팀 골 평균 그래프 보기'):
            
            chart_data = pd.DataFrame(chart2)
            st.bar_chart(chart_data,use_container_width=True)
           
            st.subheader(choice+'의팀 평균 골 갯수는'+str(round(means2,1)) + '개 입니다.')
         
        st.image(img44,width=450)        
        
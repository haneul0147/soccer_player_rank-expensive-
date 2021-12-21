
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
        choice=st.selectbox('몸 값이 높은 순으로 나열됩니다.',df['Club'])
        st.dataframe(df[df['Club']==choice]) 
        df2=df[df['Club']==choice]
        means=df2['Matches']
        means=means.value_counts()
        means=round(means,1)
        means2=df2['Goals']
        means2=means2.value_counts()
        means2=round(means2,1)

        if st.checkbox('팀 선수 경기 그래프보기'):
           
            chart_data = pd.DataFrame(means)
            st.bar_chart(chart_data,use_container_width=True)
            
            st.subheader(choice+'의 팀 평균 경기수는'+str(means.mean()) + '게임 입니다.')
            
        elif st.checkbox('팀 골 평균 그래프 보기'):
            fig2 = plt.figure()
            
            chart_data = pd.DataFrame(means2)
            st.bar_chart(chart_data,use_container_width=True)
            
            st.subheader(choice+'의팀 평균 골 갯수는'+str(means2.mean()) + '개 입니다.')
         
        st.image(img44,width=450)        
        
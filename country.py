from re import S
from numpy import arange
import streamlit as st 
import pandas as pd 
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.figure_factory as ff
import numpy as np

df=pd.read_csv('data/players01.csv',index_col=0)
def run_country():
    st.title('나라 별 선수 보기')
    if st.checkbox('나라별 선수 찾기'):
        choice=st.selectbox('몸 값이 높은 순으로 나열됩니다.',df['Country'])
        st.dataframe(df[df['Country']==choice]) 
        df2=df[df['Country']==choice]
        means=df2['Position']
        means=means.value_counts()
    
        if st.checkbox('국가 별 포지션당 선수 수 보기'):
            chart_data = pd.DataFrame(means)
            st.bar_chart(chart_data,use_container_width=True)
        #     # chart_data = df2['position']
        #     # st.line_chart(chart_data) 
        
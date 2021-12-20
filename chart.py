from random import choice
from re import X
import streamlit as st 
import pandas as pd 
from PIL import Image
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit.elements import selectbox
import plotly.express as px 


def run_chart_app():
    st.title('차트로 몸 값 비교하기')
    df=pd.read_csv('data/players01.csv',index_col=0)
 
    
    # 비싼 몸값 top500 중 가장 많은 팀
    # df2=df.groupby('Club')['Markey Value In Millions(£)'].sum()
    # df2=df2.sort_values(ascending=False).head(10)
    
    # def run_chart_app(self,snumber):
    #         df = self.copy()
    #         try:
    #             df = df[df['season']==snumber].groupby(['character'])['dialogue'].apply(lambda x:' '.join(x)).reset_index()
    #             df['spoken_words'] = df.dialogue.str.split().str.len()
    #             df = self.data_sort(df)
    #             return df
    #         except:
    #             # print("Invalid season number or record number")
    #             return 
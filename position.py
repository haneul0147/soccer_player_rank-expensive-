import streamlit as st 
import pandas as pd 
from PIL import Image

from strike import run_strlike
def run_postiton_app():
        img7=Image.open('data/image_07.jpg')
        img8=Image.open('data/image_08.jpg')
        img1=Image.open('data/image_01.jpg')

        df=pd.read_csv('data/players01.csv')
        cf=df.loc[df['Position']=='Centre-Forward',]
        cf_mat=cf.sort_values('Matches',ascending=False)
        cf_goals=cf.sort_values('Goals',ascending=False)
        cf_value=cf.sort_values('Markey Value In Millions(£)',ascending=False)
        st.title('포지션별 선수 찾기')
        choice_p=st.selectbox('포지션 선택',['선택', 'ST(공격수)','MF(미드필더)',
                        'DF(수비수)','GK (골키퍼)'])
        if choice_p =='ST(공격수)':
            run_strlike()
               
                
        
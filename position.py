from numpy import e
import streamlit as st 
import pandas as pd 
from PIL import Image
from DF import run_df
from GK import run_gk
from MF import run_mf
from ST import run_ST


def run_postiton_app():
                        
    st.title('포지션별 최고 선수 찾기')
    
    choice_p=st.selectbox('포지션 선택',['선택', 'ST(공격수)','MF(미드필더)',
                    'DF(수비수)','GK (골키퍼)'])
    if choice_p =='ST(공격수)':
        # ST.py 파일  안에 있는 함수 
        run_ST()
    elif choice_p =='MF(미드필더)':
        # MF.py 파일 안에 있는 함수
        run_mf()  
    elif choice_p =='DF(수비수)':
        run_df()
    elif choice_p =='GK (골키퍼)':
        run_gk()
            
           
        
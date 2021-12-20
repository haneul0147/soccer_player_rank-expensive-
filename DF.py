import streamlit as st 
import pandas as pd 
from PIL import Image

def run_df():
    # 데이터 프레임 가져오기
    df=pd.read_csv('data/players01.csv')
    # 중앙 수비수의 데이터를 가져오기 한 것 
    cb=df.loc[df['Position']=='Centre-Back',]
    cb_mat=cb.sort_values('Matches',ascending=False)
    cb_goals=cb.sort_values('Goals',ascending=False)
    cb_value=cb.sort_values('Markey Value In Millions(£)',ascending=False)
    # 오른쪽 수비수의 데이터를 가져오기 한 것
    rb=df.loc[df['Position']=='Right-Back',]
    rb_goals=rb.sort_values('Goals',ascending=False)
    rb_value=rb.sort_values('Markey Value In Millions(£)',ascending=False)    
    rb_mat=rb.sort_values('Matches',ascending=False)
    # 왼쪽 수비수 데이터 가져오기 한것
    lb=df.loc[df['Position']=='Left-Back',]
    lb_goals=lb.sort_values('Goals',ascending=False)
    lb_value=lb.sort_values('Markey Value In Millions(£)',ascending=False)    
    lb_mat=lb.sort_values('Matches',ascending=False)

     # 이미지 가져오기
    img30=Image.open('data/image_30.jpg') # 아리츠 엘루스톤도
    img31=Image.open('data/image_31.jpg') # 후벵 디아스
    img32=Image.open('data/image_32.jpg') # 브누와 바디아쉴   
    img33=Image.open('data/image_33.jpg') # 하파엘 게헤이루
    img34=Image.open('data/image_34.jpg') # 알폰소 데이비스
    img35=Image.open('data/image_35.jpg') # 알렉스 그리말도 
    img36=Image.open('data/image_36.jpg') # 노사이르 마즈라우이 
    img37=Image.open('data/image_37.jpg') # 트렌트 알렉산더아놀드 
    img38=Image.open('data/image_38.jpg') # 도도 
    
    choice_den=st.radio('포지션 선택',['원하는 포지션을 선택하세요','Centre-Back(중앙 수비수)',
        'Left-Back(왼쪽 수비수)','Right-Back(오른쪽 수비수)'])

    # 중앙 수비수 선택
    if choice_den =='Centre-Back(중앙 수비수)':
        choice_de2=st.selectbox('선택',['선택','득점률 가장 높은 수비수','가장 몸값이 비싼 선수','가장 많은 경기를 뛴 선수'])
        # 중앙 수비수 중 득점률이 높은 수비수
        if choice_de2=='득점률 가장 높은 수비수':
            st.write('1위 ! Aritz Elustondo(아리츠 엘루스톤도)')
            st.write('소속팀:레알 소시에다드')
            st.image(img30,width=450)
            st.dataframe(cb_goals.iloc[:3,[1,8,5,6]]) 
        # 중앙 수비수 중 가장 몸값이 비싼 선수
        if choice_de2=='가장 몸값이 비싼 선수' :
            st.write('1위 ! Rúben Dias(후벵 디아스)')
            st.write('소속팀:맨체스터 시티 FC')
            st.image(img31,width=450)               
            st.dataframe(cb_value.iloc[:3,[1,4,6,5]])
        # 중앙 수비수 중 가장 경기를많이 뛴 선수
        if choice_de2=='가장 많은 경기를 뛴 선수':
            st.write('1위 ! Benoît Badiashile(브누와 바디아쉴)')
            st.write('소속팀:AS 모나코')
            st.image(img32,width=450)                
            st.dataframe(cb_mat.iloc[:3,[1,7,4,6]])
    
    #------------------------------------왼쪽 수비수
    # 왼쪽 수비수 선택
    if choice_den =='Left-Back(왼쪽 수비수)':
        choice_de2=st.selectbox('선택',['선택','득점률 가장 높은 수비수','가장 몸값이 비싼 선수','가장 많은 경기를 뛴 선수'])
        # 왼쪽 수비수 중 득점률이 높은 수비수
        if choice_de2=='득점률 가장 높은 수비수':
            st.write('1위 ! Raphaël Guerreiro(하파엘 게헤이루)')
            st.write('소속팀:보루시아 도르트문트')
            st.image(img33,width=450)
            st.dataframe(lb_goals.iloc[:3,[1,8,5,6]]) 
        # 왼쪽 수비수 중 가장 몸값이 비싼 선수
        if choice_de2=='가장 몸값이 비싼 선수' :
            st.write('1위 ! Alphonso Davies(알폰소 데이비스)')
            st.write('소속팀:FC 바이에른 뮌헨')
            st.image(img34,width=450)               
            st.dataframe(lb_value.iloc[:3,[1,4,6,5]])
        # 왼쪽 수비수 중 가장 경기를많이 뛴 선수
        if choice_de2=='가장 많은 경기를 뛴 선수':
            st.write('1위 ! Alejandro Grimaldo(알렉스 그리말도)')
            st.write('소속팀:SL 벤피카')
            st.image(img35,width=450)                
            st.dataframe(lb_mat.iloc[:3,[1,7,4,6]])

    #------------------------------------오른쪽 수비수
    # 오른쪽 수비수 선택
    if choice_den =='Right-Back(오른쪽 수비수)':
        choice_de2=st.selectbox('선택',['선택','득점률 가장 높은 수비수','가장 몸값이 비싼 선수','가장 많은 경기를 뛴 선수'])
        # 오른쪽 수비수 중 득점률이 높은 수비수
        if choice_de2=='득점률 가장 높은 수비수':
            st.write('1위 ! Noussair Mazraoui(노사이르 마즈라우이)')
            st.write('소속팀:AFC 아약스')
            st.image(img36,width=450)
            st.dataframe(rb_goals.iloc[:3,[1,8,5,6]]) 
        # 오른쪽 수비수 중 가장 몸값이 비싼 선수
        if choice_de2=='가장 몸값이 비싼 선수' :
            st.write('1위 ! Trent Alexander-Arnold(트렌트 알렉산더아놀드)')
            st.write('소속팀:리버풀 FC')
            st.image(img37,width=450)               
            st.dataframe(rb_value.iloc[:3,[1,4,6,5]])
        # 오른쪽 수비수 중 가장 경기를많이 뛴 선수
        if choice_de2=='가장 많은 경기를 뛴 선수':
            st.write('1위 ! Dodô(도도)')
            st.write('소속팀:FC 샤흐타르 도네츠크')
            st.image(img38,width=450)                
            st.dataframe(rb_mat.iloc[:3,[1,7,4,6]])
import streamlit as st 
import pandas as pd 
from PIL import Image

def run_mf():
    # 이미지 가져오기
    img17=Image.open('data/image_17.jpg') # 데용
    img18=Image.open('data/image_18.jpg') # 웬델
    img19=Image.open('data/image_19.jpg') # 로렌초
    img20=Image.open('data/image_20.jpg') # 요주아 키미히
    img21=Image.open('data/image_21.jpg') # 산드로 토날리
    img22=Image.open('data/image_22.jpg') # 오렐리앵 추아메니
    img23=Image.open('data/image_23.jpg') # 사카
    img24=Image.open('data/image_24.jpg') # 루이스 디아스
    img25=Image.open('data/image_25.jpg') # 바쿠
    img26=Image.open('data/image_26.jpg') # 코로나 
    img27=Image.open('data/image_27.jpg') # 데브라이너
    img28=Image.open('data/image_28.jpg') # 크리스토퍼은쿤쿠
    img29=Image.open('data/image_29.jpg') # 소피앙 디옴 



    # 데이터 프레임 가져오기
    df=pd.read_csv('data/players01.csv')
    
    # 공격형 미드필더의 데이터를 가져오기 한 것 
    am=df.loc[df['Position']=='Attacking Midfield',]
    am_mat=am.sort_values('Matches',ascending=False)
    am_goals=am.sort_values('Goals',ascending=False)
    am_value=am.sort_values('Markey Value In Millions(£)',ascending=False)
    
    # 중앙 미드필더의 데이터를 가져오기 한 것 
    cam=df.loc[df['Position']=='Central Midfield',]
    cam_mat=cam.sort_values('Matches',ascending=False)
    cam_goals=cam.sort_values('Goals',ascending=False)
    cam_value=cam.sort_values('Markey Value In Millions(£)',ascending=False)
    # 수비형 미드필더의 데이터를 가져오기 한 것
    dm=df.loc[df['Position']=='Defensive Midfield',]
    dm_goals=dm.sort_values('Goals',ascending=False)
    dm_value=dm.sort_values('Markey Value In Millions(£)',ascending=False)    
    dm_mat=dm.sort_values('Matches',ascending=False)
    # 왼쪽 미드필더 데이터 가져오기 한것
    lm=df.loc[df['Position']=='Left Midfield',]
    lm_goals=lm.sort_values('Goals',ascending=False)
    lm_value=lm.sort_values('Markey Value In Millions(£)',ascending=False)    
    lm_mat=lm.sort_values('Matches',ascending=False)
    # 오른쪽 미드필더 데이터 가져오기 한것
    rm=df.loc[df['Position']=='Right Midfield',]
    rm_goals=rm.sort_values('Goals',ascending=False)
    rm_value=rm.sort_values('Markey Value In Millions(£)',ascending=False)    
    rm_mat=rm.sort_values('Matches',ascending=False)
   
   
#----------------------------------------------------------
   
    choice_mf=st.radio('포지션 선택',['원하는 포지션을 선택하세요','Attacking Midfield(공격형 미드필더)','Central Midfield(중앙 미드필더)','Defensive Midfield(수비형 미드필더)','Left Midfield(왼쪽 미드필더)','Right Midfield(오른쪽 미드필더)'])
   
   #----------------공격형 미드필더
   
    if choice_mf == 'Attacking Midfield(공격형 미드필더)':
        choice_mf2=st.selectbox('선택',['선택','득점률 가장 높은 미드필더','가장 몸값이 비싼 선수','가장 많은 경기를 뛴 선수'])
        # 공격형 미드필더 중 득점률이 높은 미드필더
        if choice_mf2=='득점률 가장 높은 미드필더':
            st.write('1위 ! Christopher Nkunku(크리스토퍼 은쿤쿠)')
            st.write('소속팀:RB 라이프치히')
            st.image(img28,width=450)
            st.dataframe(am_goals.iloc[:3,[1,8,5,6]]) 

        # 공격형 미드필더 중 가장 몸값이 비싼 선수
        if choice_mf2=='가장 몸값이 비싼 선수' :
            st.write('1위 ! Kevin De Bruyne (케빈 더 브라위너)')
            st.write('소속팀:맨체스터 시티 FC')
            st.image(img27,width=450)               
            st.dataframe(am_value.iloc[:3,[1,4,6,5]])
        # 공격형 미드필더 중 가장 경기를많이 뛴 선수
        if choice_mf2=='가장 많은 경기를 뛴 선수':
            st.write('1위 ! Sofiane Diop(소피앙 디옵)')
            st.write('소속팀:AS 모나코 ')
            st.image(img29,width=450)                
            st.dataframe(am_mat.iloc[:3,[1,7,4,6]])


    
    
    
    #----------------- 중앙 미드필더

    
    elif choice_mf == 'Central Midfield(중앙 미드필더)':
        choice_mf2=st.selectbox('선택',['선택','득점률 가장 높은 미드필더','가장 몸값이 비싼 선수','가장 많은 경기를 뛴 선수'])
        
        # 중앙 미드필더 중 득점률이 높은 미드필더
        if choice_mf2=='득점률 가장 높은 미드필더':
            st.write('1위 ! Lorenzo Pellegrini(로렌초 펠레그리니)')
            st.write('소속팀:AS 로마')
            st.image(img19,width=450)
            st.dataframe(cam_goals.iloc[:3,[1,8,5,6]]) 

        # 중앙 미드필더 중 가장 몸값이 비싼 선수
        if choice_mf2=='가장 몸값이 비싼 선수' :
            st.write('1위 ! Frenkie de Jong (프렌키 데 용)')
            st.write('소속팀:FC 바로셀로나')
            st.image(img17,width=450)               
            st.dataframe(cam_value.iloc[:3,[1,4,6,5]])
        # 중앙 미드필더 중 가장 경기를많이 뛴 선수
        if choice_mf2=='가장 많은 경기를 뛴 선수':
            st.write('1위 ! Wendel(웬델)')
            st.write('소속팀:FC 제니트 상트페테르부르크 ')
            st.image(img18,width=450)                
            st.dataframe(cam_mat.iloc[:3,[1,7,4,6]])


        #-----------------------수비형 미드필더
    if choice_mf == 'Defensive Midfield(수비형 미드필더)':
        choice_mf2=st.selectbox('선택',['선택','득점률 가장 높은 미드필더','가장 몸값이 비싼 선수','가장 많은 경기를 뛴 선수'])    
       
        # 수비형 미드필더 중 득점률이 높은 미드필더
        if choice_mf2=='득점률 가장 높은 미드필더':
            st.write('1위 ! Joshua Kimmich(요주아 키미히)')
            st.write('소속팀:FC 바이에른 뮌헨')
            st.image(img20,width=450)
            st.dataframe(dm_goals.iloc[:3,[1,8,5,6]]) 

        # 수비형 미드필더 중 가장 몸값이 비싼 선수
        if choice_mf2=='가장 몸값이 비싼 선수' :
            st.write('1위 ! Joshua Kimmich (요주아 키미히)')
            st.write('소속팀:FC 바이에른 뮌헨')
            st.image(img20,width=450)               
            st.dataframe(dm_value.iloc[:3,[1,4,6,5]])
        # 수비형 미드필더 중 가장 경기를많이 뛴 선수
        if choice_mf2=='가장 많은 경기를 뛴 선수':
            st.write('공동 1위 ! 산드로 토날리/오렐리앵 추아메니')
            st.write('소속팀:AC밀란/ AS모나코 ')
            st.image(img21,width=300)
            st.image(img22,width=300)                
            st.dataframe(dm_mat.iloc[:3,[1,7,4,6]])

# ----------------왼쪽 미드필더 
    if choice_mf == 'Left Midfield(왼쪽 미드필더)':
        choice_mf2=st.selectbox('선택',['선택','득점률 가장 높은 미드필더','가장 몸값이 비싼 선수','가장 많은 경기를 뛴 선수'])    
       
        # 왼쪽 미드필더 중 득점률이 높은 미드필더
        if choice_mf2=='득점률 가장 높은 미드필더':
            st.write('1위 ! 루이스 디아스 (Luis Díaz)')
            st.write('소속팀:FC포르투')
            st.image(img24,width=450)
            st.dataframe(lm_goals.iloc[:3,[1,8,5,6]]) 

        # 왼쪽 미드필더 중 가장 몸값이 비싼 선수
        if choice_mf2=='가장 몸값이 비싼 선수' :
            st.write('1위 ! Bukayo Saka (부카요 사카)')
            st.write('소속팀:아스널 FC')
            st.image(img23,width=450)               
            st.dataframe(lm_value.iloc[:3,[1,4,6,5]])
        # 왼쪽 미드필더 중 가장 경기를많이 뛴 선수
        if choice_mf2=='가장 많은 경기를 뛴 선수':
            st.write('1위 ! 루이스 디아스 (Luis Díaz)')
            st.write('소속팀:FC포르투 ')
            st.image(img24,width=450)
            st.dataframe(lm_mat.iloc[:3,[1,7,4,6]])
            
            # with col1:
            #     st.image(img21,width=300)
            # with col2:
            #     st.image(img22,width=300)                
            
# -------------------오른쪽 미드필더
    if choice_mf == 'Right Midfield(오른쪽 미드필더)':
        choice_mf2=st.selectbox('선택',['선택','득점률 가장 높은 미드필더','가장 몸값이 비싼 선수','가장 많은 경기를 뛴 선수'])    
       
        # 오른쪽 미드필더 중 득점률이 높은 미드필더
        if choice_mf2=='득점률 가장 높은 미드필더':
            st.write('1위 ! Ridle Baku (리들레 바쿠)')
            st.write('소속팀:Vfl 볼프스부르크')
            st.image(img25,width=450)
            st.dataframe(rm_goals.iloc[:3,[1,8,5,6]]) 

        # 오른쪽 미드필더 중 가장 몸값이 비싼 선수
        if choice_mf2=='가장 몸값이 비싼 선수' :
            st.write('1위 ! Jesús Manuel Corona (헤수스 코로나)')
            st.write('소속팀:FC 포르투')
            st.image(img26,width=450)               
            st.dataframe(rm_value.iloc[:3,[1,4,6,5]])
        # 오른쪽 미드필더 중 가장 경기를많이 뛴 선수
        if choice_mf2=='가장 많은 경기를 뛴 선수':
            st.write('1위 ! Ridle Baku (리들레 바쿠)')
            st.write('소속팀:Vfl 볼프스부르크 ')
            st.image(img25,width=450)
            st.dataframe(rm_mat.iloc[:3,[1,7,4,6]])
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


def run_eda_app():

    st.info('EDA 화면 입니다')
    
    st.text('차량 정보 데이터프레임')
    df = pd.read_csv('./data/Car_Purchasing_Data.csv')
    st.dataframe(df)

    st.success('기초통계데이터 확인하기')
    if st.checkbox('통게데이터 보기') :
        st.dataframe(df.describe())
    
    st.success('상관계수')
    if st.checkbox('상관계수 보기'):
        st.dataframe(df.corr(numeric_only=True))

    st.text('최대 /최소 데이터 확인하기')
    column_list = df.columns[ 4 :]
    selected_colums = st.selectbox('컬럼을 선택하세요', column_list)

    st.dataframe(df.loc[ df[selected_colums] == df[selected_colums].min() , ] )

    st.dataframe( df.loc[ df[selected_colums] == df[selected_colums].max() , ] )

    st.text( selected_colums +'컬럼의 히스토그램')

    fig1 = plt.figure()
    df[selected_colums].hist(bins=20)
    st.pyplot(fig1)

    
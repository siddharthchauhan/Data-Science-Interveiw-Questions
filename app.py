import pandas as pd
import streamlit as st

question = ["Data Scientist", "Data Analyst"]
choice = st.sidebar.selectbox("Select your field", question)

if choice == 'Data Scientist':

    df_ds = pd.read_excel('Glassdoor Data Scientist Interview Questions.xlsx')

    df_ds['Date'] = pd.to_datetime(df_ds['Date'])
    df_ds['Year']= df_ds['Date'].dt.year

    company_title = st.sidebar.selectbox('Company Name', sorted(df_ds['Company'].unique()))
    date_asked = st.sidebar.selectbox('Year', df_ds['Year'].unique())
    st.title(company_title)
    st.subheader(date_asked)
    st.table(df_ds[(df_ds["Company"] == company_title) & (df_ds["Year"] == date_asked)])

elif choice == 'Data Analyst':


    df = pd.read_excel('Glassdoor Data Analyst Interview Questions.xlsx')

    df['Date'] = pd.to_datetime(df['Date'])
    df['Year']= df['Date'].dt.year

    company_title = st.sidebar.selectbox('Company Name', sorted(df['Company'].unique()))
    date_asked = st.sidebar.selectbox('Year', sorted(df['Year'].unique()))
    st.title(company_title)
    st.subheader(date_asked)
    st.table(df[(df["Company"] == company_title) & (df["Year"] == date_asked)])

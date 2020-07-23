import pandas as pd
import streamlit as st


def main():

    question = ["Data Scientist", "Data Analyst"]
    choice = st.sidebar.selectbox("Select your field", question)

    if choice == 'Data Scientist':

            df = pd.read_excel('Glassdoor Data Scientist Interview Questions.xlsx')

            company = sorted(df['Company'].unique())
            df['Date'] = pd.to_datetime(df['Date'])
            df['Year']= df['Date'].dt.year
            year = df['Year'].unique()

            if not st.sidebar.checkbox("Close", True):
                company_title = st.sidebar.selectbox('Company Name', company)
                st.title(company_title)

                filter_question = (df['Company'] == company_title)
                st.table(df[filter_question])

            if not st.sidebar.checkbox("Hide", True):
                date_asked = st.sidebar.selectbox('Year', year)
                st.title(date_asked)

                fil_question = (df['Year'] == date_asked)
                st.table(df[fil_question])

    elif choice == 'Data Analyst':

            df = pd.read_excel('Glassdoor Data Analyst Interview Questions.xlsx')
            com = sorted(df['Company'].unique())
            df['Date'] = pd.to_datetime(df['Date'])
            df['Year'] = df['Date'].dt.year
            year = df['Year'].unique()

            if not st.sidebar.checkbox("Close", True):
                comp_title = st.sidebar.selectbox('Company Name', com)
                st.title(comp_title)

                filt_question = (df['Company'] == comp_title)
                st.table(df[filt_question])

            if not st.sidebar.checkbox("Hide", True):
                date_ask = st.sidebar.selectbox('Year', year)
                st.title(date_ask)

                fil_ques = (df['Year'] == date_ask)
                st.table(df[fil_ques])

if __name__ == '__main__':
    main()
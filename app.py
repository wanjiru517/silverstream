
from pkgutil import get_data
from unicodedata import name
from http.cookies import Morsel
from unittest import result
import streamlit as st
import pandas as pd
from pandas import ExcelFile
import plotly as px
#---Main Page---
st.set_page_config(page_title='THE SILVERSTREAM ACADEMY')
st.header('THE SILVERSTREAM ACADEMY')
st.image('st 1.jpeg')

### --- LOAD DATAFRAME
df = pd.read_excel('C:\Users\USER\silver stream\silverstream\KCPE RESULTS.xlsx')
print(df.head())
#Please rename your excel file to KCSE RESULTS.xlsx
df_2018 = pd.read_excel('KCPE RESULTS.xlsx', sheet_name='2018')
df_2019 = pd.read_excel('KCPE RESULTS.xlsx', sheet_name='2019')
df_2020 = pd.read_excel('KCPE RESULTS.xlsx', sheet_name='2020')
df_2021 = pd.read_excel('KCPE RESULTS.xlsx', sheet_name='2021')
# Combining all datasets
pdList = [df_2018, df_2019,  df_2020, df_2021]
all_records = pd.concat(pdList)
     

st.markdown(
    'A simpe school dashboard outputing the school,s results since founding')

st.image('st 2.jpeg')
#----SIDEBAR-----
st.sidebar.header('Filter Here')
#use selectbox to select one option at a time
options = st.sidebar._selectbox("select the sheet:",[2018,2019,2020,2021,'all'])

if options == 2018:
    st.write(df_2018)
elif options == 2019:
    st.write(df_2019)
elif options == 2020:
    st.write(df_2020)
elif options == 2021:
    st.write(df_2021)
else:
    st.write(all_records)           
#---KCSE RESULTS PER YEAR[BAR CHART]----



 

if st.button('more info'):
    st.write('contact 0716731548')


#from lib2to3.pytree import _Resultd
from pkgutil import get_data
from unicodedata import name
from http.cookies import Morsel
from unittest import result
import streamlit as st
import pandas as pd
from pandas import ExcelFile
import plotly as px
import numpy as np
#---Main Page---
st.set_page_config(page_title='THE SILVERSTREAM ACADEMY')
st.header('THE SILVERSTREAM ACADEMY')
st.title('KCPE results analysis')
st.image('st 1.jpeg')

### --- LOAD DATAFRAME

df_2018 = pd.read_excel('KCPE RESULTS.xlsx', sheet_name='2018')
df_2019 = pd.read_excel('KCPE RESULTS.xlsx', sheet_name='2019')
df_2020 = pd.read_excel('KCPE RESULTS.xlsx', sheet_name='2020')
df_2021 = pd.read_excel('KCPE RESULTS.xlsx', sheet_name='2021')
# Combining all datasets
pdList = [df_2018, df_2019,  df_2020, df_2021]
all_records = pd.concat(pdList)   

st.markdown(
    'The dashboard shows KCPE RESULTS as from 2018 to present')

st.write("They are as follows,")
#----SIDEBAR-----
st.sidebar.header('Filter Here')
#use selectbox to select one option at a time
options = st.sidebar.selectbox("select the sheet:",[2018,2019,2020,2021, 'all'])

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
            
# #---CHART----
data = {'KCPE RESULTS.xlsx'}
df = pd.DataFrame(data)

# Read all sheets of the workbook
sheets = pd.read_excel('KCPE RESULTS.xlsx.', sheet_name='2018')
for sheet_name, df in sheets.items():
    df.plot(x='MATH', y='ENG', title=sheet_name)

#--graphs per sheets--
for sheet_name in ("2018", "2019", "2020", "2021"):
    df = sheet[sheet_name]
    df.plot(x={'ENG','KIS','MATH','SCI','SSR'} y='TOTAL', title=sheet_name)
 

if st.button('more info'):
    st.write('contact 0716731548')
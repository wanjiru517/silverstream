
from lib2to3.pytree import _Results
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

df = pd.read_excel (r'C:\Users\USER\silver stream\silverstream\KCPE RESULTS..xlsx')
     
def get_data_from_excel():
    df = pd.read_excel




st.markdown(
    'A simpe school dashboard outputing the school,s results since founding')
st.image('st 2.jpeg')
#----SIDEBAR-----
st.sidebar.header('Filter Here')
ExcelFile = st.sidebar.multiselect(
     "select the sheet:",
              options=df["2018"].unique()
              Options=df["2019"].unique()
              options=df["2020"].unique()
              options=df["2021"].unique()
)
            
#---KCSE RESULTS PER YEAR[BAR CHART]----
result_by_year = (df_selection.groupby(by=["2018"])
)

result_by_year = (df_selection.groupby)


 

if st.button('more info'):
    st.write('contact 0716731548')

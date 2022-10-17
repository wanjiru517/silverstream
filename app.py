
#from lib2to3.pytree import _Resultd
from ast import If
from asyncore import write
from optparse import Values
from os import rename
from pkgutil import get_data
from re import M
from tkinter.font import names
from unicodedata import name
from http.cookies import Morsel
from unittest import result
import streamlit as st
import pandas as pd
from pandas import ExcelFile
import plotly as px
import numpy as np
import matplotlib.pyplot as plp

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
cols = [1, 2, 3, 4, 5, 6, 7]
df = pdList

st.markdown(
    'The dashboard shows KCPE RESULTS as from 2018 to present')
df_2018.head()
st.write("They are as follows,")
#----SIDEBAR-----
st.sidebar.header('Filter Here')
#selectbox to select one option at a time
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
            
# #---RESULTS BY SUBJECT--

options = st.sidebar.selectbox("select the subject:",[1, 2, 3, 4, 5, 6, 7])

if options == 1:
    st.write(1)
elif options == 2:
    st.write(2)
elif options == 3:
    st.write(3)
elif options == 4:
    st.write(4)
elif options == 5:
    st.write(5)
elif options == 6:
    st.write(6)
elif options == 7:
    st.write(7)

#---results per gender---
gender = st.sidebar.multiselect(
    "Select the Gender:",
    options=df["M"].unique(),
    default=df["F"].unique()
)

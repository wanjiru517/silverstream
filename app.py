from ast import keyword
import csv
from curses.ascii import TAB
from unicodedata import name
import matplotlib
from http.cookies import Morsel
from json import load
from logging import makeLogRecord
import streamlit as st
import pandas as pd
import plotly as px
from PIL import Image
st.set_page_config(page_title='THE SILVERSTREAM ACADEMY')
st.header('THE SILVERSTREAM ACADEMY')
st.image('st 1.jpeg')

### --- LOAD DATAFRAME
csv.excel_tab = 'KCPE RESULTS.XLSX' 
csv.excel  = '2018'

df = pd.read_excel(csv.excel_tab,
                   sheet_name=2018)



st.markdown(
    'A simpe school dashboard outputing the school,s results since founding')
st.image('st 2.jpeg')
st.sidebar.write ('KCPE RESULTS')
 # Load exel data from user


locations= {"lat":[-0.467277], 
            "lon":[37.450611]}
df = pd.DataFrame(data=locations)
st.map(df) 
st.title('KCSE RECORDS')

if st.button('more info'):
    st.write('contact 0716731548')

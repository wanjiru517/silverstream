import csv
import matplotlib
from http.cookies import Morsel
from json import load
from logging import makeLogRecord
import streamlit as st
import pandas as pd
st.set_page_config(page_title='THE SILVERSTREAM ACADEMY')
st.title('THE SILVERSTREAM ACADEMY')
st.image('st 1.jpeg')

st.markdown(
    'A simpe school dashboard outputing the school,s results since founding')
st.image('st 2.jpeg')
st.sidebar.write ('KCPE RESULTS')
 # Load exel data from user
sheet1, sheet2, sheet3, sheet4 = None, None, None, None
with pd.ExcelFile("C:\Users\USER\silver stream\silverstream\KCPE RESULTS..xlsx") as reader:
    sheet1 = pd.read_excel(reader, sheet_name='Sheet1')
    sheet2 = pd.read_excel(reader, sheet_name='Sheet2')
    sheet3 = pd.read_excel(reader, sheet_name='Sheet3')
    sheet4 = pd.read_excel(reader, sheet_name='Sheet4')
locations= {"lat":[-0.467277], 
            "lon":[37.450611]}
df = pd.DataFrame(data=locations)
st.map(df) 
st.title('KCSE RECORDS')

if st.button('more info'):
    st.write('contact 0716731548')

from ast import keyword
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

excel_file = 'KCPE RESULTS.xlxs'
keyword = pd.read_excel(excel_file)
locations= {"lat":[-0.467277], 
            "lon":[37.450611]}
df = pd.DataFrame(data=locations)
st.map(df) 
st.title('KCSE RECORDS')

if st.button('more info'):
    st.write('contact 0716731548')

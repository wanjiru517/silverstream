import csv
from http.cookies import Morsel
from json import load
from logging import makeLogRecord
import streamlit as st
import pandas as pd
st.set_page_config(page_title='THE SILVERSTREAM ACADEMY')
st.markdown('THE SILVERSTREAM ACADEMY')
st.image('st 1.jpeg')

st.markdown(
    'A simpe school dashboard outputing the school,s results since founding')
st.image('st 2.jpeg')

locations= {"lat":[-0.467277], 
            "lon":[37.450611]}
df = pd.DataFrame(data=locations)
st.map(df) 
st.title('KCSE RECORDS')

if st.button('more info'):
    st.write('contact 0716731548')
st.sidebar.write ('KCPE RESULTS')
 # Load data from desktop
df= pd.read_excel(r'C:\Users\USER\Desktop\KCPE RESULTS..xlsx')
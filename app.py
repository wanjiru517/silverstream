from http.cookies import Morsel
from logging import makeLogRecord
import streamlit as st
import pandas as pd
st.header('THE SILVERSTREAM ACADEMY')
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
 # Load data from user 

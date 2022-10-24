
#from lib2to3.pytree import _Resultd
from ast import If
from asyncore import write
from cgitb import text
from codecs import getencoder
from logging import info
from optparse import Values
from os import rename
from pkgutil import get_data
from unicodedata import name
from http.cookies import Morsel
from unittest import result
import streamlit as st
import pandas as pd
from pandas import ExcelFile
import plotly as px
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plp

#---Main Page---
st.set_page_config(page_title='THE SILVERSTREAM ACADEMY')
st.header('THE SILVERSTREAM ACADEMY')
st.title('KCPE results analysis')
st.image('st 1.jpeg')
st.write('The aplication shows and outputs the KCPE results of the students from the year 2018 to 2021.')
st.subheader('ABOUT')
st.write('The Silver Stream academy is a private primary school based in Embu, Kenya. It is a sole propreitorship ownership by Mr. Josphat K.Kathumi and family.')
### --- LOAD DATAFRAME

df_2018 = pd.read_excel('KCPE RESULTS.xlsx', sheet_name='2018')
df_2019 = pd.read_excel('KCPE RESULTS.xlsx', sheet_name='2019')
df_2020 = pd.read_excel('KCPE RESULTS.xlsx', sheet_name='2020')
df_2021 = pd.read_excel('KCPE RESULTS.xlsx', sheet_name='2021')


# Combining all datasets
pdList = [df_2018, df_2019,  df_2020, df_2021]
all_records = pd.concat(pdList)   
df = pdList

st.markdown(
    'The dashboard shows KCPE RESULTS as from 2018 to present')

st.write("They are as follows,")
#----SIDEBAR-----
st.sidebar.header('Filter Here')
#selectbox to select one option at a time
options = st.sidebar.selectbox("select the sheet:",[2018,2019,2020,2021, 'all'])

if options == 2018:
    st.write(df_2018)
    st.write('the graph below shows the average number of the students who have sat for the exam based on their gender')

    st.bar_chart(df_2018.GENDER.value_counts())
elif options == 2019:
    st.write(df_2019)
    st.write('the graph below shows the average number of the students who have sat for the exam based on their gender')
    st.bar_chart(df_2019.GENDER.value_counts())
elif options == 2020:
    st.write(df_2020)
    st.write('the graph below shows the average number of the students who have sat for the exam based on their gender')
    st.bar_chart(df_2020.GENDER.value_counts())
elif options == 2021:
    st.write(df_2021)
    st.write('the graph below shows the average number of the students who have sat for the exam based on their gender')
    st.bar_chart(df_2021.GENDER.value_counts())

else:
    st.write(all_records)
    st.bar_chart(all_records.GENDER.value_counts())
            

#--AVERAGE MEAN OF SUBJECTS FOR THE FOUR YEARS--=
st.subheader('The avarege percentage of the subjects over the four years')
data = [['ENG', 64.21], ['KISW', 58.80], ['MATH', 61.528], ['SCI', 59.58], ['SSR', 59.96]]
df = pd.DataFrame(data, columns=['SUBJECT', 'AVERAGE %'])
df

# chart
st.title('comparison of the average results')
subjects = ['ENG', 'KIS', 'MATH', 'SCI', 'SSR']
marks1 = []
for subject in subjects:
    average=df_2018[subject].mean()
    marks1.append(average)
marks2 = []
for subject in subjects:
    average=df_2019[subject].mean()
    marks2.append(average)
marks3 = []
for subject in subjects:
    average=df_2020[subject].mean()
    marks3.append(average)
marks4 = []
for subject in subjects:
    average=df_2021[subject].mean()
    marks4.append(average)
    
zipped = list(zip(marks1, marks2, marks3, marks4))
df = pd.DataFrame(zipped, columns=['2018', '2019', '2020', '2021'])
df = df.T
df.columns= subjects
fig = px.line(df.T)


st.plotly_chart(fig)




import streamlit as st
import pandas as pd

st.title('🤖 Machine Learning App')
st.info('This is app builds a machine learning model!')
st.write('Hello Juan Carlos!')

with st.expander('DATA'):
  st.write('Raw Data')
  df = pd.read_csv('https://raw.githubusercontent.com/JuKpe/data/refs/heads/master/penguins_cleaned.csv')
  df

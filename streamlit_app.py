import streamlit as st
import pandas as pd

st.title('🤖 Machine Learning App')
st.info('This is app builds a machine learning model!')
st.write('Hello Juan Carlos!')

with st.expander('DATA'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/JuKpe/data/refs/heads/master/penguins_cleaned.csv')
  df

  st.write('**X**')
  X = df.drop('species', axis=1)
  X

  st.write('**y**')
  y = df.species
  y

with st.expander('Data visualization')
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')


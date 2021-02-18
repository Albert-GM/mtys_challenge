import pandas as pd
import streamlit as st


df_raw = pd.read_csv('../data/movies.csv')

st.write("""
         
# Predicción de la recaudación de una película

Esta aplicación predice la recaudación de una película según sus
características.      
         """)
         
st.sidebar.header('Características de la Película')





def user_input_features():
    budget = st.sidebar.slider('Presupuesto', 1, 300, 100)
    # genre = st.sidebar.selectbox('Género', 1, 300, 100)

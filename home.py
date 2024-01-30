import streamlit as st
import pandas as pd

def app():
    df = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv').head(10)
    st.markdown( """<h1 style="text-align: center;">ANALYSES DU DATASET DES VOITURES</h1>""", unsafe_allow_html=True,)
    st.write('')
    st.write('Voici les 10 premiers lignes')
    st.dataframe(df, use_container_width=True)
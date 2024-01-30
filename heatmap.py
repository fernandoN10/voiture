import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout='wide')
def app():

        st.write('Heatmap')

        link = 'https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv'
        df = pd.read_csv(link)
        
        
        st.write("")
        st.subheader("Map de correlation") 
        
        with st.sidebar:
            with st.form("filters"):
                st.write("Choisissez la/les regions")
                US = st.checkbox('US')
                Europe = st.checkbox('Europe')
                Japan = st.checkbox('Japan')
                
                submitted = st.form_submit_button("Submit")
                
        if US and Europe and Japan:
            df1 = df
        elif US and Europe:
            df1 = df.loc[df['continent'].str.strip().isin(['US.','Europe.'])]
        elif US and Japan:
            df1 = df.loc[df['continent'].str.strip().isin(['US.','Japan.'])]
        elif Japan and Europe:
            df1 = df.loc[df['continent'].str.strip().isin(['Japan.','Europe.'])]
        elif US:
            df1 = df.loc[df['continent'].str.strip() == 'US.']
        elif Europe:
            df1 = df.loc[df['continent'].str.strip() == 'Europe.']
        elif Japan:
            df1 = df.loc[df['continent'].str.strip() == 'Japan.']
        else:
            st.caption('On attend que vous faites votre choix')
            df1 = df
        
        if submitted:
            # Creation de la matrice de correlation
            matrix_correlation = df1.select_dtypes(include=['number']).corr()
            # Creation du graphique de correlation
            plt.figure(figsize=(8, 5))
            heatmap = sns.heatmap(matrix_correlation, cmap='coolwarm', fmt='.2f')
            st.pyplot(heatmap.figure)
        else:
            # Creation de la matrice de correlation
            matrix_correlation = df.select_dtypes(include=['number']).corr()
            # Creation du graphique de correlation
            plt.figure(figsize=(8, 5))
            heatmap = sns.heatmap(matrix_correlation, cmap='coolwarm', fmt='.2f')
            st.pyplot(heatmap.figure)
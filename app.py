import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('../vehicles_us.csv')
hist_button = st.button('Construir histograma')
st.header('App')
if hist_button:
    st.write('Crea histograma.')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
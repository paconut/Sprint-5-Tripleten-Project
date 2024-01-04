import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('../vehicles_us.csv')
st.header('App')
hist_button = st.checkbox('Construir histograma')
if hist_button:
    st.write('Crea histograma.')
    fig1 = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig1, use_container_width=True)

disp_button = st.checkbox('Construir gráfico de dispersión')
if disp_button:
    st.write('Crea gráfico de dispersión.')
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)
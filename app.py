import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv("vehicles_us.csv")  # leer los datos

st.header('Análisis de datos de anuncios de venta de coches')  # título
st.write(
    'Este es un análisis de datos de anuncios de venta de coches en Estados Unidos.\n\
    El conjunto de datos contiene información sobre los anuncios, incluyendo el precio, el kilometraje y otros detalles del vehículo.')


build_histogram = st.checkbox('Construir un histograma')
if build_histogram:

    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

build_dispersion = st.checkbox('Construir un disgrama de dispersión')
if build_dispersion:
    st.write(
        'Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

import streamlit as st # type: ignore
import pandas as pd
import os

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 2")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

st.header("Solución")

# Cargar el dataset
@st.cache_data
def load_data():
    try:
        data = pd.read_csv('static/dataset/estudiantes_colombia.csv')
        return data
    except FileNotFoundError:
        st.error("Error: No se encontró el archivo estudiantes_colombia.csv en static/dataset/")
        return None

df = load_data()

if df is not None:
    st.title('Explorador de Datos de Estudiantes')

    if st.checkbox('Mostrar primeras 5 filas'):
        st.subheader('Primeras 5 Filas')
        st.dataframe(df.head())

    if st.checkbox('Mostrar últimas 5 filas'):
        st.subheader('Últimas 5 Filas')
        st.dataframe(df.tail())

    if st.checkbox('Mostrar información del dataset'):
        st.subheader('Información del Dataset')
        st.text(df.info())

    if st.checkbox('Mostrar descripción estadística'):
        st.subheader('Descripción Estadística')
        st.dataframe(df.describe())

    columnas_seleccionadas = st.multiselect('Seleccionar columnas:', df.columns)
    if columnas_seleccionadas:
        st.subheader('Columnas Seleccionadas')
        st.dataframe(df[columnas_seleccionadas])

    st.subheader('Filtrar por Promedio')
    min_prom = float(df['promedio'].min())
    max_prom = float(df['promedio'].max())
    promedio_filtrado = st.slider('Promedio mínimo:', min_value=min_prom, max_value=max_prom, value=min_prom)
    df_filtrado = df[df['promedio'] >= promedio_filtrado]
    st.subheader(f'Estudiantes con promedio >= {promedio_filtrado}')
    st.dataframe(df_filtrado)
else:
    st.warning("No se pudieron cargar los datos. Verifica la ubicación del archivo.")
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
code = """@st.cache_data
def load_data():
    file_path = os.path.join('static', 'dataset', 'estudiantes_colombia.csv')
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        st.error(f"Error: No se encontró el archivo en la ruta: {file_path}")
        return None

df = load_data()

if df is not None:
    st.title('Explorador de Datos de Estudiantes Colombianos')
    st.write('Utiliza esta aplicación para explorar el dataset de estudiantes.')"""

st.code(code, language='python')

@st.cache_data
def load_data():
    file_path = os.path.join('static', 'dataset', 'estudiantes_colombia.csv')
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        st.error(f"Error: No se encontró el archivo en la ruta: {file_path}")
        return None

df = load_data()

if df is not None:
    st.title('Explorador de Datos de Estudiantes Colombianos')
    st.write('Utiliza esta aplicación para explorar el dataset de estudiantes.')

    # Mostrar las primeras y últimas filas

    code = '''if st.checkbox('Mostrar las primeras 5 filas'):
        st.subheader('Primeras 5 Filas')
        st.dataframe(df.head())

    if st.checkbox('Mostrar las últimas 5 filas'):
        st.subheader('Últimas 5 Filas')
        st.dataframe(df.tail())'''
    st.code(code, language='python')
    
    if st.checkbox('Mostrar las primeras 5 filas'):
        st.subheader('Primeras 5 Filas')
        st.dataframe(df.head())

    if st.checkbox('Mostrar las últimas 5 filas'):
        st.subheader('Últimas 5 Filas')
        st.dataframe(df.tail())

    # Mostrar información del dataset
    code = """if st.checkbox('Mostrar información del dataset (.info())'):
        st.subheader('Información del Dataset')
        st.text(df.info())"""
    st.code(code, language='python')
    
    if st.checkbox('Mostrar información del dataset (.info())'):
        st.subheader('Información del Dataset')
        st.text(df.info())

    # Mostrar descripción estadística del dataset
    code = """ if st.checkbox('Mostrar descripción estadística del dataset (.describe())'):
        st.subheader('Descripción Estadística del Dataset')
        st.dataframe(df.describe())"""
    st.code(code, language='python')

    if st.checkbox('Mostrar descripción estadística del dataset (.describe())'):
        st.subheader('Descripción Estadística del Dataset')
        st.dataframe(df.describe())

    # Selección de columnas

    code = """st.subheader('Seleccionar Columnas a Mostrar')
    selected_columns = st.multiselect('Selecciona las columnas:', df.columns)

    if selected_columns:
        st.subheader('Columnas Seleccionadas')
        st.dataframe(df[selected_columns])"""
    st.code(code, language='python')

    st.subheader('Seleccionar Columnas a Mostrar')
    selected_columns = st.multiselect('Selecciona las columnas:', df.columns)

    if selected_columns:
        st.subheader('Columnas Seleccionadas')
        st.dataframe(df[selected_columns])

    # Filtrar por promedio

    code = """st.subheader('Filtrar Estudiantes por Promedio')
    min_promedio = float(df['promedio'].min())
    max_promedio = float(df['promedio'].max())
    promedio_filtro = st.slider('Mostrar estudiantes con promedio mayor o igual a:', min_value=min_promedio, max_value=max_promedio, value=min_promedio)

    df_filtrado = df[df['promedio'] >= promedio_filtro]
    st.subheader(f'Estudiantes con promedio mayor o igual a {promedio_filtro}')
    st.dataframe(df_filtrado)
else:
    st.warning("No se pudieron cargar los datos. Verifica la ruta del archivo.")"""
    st.code(code, language='python')

    st.subheader('Filtrar Estudiantes por Promedio')
    min_promedio = float(df['promedio'].min())
    max_promedio = float(df['promedio'].max())
    promedio_filtro = st.slider('Mostrar estudiantes con promedio mayor o igual a:', min_value=min_promedio, max_value=max_promedio, value=min_promedio)

    df_filtrado = df[df['promedio'] >= promedio_filtro]
    st.subheader(f'Estudiantes con promedio mayor o igual a {promedio_filtro}')
    st.dataframe(df_filtrado)
else:
    st.warning("No se pudieron cargar los datos. Verifica la ruta del archivo.")


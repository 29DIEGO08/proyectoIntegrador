import streamlit as st

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 1")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad tiene como objetivo proporcionar una introducción práctica a Python y sus estructuras 
de datos fundamentales. A través de ejercicios guiados, los participantes explorarán conceptos clave 
como variables, tipos de datos, operadores y las estructuras de datos esenciales: listas, tuplas, 
diccionarios y conjuntos. Además, se aprenderá a manipular y visualizar datos utilizando la biblioteca
 Pandas y Streamlit, creando DataFrames desde diversas fuentes y mostrando los resultados de manera interactiva.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Fundamentos de Python:
Comprender y aplicar los tipos de datos básicos de Python.
Utilizar variables y operadores de manera efectiva.
            
- Estructuras de Datos:
Dominar el uso de listas, tuplas, diccionarios y conjuntos.
Seleccionar la estructura de datos adecuada para cada situación.
            
- Manipulación de Datos con Pandas:
Crear DataFrames desde múltiples fuentes: diccionarios, listas, Series, archivos CSV, Excel, JSON, bases de datos SQLite y arrays de NumPy.
Manipular y transformar datos dentro de DataFrames.
            
- Visualización de Datos con Streamlit:
Utilizar Streamlit para mostrar DataFrames de forma interactiva.
Crear aplicaciones web sencillas para visualizar datos.
            
- Aplicación Práctica:
Resolver problemas prácticos utilizando las estructuras de datos y las herramientas aprendidas.
Aprender el manejo de errores al momento de leer archivos externos o bases de datos.
""")

st.header("Solución")

import pandas as pd
import sqlite3
import numpy as np

# Configuración inicial de Streamlit
st.title("Actividad 1 - Creación de DataFrames")
st.write("""
Esta actividad muestra cómo crear DataFrames en Pandas desde diferentes fuentes y visualizarlos en Streamlit.
""")



# 1. Desde diccionario
st.header("1. Desde diccionario")

code = """
libros_dict = {
    "título": ["El Hobbit", "1984", "Cien años de soledad"],
    "autor": ["J.R.R. Tolkien", "George Orwell", "Gabriel García Márquez"],
    "año de publicación": [1937, 1949, 1967],
    "género": ["Fantasía", "Distopía", "Realismo mágico"]
}
df_libros = pd.DataFrame(libros_dict)
st.write("DataFrame de Libros:")
st.dataframe(df_libros)
"""
st.code(code, language="python")

libros_dict = {
    "título": ["El Hobbit", "1984", "Cien años de soledad"],
    "autor": ["J.R.R. Tolkien", "George Orwell", "Gabriel García Márquez"],
    "año de publicación": [1937, 1949, 1967],
    "género": ["Fantasía", "Distopía", "Realismo mágico"]
}
df_libros = pd.DataFrame(libros_dict)
st.write("Resultado de DataFrame de Libros:")
st.dataframe(df_libros)

# 2. Desde lista de diccionarios
st.header("2. Desde lista de diccionarios")

code = """
ciudades = [
    {"nombre": "Madrid", "población": 3300000, "país": "España"},
    {"nombre": "Buenos Aires", "población": 2891000, "país": "Argentina"},
    {"nombre": "Lima", "población": 975000, "país": "Perú"}
]
df_ciudades = pd.DataFrame(ciudades)
st.write("Información de Ciudades:")
st.dataframe(df_ciudades)"""
st.code(code, language="python")

ciudades = [
    {"nombre": "Madrid", "población": 3300000, "país": "España"},
    {"nombre": "Buenos Aires", "población": 2891000, "país": "Argentina"},
    {"nombre": "Lima", "población": 975000, "país": "Perú"}
]
df_ciudades = pd.DataFrame(ciudades)
st.write("Resultado de Información de Ciudades:")
st.dataframe(df_ciudades)

# 3. Desde lista de listas
st.header("3. Desde lista de listas")

code = """productos = [
    ["Laptop", 1200, 15],
    ["Mouse", 25, 50],
    ["Teclado", 50, 30]
]
df_productos = pd.DataFrame(productos, columns=["producto", "precio", "stock"])
st.write("Productos en Inventario:")
st.dataframe(df_productos)"""
st.code(code, language="python")

productos = [
    ["Laptop", 1200, 15],
    ["Mouse", 25, 50],
    ["Teclado", 50, 30]
]
df_productos = pd.DataFrame(productos, columns=["producto", "precio", "stock"])
st.write("Resultado de Productos en Inventario:")
st.dataframe(df_productos)

# 4. Desde Series
st.header("4. Desde Series")

code = """nombres = pd.Series(["Ana", "Juan", "María", "Carlos"])
edades = pd.Series([25, 30, 28, 35])
ciudades_series = pd.Series(["Madrid", "Barcelona", "Valencia", "Sevilla"])
df_personas = pd.DataFrame({
    "nombre": nombres,
    "edad": edades,
    "ciudad": ciudades_series
})
st.write("Datos de Personas:")
st.dataframe(df_personas)"""
st.code(code, language="python")

nombres = pd.Series(["Ana", "Juan", "María", "Carlos"])
edades = pd.Series([25, 30, 28, 35])
ciudades_series = pd.Series(["Madrid", "Barcelona", "Valencia", "Sevilla"])
df_personas = pd.DataFrame({
    "nombre": nombres,
    "edad": edades,
    "ciudad": ciudades_series
})
st.write("Resultado de Datos de Personas:")
st.dataframe(df_personas)

# 5. DataFrame desde un archivo CSV (local)
st.subheader("5. DataFrame desde Archivo CSV (local)")

code = """try:
    df_csv = pd.read_csv("data.csv")
    st.write("Datos desde CSV")
    st.dataframe(df_csv)
except FileNotFoundError:
    st.error("Error")"""
st.code(code, language="python")

try:
    df_csv = pd.read_csv("data.csv")
    st.write("Resultado desde CSV")
    st.dataframe(df_csv)
except FileNotFoundError:
    st.error("Error")

# 6. DataFrame desde un archivo Excel (local)
st.subheader("6. DataFrame desde Archivo Excel (local)")

code = """try:
    df_excel_local = pd.read_excel("data.xlsx")
    st.write("Datos desde Excel")
    st.dataframe(df_excel_local)
except FileNotFoundError:
    st.error("Error")"""
st.code(code, language="python")

try:
    df_excel_local = pd.read_excel("data.xlsx")
    st.write("Resultado desde Excel")
    st.dataframe(df_excel_local)
except FileNotFoundError:
    st.error("Error")


# 7. DataFrame desde un archivo JSON
st.subheader("7. DataFrame desde Archivo JSON")

code = """try:
    df_json = pd.read_json("data.json")
    st.write("Datos de Usuarios desde JSON")
    st.dataframe(df_json)
except FileNotFoundError:
    st.error("Error")"""
st.code(code, language="python")

try:
    df_json = pd.read_json("data.json")
    st.write("Resultado de Usuarios desde JSON")
    st.dataframe(df_json)
except FileNotFoundError:
    st.error("Error")

# 8. Desde URL
st.header("8. Desde URL")

code = """try:
    url = "https://raw.githubusercontent.com/plotly/datasets/master/iris.csv"
    df_url = pd.read_csv(url)
    st.write("Datos desde URL:")
    st.dataframe(df_url)
except Exception as e:
    st.error(f"Error {str(e)}")"""
st.code(code, language="python")

try:
    url = "https://raw.githubusercontent.com/plotly/datasets/master/iris.csv"
    df_url = pd.read_csv(url)
    st.write("Resultado desde URL:")
    st.dataframe(df_url)
except Exception as e:
    st.error(f"Error {str(e)}")

# 9. Desde SQLite
st.header("9. Desde SQLite")

code = """try:
    conn = sqlite3.connect('estudiantes.db')
    cursor = conn.cursor()
    
    # Crear tabla e insertar datos
    cursor.execute('CREATE TABLE IF NOT EXISTS estudiantes (nombre TEXT, calificación INTEGER)')
    cursor.execute('INSERT INTO estudiantes VALUES ("Ana", 85)')
    cursor.execute('INSERT INTO estudiantes VALUES ("Luis", 90)')
    cursor.execute('INSERT INTO estudiantes VALUES ("Marta", 78)')
    conn.commit()
    
    df_sql = pd.read_sql('SELECT * FROM estudiantes', conn)
    st.write("Datos desde SQLite:")
    st.dataframe(df_sql)
    conn.close()
except Exception as e:
    st.error(f"Error {str(e)}")"""
st.code(code, language="python")

try:
    conn = sqlite3.connect('estudiantes.db')
    cursor = conn.cursor()
    
    # Crear tabla e insertar datos
    cursor.execute('CREATE TABLE IF NOT EXISTS estudiantes (nombre TEXT, calificación INTEGER)')
    cursor.execute('INSERT INTO estudiantes VALUES ("Ana", 85)')
    cursor.execute('INSERT INTO estudiantes VALUES ("Luis", 90)')
    cursor.execute('INSERT INTO estudiantes VALUES ("Marta", 78)')
    conn.commit()
    
    df_sql = pd.read_sql('SELECT * FROM estudiantes', conn)
    st.write("Resultado desde SQLite:")
    st.dataframe(df_sql)
    conn.close()
except Exception as e:
    st.error(f"Error {str(e)}")

# 10. Desde NumPy
st.header("10. Desde NumPy")

code = """try:
    data = np.array([
        [1, 'A', 100],
        [2, 'B', 200],
        [3, 'C', 300]
    ])
    df_numpy = pd.DataFrame(data, columns=['ID', 'Letra', 'Valor'])
    st.write("Datos desde NumPy:")
    st.dataframe(df_numpy)
except Exception as e:
    st.error(f"Error {str(e)}")"""
st.code(code, language="python")

try:
    data = np.array([
        [1, 'A', 100],
        [2, 'B', 200],
        [3, 'C', 300]
    ])
    df_numpy = pd.DataFrame(data, columns=['ID', 'Letra', 'Valor'])
    st.write("Resultado desde NumPy:")
    st.dataframe(df_numpy)
except Exception as e:
    st.error(f"Error {str(e)}")



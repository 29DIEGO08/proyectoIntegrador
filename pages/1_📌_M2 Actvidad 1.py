import streamlit as st

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 1")

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
st.write("DataFrame de Libros:")
st.dataframe(df_libros)

# 2. Desde lista de diccionarios
st.header("2. Desde lista de diccionarios")
ciudades = [
    {"nombre": "Madrid", "población": 3300000, "país": "España"},
    {"nombre": "Buenos Aires", "población": 2891000, "país": "Argentina"},
    {"nombre": "Lima", "población": 975000, "país": "Perú"}
]
df_ciudades = pd.DataFrame(ciudades)
st.write("Información de Ciudades:")
st.dataframe(df_ciudades)

# 3. Desde lista de listas
st.header("3. Desde lista de listas")
productos = [
    ["Laptop", 1200, 15],
    ["Mouse", 25, 50],
    ["Teclado", 50, 30]
]
df_productos = pd.DataFrame(productos, columns=["producto", "precio", "stock"])
st.write("Productos en Inventario:")
st.dataframe(df_productos)

# 4. Desde Series
st.header("4. Desde Series")
nombres = pd.Series(["Ana", "Juan", "María", "Carlos"])
edades = pd.Series([25, 30, 28, 35])
ciudades_series = pd.Series(["Madrid", "Barcelona", "Valencia", "Sevilla"])
df_personas = pd.DataFrame({
    "nombre": nombres,
    "edad": edades,
    "ciudad": ciudades_series
})
st.write("Datos de Personas:")
st.dataframe(df_personas)

# 5. DataFrame desde un archivo CSV (local)
st.subheader("5. DataFrame desde Archivo CSV (local)")
try:
    df_csv = pd.read_csv("data.csv")
    st.write("Datos desde CSV")
    st.dataframe(df_csv)
except FileNotFoundError:
    st.error("El archivo data.csv no se encontró. Asegúrate de crearlo en la misma carpeta que el script.")

# 6. DataFrame desde un archivo Excel (local)
st.subheader("6. DataFrame desde Archivo Excel (local)")
try:
    df_excel_local = pd.read_excel("data.xlsx")
    st.write("Datos desde Excel")
    st.dataframe(df_excel_local)
except FileNotFoundError:
    st.error("El archivo data.xlsx no se encontró. Asegúrate de crearlo en la misma carpeta que el script.")
except ImportError:
    st.warning("La biblioteca 'openpyxl' no está instalada. Intenta pip install openpyxl en tu terminal.")

# 7. DataFrame desde un archivo JSON
st.subheader("7. DataFrame desde Archivo JSON")
try:
    df_json = pd.read_json("data.json")
    st.write("Datos de Usuarios desde JSON")
    st.dataframe(df_json)
except FileNotFoundError:
    st.error("El archivo data.json no se encontró. Asegúrate de crearlo en la misma carpeta que el script.")

# 8. Desde URL
st.header("8. Desde URL")
try:
    url = "https://raw.githubusercontent.com/plotly/datasets/master/iris.csv"
    df_url = pd.read_csv(url)
    st.write("Datos desde URL:")
    st.dataframe(df_url)
except Exception as e:
    st.error(f"Error al cargar datos desde URL: {str(e)}")

# 9. Desde SQLite
st.header("9. Desde SQLite")
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
    st.write("Datos desde SQLite:")
    st.dataframe(df_sql)
    conn.close()
except Exception as e:
    st.error(f"Error con SQLite: {str(e)}")

# 10. Desde NumPy
st.header("10. Desde NumPy")
try:
    data = np.array([
        [1, 'A', 100],
        [2, 'B', 200],
        [3, 'C', 300]
    ])
    df_numpy = pd.DataFrame(data, columns=['ID', 'Letra', 'Valor'])
    st.write("Datos desde NumPy:")
    st.dataframe(df_numpy)
except Exception as e:
    st.error(f"Error con NumPy: {str(e)}")


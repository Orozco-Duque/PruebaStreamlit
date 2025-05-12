import streamlit as st
import joblib
import numpy as np

# Cargar el modelo entrenado
modelo = joblib.load('modelo_iris.pkl')

# Título de la aplicación
st.title("Clasificación de Flores Iris 🌸")
st.write("Ingrese las características de la flor para predecir el tipo de Iris")

# Entradas del usuario
sepal_length = st.number_input("Longitud del sépalo (cm)", min_value=0.0, max_value=10.0, value=5.1)
sepal_width = st.number_input("Ancho del sépalo (cm)", min_value=0.0, max_value=10.0, value=3.5)
petal_length = st.number_input("Longitud del pétalo (cm)", min_value=0.0, max_value=10.0, value=1.4)
petal_width = st.number_input("Ancho del pétalo (cm)", min_value=0.0, max_value=10.0, value=0.2)

# Predicción
if st.button("Predecir"):
    # Crear un array con las características ingresadas
    entrada = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    # Realizar la predicción
    prediccion = modelo.predict(entrada)[0]
    clases = ['Setosa', 'Versicolor', 'Virginica']
    resultado = clases[prediccion]

    # Mostrar resultado
    st.success(f"🌼 La flor es de tipo: **{resultado}**")
import streamlit as st

st.title("Convertidor a Mayúsculas")

# Caja de texto de entrada
texto_entrada = st.text_input("Escribe tu texto aquí:", "")

# Procesar texto y ponerlo en mayúsculas
texto_mayusculas = texto_entrada.upper()

# Mostrar el resultado en otra caja de texto (deshabilitada para que sea de solo lectura)
st.text_input("Texto procesado (Mayúsculas):", value=texto_mayusculas, disabled=True)

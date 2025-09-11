import streamlit as st
import time

st.title("TABUADA")

# Entrada do usuário
numero = st.number_input("Digite um número para ver a tabuada:", step=1, value=1)

# Mostrar a tabuada
st.write(f"### Tabuada do {numero}")
for i in range(1, 11):
    st.write(f"{numero} x {i} = {numero * i}")
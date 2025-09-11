# escrever um algoritimo que mostra os numeros pares entre 100 e 200

import streamlit as st
import time
st.title("atividade: 1")
st.header("laços de repetição: for")

numero= st.number_input("diigte um numero: ",step=1)

st.button("iniciar")
for i in range(100,121, 2):
    st.info(i)
    time.slleep(1)
    




#Escrever um programa de computador que solicite do usuário 4 notas e, ao final, apresente a média.

import streamlit as st

st.title("logica de programaçao")
st.header("laço de repetiçao")

soma=0

for i in range(4):
    nota=st.number_input(f"diigte a {i+1}ª nota: ")
    soma=soma+soma

media = soma / 4

if st.button("mostrar resultado"):
    st.info(f"media: {media}")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
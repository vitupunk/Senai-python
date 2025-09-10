# verique a idade de uma pessoa.
# se menor que 18, mostre: menor de idade
# caso comtrario, mostre: maior de idade
# usando streamlit

import streamlit as st

st.title("verificando a idade")
idade = st.number_input("digite sua idade")

if st.button("verificar"):
    if idade < 18:
        st.write("menor de idade")
    else:
        st.write("maior de idade")


else:
    st.write("por favor, digite  idade")


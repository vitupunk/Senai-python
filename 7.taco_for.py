import streamlit as st
import time
st.title("laço de repetiçao - for")

st.header("contagem de 1 a 10")

numero = st.number_input("digite um numero: ", step=1)

if st.button("iniciar"):

    for i in range(1,11):
        st.write(i)
        time.sleep(1)
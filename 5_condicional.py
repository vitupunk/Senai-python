# vericando a media
# solicite ao usuario a media do aluno
# se maior ou igual a 7, mostre como aprovado
# caso contrario, mostre como reprovado

import streamlit as st

st.title("verifique media")

media = st.number_input("digite a media")
if st.button("verificar"):
    if media >= 7:
        st.success("aprovado")
    else:
        st.error("reprovado")
else:
    st.warning("informe a media")

#success - verde
#warning - amarelo
#info - azul
#error - vermelho

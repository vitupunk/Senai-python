#Escrever um programa de computador que solicite do usuário 3 notas e, ao final, apresente a média e mostre para o usuário se o aluno está aprovado, em recuperação ou reprovado. 
#Considere que para aprovação, deve-se obter média maior ou igual a 7, para ser reprovado, a média deve ser menor que 4.

import streamlit as st 

st.title("logica de rpogramaçao")
st.header("laço de repetiçao")

quantidade_notas=3
soma=0

for i in range(quantidade_notas):
    nota=st.number_input(f"digite a {i+1}ª nota: ")
    soma=soma+nota

media=soma/quantidade_notas

if st.button("mostrar resultado"):
    st.info(f"media:{media:.1f}")
    if media>=7:
        st.success(f"aprovado")
    elif media>=4:
        st.warning(f"recuperaçao")
    else:
        st.error(f"reprovado")    
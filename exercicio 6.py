#Escreva um algoritmo que solicite ao usuário 5 valores
#inteiros e ao final mostre: 
#quantos números são pares; 
#quantos números são ímpares;

import streamlit as st 

st.title("contador de pares e impares")

pares=0
impares=0
numeros=[]

for i in range(1,6):
    num=st.number_input(f"digite o {i} numero inteiro: ",step=1,key=f"num{i}")
    numeros.append(num)

if st.button("calcular"):
    pares=sum(1 for n in numeros if n %2==0)
    impares=sum(1 for n in numeros if n %2!=0)

st.info(f"quantos numeros sao pares: {pares}")
st.info(f"quantos numeros sao impares: {impares}")
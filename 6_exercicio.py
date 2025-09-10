import streamlit as st

st.title("verificando media,soma,produto,menor valor,maior valor")

n1 = st.number_input("digite um numero")
n2 = st.number_input("digite outro numero")

soma = n1 + n2
produto = n1 * n2

media = (n1+n2)/2
maior = max(n1, n2)
menor = min (n1, n2)

if st.button("verificar"):
    if n1 and n2:
        st.write(f"soma: {soma}")
        st.write(f"produto: {produto}")
        st.write(f"media: {media}")
        st.write(f"maior: {maior} ")
        st.write(f"menor: {menor}")

else:
    st.info("informe os numeros.")
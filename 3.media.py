import os 
os.system("cls")

#criando um vetor(lista)
lista_notas=[]

#constante
quantidade_notas=3

#inserindo notas
for i in range(3):
    nota=int(input(f"digite a {i+1}ª nota: "))
    soma+= nota

#mostrar notas

print(f"nota:  {nota}")
print(f"soma: {soma}")

print("fim")

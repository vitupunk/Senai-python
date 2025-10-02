import os
os.system("cls")

pares=0
impares=0
lista_numeros=[]

for i in range(6):
    numero=int(input(f"insira o numero: "))
    if numero %2==0:
        pares +=1
    else:
        impares +=1

print(f"quantidade de numero pares: {pares}")
print(f"quantidade de numero impares: {impares}")
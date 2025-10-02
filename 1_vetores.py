import os
os.system("cls")

#criando um vetor.
vetor_de_notas=[]

print("solicitando 3 notas.")
for i in range(3):
    nota=float(input("digite uma nota: "))
    #inserindo uma nota na vetor de notas.
    vetor_de_notas.append(nota)

print("\nmostrando todas as notas.")
for i in range(3):
    #o valor  da variavel i começa com zero
    #o valor de i no vetor faz mostrar o indice no vetor
    print(f"nota:{vetor_de_notas[i]}")

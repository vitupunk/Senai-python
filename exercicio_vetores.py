# Exercício: Armazenar 5 números em um vetor, substituindo valores negativos por 0 e listando o vetor

vetor = []

for i in range(5):
    valor = int(input(f"Digite o número {i+1}: "))
    if valor < 0:
        valor = 0
    vetor.append(valor)

print("Valores do vetor:", vetor) 
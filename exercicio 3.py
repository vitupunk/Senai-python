# Crie um programa que leia 5 números, armazenando em um vetor e informe qual é o menor número e o maior.
# Mostre os números informados pelo usuário.

numeros = []

for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

print("Números informados:", numeros)
print("Menor número:", min(numeros))
print("Maior número:", max(numeros))
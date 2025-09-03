import os
os.system("cls")

def mostrar_mes(numero):
    match numero:
        case 1:
            print("Janeiro")
        case 2:
            print("Fevereiro")
        case 3:
            print("Março")
        case 4:
            print("Abril")
        case 5:
            print("Maio")
        case 6:
            print("Junho")
        case 7:
            print("Julho")
        case 8:
            print("Agosto")
        case 9:
            print("Setembro")
        case 10:
            print("Outubro")
        case 11:
            print("Novembro")
        case 12:
            print("Dezembro")
        case _:
            print("Número inválido! Digite um número de 1 a 12.")

try:
    numero = int(input("Digite o número do mês (1-12): "))
    mostrar_mes(numero)
except ValueError:
    print("Entrada inválida! Por favor, digite um número inteiro.")

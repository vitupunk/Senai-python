import os
os.system("cls")

def verificar_dia(dia):
    match dia:
        case 1:
            print("Domingo - Final de semana")
        case 7:
            print("Sábado - Final de semana")
        case 2 | 3 | 4 | 5 | 6:
            print("Dia útil")
        case _:
            print("Dia inválido")

# Solicita entrada do usuário
try:
    dia = int(input("Digite um número de 1 a 7 representando o dia da semana (Domingo=1, Sábado=7): "))
    verificar_dia(dia)
except ValueError:
    print("Entrada inválida! Por favor, digite um número inteiro.")

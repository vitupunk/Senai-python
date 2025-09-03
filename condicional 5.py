import os
os.system("cls")

def calcular_pagamento(valor, forma_pagamento):
    match forma_pagamento:
        case 1:  # Pagamento à vista
            desconto = valor * 0.10
            total = valor - desconto
            print(f"Valor do produto: R$ {valor:.2f}")
            print("Forma de pagamento: à vista")
            print(f"Valor do desconto: R$ {desconto:.2f}")
            print(f"Total a pagar: R$ {total:.2f}")

        case 2:  # Pagamento à prazo
            print(f"Valor do produto: R$ {valor:.2f}")
            print("Forma de pagamento: à prazo")
            while True:
                try:
                    parcelas = int(input("Digite a quantidade de parcelas (até 6): "))
                    if 1 <= parcelas <= 6:
                        valor_parcela = valor / parcelas
                        print(f"Quantidade de parcelas: {parcelas}")
                        print(f"Valor por parcela: R$ {valor_parcela:.2f}")
                        print(f"Total à prazo: R$ {valor:.2f}")
                        break
                    else:
                        print("Número inválido. Pode parcelar de 1 até 6 vezes.")
                except ValueError:
                    print("Entrada inválida! Digite um número inteiro.")
        case _:
            print("Forma de pagamento inválida. Digite 1 para à vista ou 2 para à prazo.")

try:
    valor_produto = float(input("Informe o valor do produto: R$ "))
    forma = int(input("Informe a forma de pagamento (1 - à vista, 2 - à prazo): "))
    calcular_pagamento(valor_produto, forma)
except ValueError:
    print("Entrada inválida! Digite um valor numérico para o produto e um número inteiro para a forma de pagamento.")

import os
os.system("cls")

import math

# Solicita o valor do produto
valor_produto = float(input("Informe o valor do produto: R$ "))

# Solicita a forma de pagamento
print("Forma de pagamento:")
print("1 - Pagamento à vista")
print("2 - Pagamento à prazo")
forma_pagamento = int(input("Escolha a forma de pagamento (1 ou 2): "))

match forma_pagamento:
    case 1:
        # Pagamento à vista com desconto de 10%
        desconto = valor_produto * 0.10
        total = valor_produto - desconto
        
        print(f"\nValor do produto: R$ {valor_produto:.2f}")
        print("Forma de pagamento: à vista")
        print(f"Valor do desconto: R$ {desconto:.2f}")
        print(f"Total a pagar: R$ {total:.2f}")
        
    case 2:
        # Pagamento a prazo, pede quantidade de parcelas (até 6)
        parcelas = int(input("Quantidade de parcelas (até 6): "))
        if parcelas < 1 or parcelas > 6:
            print("Quantidade de parcelas inválida. Deve ser entre 1 e 6.")
        else:
            valor_parcela = valor_produto / parcelas
            
            # round

            
            valor_parcela = round(valor_parcela, 2)
            
            print(f"\nValor do produto: R$ {valor_produto:.2f}")
            print("Forma de pagamento: à prazo")
            print(f"Quantidade de parcelas: {parcelas}")
            print(f"Valor por parcela: R$ {valor_parcela:.2f}")
            print(f"Total à prazo: R$ {valor_produto:.2f}")
            
    case _:
        print("Forma de pagamento inválida. Escolha 1 ou 2.")

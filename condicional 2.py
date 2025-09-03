import os
os.system("cls")

print("=== Cardapio do Restaurante ===")
print("1 - Picanha          - R$ 25,00")
print("2 - Lasanha          - R$ 20,00")
print("3 - Strogonoff          - R$ 18,00")
print("4 - Bife acebolado          - R$ 15,00")
print("5 - Pão com ovo          - R$ 5,00")

codigo = int(input("digite o codigo do prato desejado "))

match codigo:
    case 1:
        print("voce escolheu: Picanha - R$ 25,00")
    case 2:
        print("voce escolheu: Lasanha - R$ 20,00")
    case 3:
        print("voce escolheu: Strogonoff - R$ 18,00")
    case 4:
        print("voce escolheu: Bife Acebolado - R$ 15,00")
    case 5:
        print("voce escolheu: Pao com Ovo - 5,00")
    case _:
        print("Codigo Invalido! Tente Novamente")
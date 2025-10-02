import os
os.system("cls")

menu = {
    1: {"nome": "Picanha", "valor": 25.00},
    2: {"nome": "Lasanha", "valor": 20.00},
    3: {"nome": "Strogonoff", "valor": 18.00},
    4: {"nome": "Bife Acebolado", "valor": 15.00},
    5: {"nome": "Pão com ovo", "valor": 5.00}
}

pedidos = []

print("Cardápio:")
for codigo, item in menu.items():
    print(f"{codigo} - {item['nome']} - R$ {item['valor']:.2f}")

while True:
    try:
        escolha = int(input("Escolha o código do prato desejado: "))
        if escolha in menu:
            pedidos.append(menu[escolha])
            continuar = input("Deseja escolher outro prato? (s/n): ").lower()
            if continuar != 's':
                break
        else:
            print("Código inválido. Tente novamente.")
    except ValueError:
        print("Por favor, digite um número válido.")

print("\nPratos escolhidos:")
total = 0
for pedido in pedidos:
    print(f"- {pedido['nome']} - R$ {pedido['valor']:.2f}")
    total += pedido['valor']

print(f"\nTotal da conta: R$ {total:.2f}")
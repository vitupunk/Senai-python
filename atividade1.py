import os
os.system("cls")


soma = 0
contador = 0
continuar = "S"


while continuar == "S":
    nota_texto = input("Digite uma nota: ")

   
    if nota_texto.replace('.', '', 1).isdigit():
        nota = float(nota_texto)
        soma += nota
        contador += 1
    else:
        print("Nota inválida. Digite apenas números.")
        continue  

    continuar = input("Deseja inserir mais uma nota? (S para sim / N para não): ").strip().upper()


if contador > 0:
    media = soma / contador
    print(f"\nVocê inseriu {contador} notas.")
    print(f"Média aritmética: {media:.2f}")
else:
    print("Nenhuma nota foi inserida.")
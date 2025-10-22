import os
os.system("cls")

def ler_nota(numero):
    """
    Lê uma nota do usuário, aceita vírgula ou ponto como separador decimal,
    e garante que esteja no intervalo [0, 10].
    """
    while True:
        entrada = input(f"Informe a nota {numero} (0-10): ").strip()
        entrada = entrada.replace(",", ".")
        try:
            nota = float(entrada)
        except ValueError:
            print("Entrada inválida. Digite um número (ex: 7.5).")
            continue
        if 0 <= nota <= 10:
            return nota
        print("Nota fora do intervalo. A nota deve ser entre 0 e 10.")

def calcular_media(n1, n2):
    return (n1 + n2) / 2

def verificar_aprovacao(media, limite=7.0):
    return "APROVADO" if media >= limite else "REPROVADO"

def main():
    print("Leitura de 2 notas do aluno:")
    nota1 = ler_nota(1)
    nota2 = ler_nota(2)

    media = calcular_media(nota1, nota2)
    situacao = verificar_aprovacao(media)

    print("\nResultado:")
    print(f"Nota 1: {nota1:.2f}")
    print(f"Nota 2: {nota2:.2f}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")

if __name__ == "__main__":
    main()
import os
import time
from dataclasses import dataclass
os.system("cls || clear") # Limpa o terminal em Windows e Linux.


lista_clientes = []


@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str




    #Metodo para mostrar as informaçoes dos clientes.
    #Metodo e o nome dado a uma funçao que  pertence a classe.
    def mostrar_dados(self):
        print(f"nome: {self.nome} \nE-mail: {self.email}\nTelefone: {self.telefone}")






# Função para verificar se a lista esta vazia.
def lista_esta_vazia(lista_clientes):
    if not lista_clientes:
        print("\nNão ha clientes cadastrados.")
        return True
    return False


def adicionar_cliente(lista_cliente):
    print("\n--- Adiconar novo cliente ---")
    nome = input("digite seu nome:")
    email = input("digite seu e-mail: ")
    telefone = input("digite seu telefone: ")

    novo_cliente = Cliente(nome=nome, email=email, telefone=telefone)
    lista_cliente.append(novo_cliente)
    print(f"\nCliente{nome} adiconado com sucesso!")


# Função para encontrar um cliente na lista
def encontrar_cliente_por_nome(lista_clientes, nome_buscar):
    nome_buscar_lower = input("digite o nome do cliente: ")
    for cliente in lista_clientes:
        if cliente.nome.lower() == nome_buscar_lower:
            return cliente
    return None #None significa retornar vazio , sem conteudo.


# Função para mostrar  todos os clientes.
def mostrar_todos_clientes(lista_clientes):
    if lista_esta_vazia(lista_clientes):
        return
    print("\n-- Lista de clientes ---")
    for cliente in lista_clientes:
        cliente.mostrar_dados()


#função para atualizar clientes.
def atualizar_clientes(lista_clientes):
    if lista_esta_vazia(lista_clientes):
        return
    


    #mostrar a lista para ajudar o usuario.
    mostrar_todos_clientes(lista_clientes)
    print("--- Atualizar dados do cliente ---")
    nome_buscar = input("\nDigite o nome do cliente: ")
    cliente_para_atualizar = encontrar_cliente_por_nome(lista_clientes, nome_buscar)


    if cliente_para_atualizar:
        print("\nPessoa encontrada.")
        print("\nDigite os novos dados ou deixe em branco para manter o valor atual. ")

        print(f"\nNome atual:{cliente_para_atualizar.nome}")
        novo_nome = input("Novo nome: ")
        
        
        print(f"\nEmail atual: {cliente_para_atualizar.email}")
        novo_email = input("Novo email: ")
        
        print(f"\nTelefone atual: {cliente_para_atualizar.telefone}")
        novo_telefone = input("Novo telefone: ")

        if novo_nome:
            cliente_para_atualizar.nome = novo_nome
        if novo_email:
            cliente_para_atualizar.email = novo_email
        if novo_telefone:
            cliente_para_atualizar.telefone = novo_telefone

        print(f"\nDados do cliente: {nome_buscar} atualizados com sucesso!")

    else:
        print(f"\nCliente com nome:{nome_buscar} não encontrado.") 


#Função para excluir um cliente.

def execluir_cliente(lista_cliente):
    if lista_esta_vazia (lista_clientes):
        return
    
    mostrar_todos_clientes(lista_clientes)

    nome_buscar = input("\nDigite o nome do cliente que deseja excluir: ")
    clien_para_remover = encontrar_cliente_por_nome(lista_clientes, nome_buscar)

    if clien_para_remover:
        lista_clientes.remove(clien_para_remover)
        print(f"\nCliente {clien_para_remover.nome} excluido com sucesso!")

    else:
        print(f"\nCliente com nome {nome_buscar} não encontrado.") 



# Mostrando menu.
while True:
    print("""
--- Gerenciador de Clientes --- 
1 - Adicionar
2 - Mostrar todos
3 - Atualizar
4 - Excluir
0 - Sair                          
     

               """)
    
    #envitando erros no programa.
    #caso o usuario digite letras.
    try:
        opcao = int(input("digite uma das opcoes acima: "))
    except ValueError:
        print("\nEntrada invalida. digite um numero...")
        time.sleep(2)
        os.system("cls ||clear")
        continue    

    opcao = int(input("digite uma das opçoes acime: "))

    match opcao:
        case 1:
            adicionar_cliente(lista_clientes)
        case 2:
            mostrar_todos_clientes(lista_clientes) 
        case 3:
            atualizar_clientes(lista_clientes)
        case 4:
            execluir_cliente(lista_clientes)
        case 0:
            print("\nSaindo do programa...")
            break
        case _:
            print("\nOpção invalida. \nTente novamente.")


    # Pausa antes de Mudar o menu.
    if opcao != 1 and opcao != 0:
        time.sleep(4)
    elif opcao == 1:
        time.sleep(1)


    #limpa tela
    if opcao != 0:
        os.system("cls || clear")



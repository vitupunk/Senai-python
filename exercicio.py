import os
os.system("cls")

from dataclasses import dataclass
@dataclass

class Pessoa:
    nome: str
    data_de_nascimento: str
    rg: str
    cpf: str
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Data de Nascimento: {self.data_de_nascimento}")
        print(f"RG: {self.rg}")
        print(f"CPF: {self.cpf}")
lista_pessoas = []
QUANTIDADE_DE_PESSOAS = 5

for i in range(QUANTIDADE_DE_PESSOAS):
    print(f"\nCadastro da pessoa {i + 1}:")
    nome = input("Digite o nome: ")
    data_de_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
    rg = input("Digite o RG: ")
    cpf = input("Digite o CPF: ")
    lista_pessoas.append(Pessoa)
    


    
    
    
    

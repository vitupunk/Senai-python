from dataclasses import dataclass

#estrutura de dados:classe
@dataclass
class pessoa:
    nome: str
    idade: int

@dataclass
class pet:
    nome:str
    idade:int

# exemplo de uso da classe
pessoa1 = pessoa("marta")
pet1 = pet("toto", 4)

print("exibindo dados da pessoa.")
print(f"nome: {pessoa1.nome}\nidade: {pessoa1.idade}\n")

print("exibindo dados do pet.")
print(f"nome: {pet1.nome}\nidade: {pet1.idade}")

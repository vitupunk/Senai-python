import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class Endereco:
    logradouro: str
    numero: int
    cidade: str

@dataclass
class cliente:
    nome: str
    endereço: Endereco

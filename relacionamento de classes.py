class Autor:
    def __init__(self, nome: str, biografia: str):
        self.nome = nome
        self.biografia = biografia

    def __repr__(self):
        return f"Autor(nome={self.nome!r})"


class Livro:
    def __init__(self, titulo: str, ano: int, autor: Autor):
        self.titulo = titulo
        self.ano = int(ano)
        self.autor = autor

    def exibir_detalhes(self):
        print(f"Título: {self.titulo}")
        print(f"Ano: {self.ano}")
        print(f"Autor: {self.autor.nome}")


# Exemplo de uso:
if __name__ == "__main__":
    autor = Autor("Clarice Lispector", "Escritora brasileira conhecida por prosa introspectiva.")
    livro = Livro("A Hora da Estrela", 1977, autor)

    livro.exibir_detalhes()
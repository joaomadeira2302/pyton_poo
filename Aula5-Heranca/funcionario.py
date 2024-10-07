class Pessoa:
    def __init__(self, nome, cargo):
        self._nome = nome
        self._cargo = cargo

    def informacoes(self):
        print(f"Olá {self._nome}, na empresa, seu cargo é: {self._cargo}")

class Engenheiro(Pessoa):
    def mostraDetalhes(self):
        print(f"Olá, eu sou {self._nome} e sou um engenheiro")

class Secretario(Pessoa):
    def relatorio(self):
        print(f"Relatório do secretário {self._nome}. Cargo: {self._cargo}")

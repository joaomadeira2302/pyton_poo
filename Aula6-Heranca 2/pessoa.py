class Pessoa:# superclsse ou classe mãe
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def info(self):
        print(f"Nome: {self._nome}. Idade: {self._idade}")

# Classe filha 1 _ Aluno
class Aluno(Pessoa):
    def __init__(self, nome, idade, serie):
        super().__init__(nome, idade) #Utilizando o construtor d4a classe mãe 
        self._serie = serie # Estamos utilizando utlizando um atributo exclusivo da classe filha
    def estudar(self):
      print(f"O aluno {self._nome} está estudando na série {self._serie}.")

# Classe filha 2 - Professor
class Profesor(Pessoa):
    pass 
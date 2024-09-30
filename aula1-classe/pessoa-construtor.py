class Pessoa:
    #Criando o método construtor
    def __init__(self, nome, hobby, endereco):
        # Estamos criando os atributos pa classe utilizando o método construtor. Nesse caso precisamos passar os parâmetros que serão usados como valores dos atributos
        self.nome = nome
        self.hobby = hobby
        self.endereco = endereco  

    # Criando od métodos normais
    def exibirDados(self):
        print(f"Olá {self.nome} seu hobby é {self.hobby}, e seu endereço é {self.endereco}")


# Criando os objetos
pessoa1 = Pessoa("Geraldo","Corredor","Rua 10 Cohab")
pessoa1.exibirDados() # Chamando o método da classe

pessoa2 = Pessoa("Karla", "Artes Maciais", "Av 12, Renascença")
print(pessoa2.nome)


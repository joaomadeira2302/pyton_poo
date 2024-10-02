class Funcionario:
    def __init__(self, cargo, salario=2000):
        self.__cargo = cargo
        self.__salario = salario # Esse atributo está opicional, caso não seja informado outro valor será atribuido o valor padrão de R$ 2000
    
    def getCargo(self):
        return self.__cargo
    
    def setCargo(self, novoCargo):
        self.__cargo = novoCargo

#IREMOS UTILIZAR UMA ÚNICA FORMA DO PYTHON PARA ACESSAR ATRIBUTOS PRIVADOS 
    #Criando o 'get' do salário 
    @property #Esse elementoirá criar o get' mais amigável'
    def salario(self):
        return self.__salario
    
    @salario.setter #Irá criar um set para o salário 'mais amigável'
    def salario(self, valor):
        self.__salario = valor
        if valor <= 0:
            print("Informe um valor positivo")
        else:
            self.__salario = valor
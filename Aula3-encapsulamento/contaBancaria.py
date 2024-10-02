class Conta:
    #Método Construtor
    def __init__(self, numero, titular, saldo, limite = 200):
        #Quando colocamos 2 underlines antes do nome do atributo, indicamos que esse atributo está com a visibilidade "privado", o contrário significa que está "público".
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite 

    #Criando os  demais métodos 
    def detalhes(self):
        print(f"Olá {self.titular} seu saldo atual é {self.saldo}")

    def getLimite(self):
        return self.__limite
    
    def setLimite(self, valor):
        if valor < 0:
            print("Informe um valor positivo para o limite")
        else:
            self._limite = valor 
 


# Criando método para depositar valor
def depositar(self,valor):
    if valor < 0:
        print("Informe um valor maior que zero")
    else:
        self._saldo = self._saldo + valor 

#Criar método para sacar valor 
def sacae(self, valor):
    if self._saldo <=0 or valor > self._saldo:
        print("Saldo insuficiente")
    else:
        self._saldo = self._saldo - valor 
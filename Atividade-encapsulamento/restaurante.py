class Servico:
    def __init__(self, pedido):
        self.__pedido = pedido   

    def novoPedido(self):
        self.__pedido += 1
        print(f"Novo pedido registrado. Total de pedidos: {self.__pedido}")

    def cancelarPedido(self):
        if self.__pedido > 0:
            self.__pedido -= 1
            print(f"Pedido cancelado. Total de pedidos: {self.__pedido}")
        else:
            print("Não há pedidos para cancelar.")

    def exibirPedido(self):
        return (f"Total de pedidos realizados: {self.__pedido}")
 
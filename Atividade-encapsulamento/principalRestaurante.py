from restaurante import Servico

def main():
    sistema_pedidos = Servico(20)

    
    sistema_pedidos.novoPedido()
    sistema_pedidos.novoPedido()

    print(sistema_pedidos.exibirPedido())

    sistema_pedidos.cancelarPedido()  
    print(sistema_pedidos.exibirPedido()) 

    sistema_pedidos.cancelarPedido()  
    print(sistema_pedidos.exibirPedido())

    sistema_pedidos.cancelarPedido() 


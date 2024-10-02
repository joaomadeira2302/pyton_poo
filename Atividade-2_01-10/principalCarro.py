from carro import Carro


carro1 = Carro("Toyota", "Corolla", 2020, 250.0)
carro2 = Carro("Fiat", "Uno", 2011, 150.0)


print("Detalhes do Carro 1:")
carro1.exibirDetalhes()
dias_aluguel1 = 3
print(f"Custo do aluguel para {dias_aluguel1} dias:{carro1.calcularPrecoAluguel(dias_aluguel1):.2f}\n")


print("Detalhes do Carro 2:")
carro2.exibirDetalhes()
dias_aluguel2 = 5
print(f"Custo do aluguel para {dias_aluguel2} dias:{carro2.calcularPrecoAluguel(dias_aluguel2):.2f}\n")
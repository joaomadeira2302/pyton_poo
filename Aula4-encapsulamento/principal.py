from funcionario import Funcionario

funcionario1 = Funcionario("Gerente", 3000)
print("Seu cargo atual é:",funcionario1.getCargo())

#Tentando mudar o valor do atributo
funcionario1.__cargo = "Supervisor"
funcionario1.setCargo("Engenheiro")
print("Seu cargo atual é: ",funcionario1.getCargo())

#EXIBINDO O SALÁRIO
print("o seu salário atueal é ",funcionario1.salario)

funcionario1.salario = -100
print("O se salário atual é ", funcionario1.salario)
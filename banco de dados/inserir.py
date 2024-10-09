import sqlite3 #Importando uma biblioteca d banco de dados 

#Estbelecendo conexão com o banco 
conexao = sqlite3.connect("departamento.db") #estamos criando um arquivo que irá guardar o nosso banco de dados

#Passo2 - Verificar se a tabela existe ou não 
tabela = """
CREATE TABLE IF NOT EXISTS funcionario(
    código INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    salario FLOAT,
    cargo VARCHAR(100)
);
"""
#Passo3 - Acessar objetivo da biblioteca sqçite3 para manipular o banco
consulta = conexao.cursor() #O objeto cursor() é responsável por manipular dados do banco

#Passo4 - executar o comando de criação de tabela 
consulta.execute(tabela)

#Passo5 - Inserir dados na tabela
nome = input("Informe o nome do funcionário:")
salario = float(input("Informe o salário do funcionário:"))
cargo = input("Informe o cargo do funcionário: ")

#Passo6 - Criando comando SQL para inserir os dados 
sql = "INSERT INTO funcionario VALUES(?,?,?,?)" #Colocamos ? no lugar dos dados reais, para evitar possíveis ataques de sql injection. Isso é uma implementação da biblioteca sqlite3

#Passo7 - Organizar os dados que irão substituir a ? no comando sql para inserir 
campos = (None, nome, salario, cargo)#Criando uma tupla comos dados que serão trocados pela ?. Ao informar o valor 'None', estamos dizendo que será atribuído o valor padrão do AUTOINCREMENT.

#Passo8 - Utilizar o comando sql e substituir ? pelos campos
consulta.execute(sql, campos)

#Passo9 - Gravar os dados no banco
conexao.commit()

print(consulta.rowcount, "linha(s) inseridas com sucesso")

#Passo10 - Finalizar conexão
conexao.close()
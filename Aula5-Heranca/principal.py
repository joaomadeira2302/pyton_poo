from funcionario import Pessoa, Engenheiro, Secretario

f1 = Pessoa("Joana", "Gerente")
engenheiro1 = Engenheiro("Roberto", "Engenheiro Pleno")
secretario1 = Secretario("Carlos", "Secretário Executivo")

f1.informacoes()

engenheiro1.informacoes()
engenheiro1.mostraDetalhes()

secretario1.relatorio()
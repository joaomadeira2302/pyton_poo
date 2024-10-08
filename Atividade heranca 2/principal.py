from personagem import Personagem, Jogador, Monstro

jogador1 = Jogador("Legolas", "Elfo")
monstro1 = Monstro("Vorath", "Dragão", 50)

jogador1.atacar()
jogador1.usarHabilidade("Visão Noturna")
jogador1.coletarItem("Espada Longa")
jogador1.coletarItem("Escudo de Madeira")


monstro1.atacar()
monstro1.exibirInformacoes()
aliado = monstro1.invocarAliado("Zyphor", "Esqueleto")
aliado.exibirInformacoes()
monstro1.defender()

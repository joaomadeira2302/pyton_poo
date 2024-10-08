class Personagem:
    def __init__(self, nome, vida=5):
        self._nome = nome
        self._vida = vida

    def atacar(self):
        print(f"{self._nome} está atacando!")


class Jogador(Personagem):
    def __init__(self, nome, raca, vida=5):
        super().__init__(nome, vida)
        self._raca = raca
        self._inventario = []  # Lista para armazenar itens

    def usarHabilidade(self, poder):
        print(f"{self._nome} usou a habilidade: {poder}")

    def coletarItem(self, item):
        self._inventario.append(item)
        print(f"Item '{item}' coletado! Inventário: {', '.join(self._inventario)}")


class Monstro(Personagem):
    def __init__(self, nome, tipo, forca, vida=20):
        super().__init__(nome, vida)
        self._tipo = tipo
        self._forca = forca

    def exibirInformacoes(self):
        print(f"Monstro: {self._nome}, Tipo: {self._tipo}, Vida: {self._vida}, Força: {self._forca}")

    def invocarAliado(self, nomeAliado, tipoAliado):
        aliado = Monstro(nomeAliado, tipoAliado, self._forca // 2)
        print(f"{self._nome} invocou um aliado: {aliado._nome}, Tipo: {aliado._tipo}, Força: {aliado._forca}")
        return aliado

    def defender(self):
        self._vida -= 1
        print(f"{self._nome} se defendeu! Vida restante: {self._vida}")

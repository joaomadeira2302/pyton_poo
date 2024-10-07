from animal import Animal, Mamifero, Reptil

animal1 = Animal("Elefante", 10)
animal1.exibirInfo()
animal1.som("Trumpet!")

mamifero1 = Mamifero("Leão", 5)
mamifero1.exibirInfo()
mamifero1.som("Rugido!")
mamifero1.alimentarFilhotes()


reptil1 = Reptil("Cobra", 2)
reptil1.exibirInfo()
reptil1.som("Sibilo!")
reptil1.mudarPele()

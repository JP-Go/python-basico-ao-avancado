class Escritor:
    """ Representa um escritor, a pessoa que escreve"""

    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


class Caneta:

    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    def escrever(self):
        print("Caneta escrevendo")


class MaquinaDeEscrever:

    def __init__(self):
        pass

    def escrever(self):
        print("Máquina escrevendo")

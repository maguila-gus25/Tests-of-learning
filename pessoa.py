class Pessoa:
    def __init__(self, nome=""):
        self.__nome = nome

    def __init__(self, idade=int):
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

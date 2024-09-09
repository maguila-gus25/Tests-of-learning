class Cliente:

    def __init__(self, codigo: int, endereco: str):
        self.__codigo = None
        self.__endereco = None
        if isinstance(codigo, int):
            self.__codigo = codigo
        if isinstance(endereco, str):
            self.__endereco = endereco

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def endereco(self) -> str:
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco: str):
        if isinstance(endereco, str):
            self.__endereco = endereco

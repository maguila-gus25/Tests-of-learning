from cliente import Cliente

class NotaFiscal:
    def __init__(self, numero: int, cliente: Cliente):
        self.__numero = None
        self.__cliente = None
        if isinstance(numero, int):
            self.__numero = numero
        if isinstance(cliente, Cliente):
            self.__cliente = cliente

    @property
    def numero(self) -> int:
        return self.__numero

    @numero.setter
    def numero(self, numero: int):
        if isinstance(numero, int):
            self.__numero = numero

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente

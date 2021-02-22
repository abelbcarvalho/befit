from core.model.abs_base import AbsBase
from core.data.data import Data


class Person(AbsBase):
    """Classe que representa uma
    pessoa que quer emagrecer.

    Args:
        AbsBase: Classe abstrata
    """

    def __init__(self):
        """Nova Pessoa.
        """
        super().__init__()
        self._nome = ''
        self._sexo = ''
        self._data = Data()
        self._altura = 0.0
        self._peso_inicial = 0.0
        self._peso_atual = 0.0
        self._cent_inicial = 0
        self._cent_atual = 0

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome

    @property
    def sexo(self) -> str:
        return self._sexo

    @sexo.setter
    def sexo(self, sexo: str) -> None:
        self._sexo = sexo

    @property
    def data(self) -> Data:
        return self._data

    @property
    def altura(self) -> float:
        return self._altura

    @altura.setter
    def altura(self, altura: float) -> None:
        self._altura = altura

    @property
    def peso_inicial(self) -> float:
        return self._peso_inicial

    @peso_inicial.setter
    def peso_inicial(self, peso_inicial: float) -> None:
        self._peso_inicial = peso_inicial

    @property
    def peso_atual(self) -> float:
        return self._peso_atual

    @peso_atual.setter
    def peso_atual(self, peso_atual: float) -> None:
        self._peso_atual = peso_atual

    @property
    def cent_inicial(self) -> int:
        return self._cent_inicial

    @cent_inicial.setter
    def cent_inicial(self, cent_inicial: int) -> None:
        self._cent_inicial = cent_inicial

    @property
    def cent_atual(self) -> int:
        return self._cent_atual

    @cent_atual.setter
    def cent_atual(self, cent_atual: int) -> None:
        self._cent_atual = cent_atual

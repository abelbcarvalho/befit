from abc import ABCMeta


class AbsBase(metaclass=ABCMeta):
    """Classe base para o banco de dados.
    """

    def __init__(self):
        self._id = 0
        self._fk = 0

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        self._id = id

    @property
    def fk(self) -> int:
        return self._fk

    @fk.setter
    def fk(self, fk: int) -> None:
        self._fk = fk

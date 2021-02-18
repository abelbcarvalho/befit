from core.model.abs_base import AbsBase
from core.data.data import Data


class Centimetros(AbsBase, Data):
    """Registro de centimetros de abdomem.
    """

    def __init__(self):
        """Nova Cintura.
        """
        super().__init__()
        self._cintura = 0.0
        self._comment = ''

    @property
    def cintura(self) -> float:
        return self._cintura

    @cintura.setter
    def cintura(self, cintura: float) -> None:
        self._cintura = cintura

    @property
    def comment(self) -> str:
        return self._comment

    @comment.setter
    def comment(self, comment: str) -> None:
        self._comment = comment

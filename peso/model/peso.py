from core.model.abs_base import AbsBase
from core.data.data import Data


class Peso(AbsBase, Data):
    """Registro de peso.
    """

    def __init__(self):
        """Novo Peso.
        """
        super().__init__()
        self._peso = 0.0
        self._comment = ''

    @property
    def peso(self) -> float:
        return self._peso

    @peso.setter
    def peso(self, peso: float) -> None:
        self._peso = peso

    @property
    def comment(self) -> str:
        return self._comment

    @comment.setter
    def comment(self, comment: str) -> None:
        self._comment = comment

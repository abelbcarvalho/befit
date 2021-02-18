class Data:
    """Classe que representa data.
    """

    def __init__(self) -> None:
        """Nova Data.
        """
        self._dia = 0
        self._mes = 0
        self._ano = 0

    @property
    def dia(self) -> int:
        return self._dia

    @dia.setter
    def dia(self, dia: int) -> None:
        self._dia = dia

    @property
    def mes(self) -> int:
        return self._mes

    @mes.setter
    def mes(self, mes: int) -> None:
        self._mes = mes

    @property
    def ano(self) -> int:
        return self._dia

    @ano.setter
    def ano(self, ano: int) -> None:
        self._ano = ano

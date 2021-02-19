class Data:
    """Classe que representa data.
    """

    def __init__(self) -> None:
        """Nova Data.
        """
        self._dia = 0
        self._mes = 0
        self._ano = 0

    def __str__(self) -> str:
        """Objeto como string.

        Returns:
            str: a data formatada.
        """
        dat = (str(self.dia), '0'+str(self.dia))[len(str(self.dia)) < 2]
        dat += '/' + (str(self.mes), '0'+str(self.mes))[len(str(self.mes)) < 2]
        dat += '/' + str(self.ano)
        return dat

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
        return self._ano

    @ano.setter
    def ano(self, ano: int) -> None:
        self._ano = ano

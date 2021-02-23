from core.data.data import Data
from datetime import datetime as date


class DataCheck:
    """Clase para teste de data.
    """

    def is_valid_data(self, data: Data) -> bool:
        """Testa e verifica se uma data é válida.

        Args:
            data (Data): Instancia com os dados.

        Returns:
            bool: True se data valida, senão False.
        """
        if data.dia < 1 or data.mes < 1 or data.ano < 1920:
            return False
        elif data.dia > 31 or data.mes > 12:
            return False
        elif date.now().year < data.ano:
            return False
        elif data.mes == 2:
            if data.dia > 29:
                return False
            elif not self._bisexto(ano=data.ano):
                return False if data.dia > 28 else True
            return True   
        elif self._mes_trinta(mes=data.mes):
            return data.dia < 31
        else:
            return data.dia < 32

    def _bisexto(self, ano: int) -> bool:
        if ano % 400 == 0:
            return True
        elif ano % 4 == 0 and ano % 100 != 0:
            return True
        else:
            return False

    def _mes_trinta(self, mes: int) -> bool:
        trinta = {
            (4,6,9,11): True,
            (1,3,5,7,8,10,12): False,
        }
        found = (m for meses, m in trinta.items() if mes in meses)
        return next(found, None)
